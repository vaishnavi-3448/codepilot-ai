from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from services.repository_indexer import RepositoryIndexer
from services.chat_service import ChatService
from services.repository_scanner import RepositoryScanner
import shutil
import zipfile
from fastapi import UploadFile, File

app = FastAPI(
    title="CodePilot AI",
    description="Multi-Agent AI Engineering Copilot",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CodePilot AI 🚀"
    }


# --------------------------------------------------
# Services
# --------------------------------------------------

repository_indexer = RepositoryIndexer("../")

chat_service = ChatService()


# --------------------------------------------------
# Request Models
# --------------------------------------------------

class ChatRequest(BaseModel):

    question: str


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "message": "Welcome to CodePilot AI 🚀"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Repository Indexing
# --------------------------------------------------

@app.post("/index")
def index_repository():

    try:

        result = repository_indexer.index()

        return {
            "message": "Repository indexed successfully",
            "files": result["files"],
            "chunks": result["chunks"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# --------------------------------------------------
# Chat
# --------------------------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        result = chat_service.ask(
            request.question
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# --------------------------------------------------
# Clear Conversation
# --------------------------------------------------

@app.delete("/chat/memory")
def clear_memory():

    chat_service.clear_memory()

    return {
        "message": "Conversation memory cleared"
    }

@app.get("/repository/tree")
def repository_tree():

    repository_root = Path("../").resolve()

    scanner = RepositoryScanner(
        str(repository_root)
    )

    files = scanner.scan()

    tree = []

    for file_path in files:

        relative_path = Path(file_path).resolve().relative_to(
            repository_root
        )

        parts = relative_path.parts

        current_level = tree

        for part in parts[:-1]:

            folder = next(
                (
                    item
                    for item in current_level
                    if item["name"] == part
                    and item["type"] == "folder"
                ),
                None
            )

            if folder is None:

                folder = {
                    "name": part,
                    "type": "folder",
                    "children": []
                }

                current_level.append(folder)

            current_level = folder["children"]


        current_level.append({
            "name": parts[-1],
            "type": "file",
            "path": str(relative_path).replace("\\", "/")
        })


    return {
        "repository": repository_root.name,
        "tree": tree
    }
@app.get("/repository/file")
def repository_file(path: str):

    repository_root = Path("../").resolve()

    requested_file = (
        repository_root / path
    ).resolve()

    # Security: prevent paths outside repository
    try:
        requested_file.relative_to(repository_root)
    except ValueError:
        raise HTTPException(
            status_code=403,
            detail="Access outside repository is not allowed."
        )

    if not requested_file.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    if not requested_file.is_file():
        raise HTTPException(
            status_code=400,
            detail="Path is not a file."
        )

    try:
        content = requested_file.read_text(
            encoding="utf-8"
        )
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Binary files cannot be displayed."
        )

    return {
        "path": path,
        "name": requested_file.name,
        "content": content
    }

@app.post("/repository/upload")
async def upload_repository(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file provided."
        )

    if not file.filename.lower().endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are supported."
        )

    repository_root = Path("../").resolve()
    upload_dir = repository_root / "uploads"

    upload_dir.mkdir(
        exist_ok=True
    )

    zip_path = upload_dir / "repository.zip"

    with open(zip_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    # Temporary extraction directory
    extract_dir = (
        upload_dir / "extracted"
    )

    if extract_dir.exists():

        shutil.rmtree(
            extract_dir
        )

    extract_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    # Safe ZIP extraction
    with zipfile.ZipFile(
        zip_path,
        "r"
    ) as archive:

        for member in archive.infolist():

            member_path = (
                extract_dir / member.filename
            ).resolve()

            try:

                member_path.relative_to(
                    extract_dir.resolve()
                )

            except ValueError:

                raise HTTPException(
                    status_code=400,
                    detail="Unsafe ZIP file."
                )

        archive.extractall(
            extract_dir
        )


    return {
        "message": "Repository uploaded successfully.",
        "filename": file.filename,
        "path": str(extract_dir)
    }