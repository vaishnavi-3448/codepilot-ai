from pathlib import Path

from services.repository_scanner import RepositoryScanner
from services.file_reader import FileReader
from services.code_chunker import CodeChunker
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore


class RepositoryIndexer:
    """
    End-to-end repository indexing pipeline.
    """

    def __init__(self, repository_path: str):

        self.repository_root = Path(
            repository_path
        ).resolve()

        self.scanner = RepositoryScanner(
            str(self.repository_root)
        )

        self.reader = FileReader()

        self.chunker = CodeChunker(
            chunk_size=1000,
            chunk_overlap=150
        )

        embedding_service = EmbeddingService()

        self.vector_store = VectorStore(
            embedding_service.get_embedding_model(),
            collection_name="code_repository"
        )

    def index(self):

        print("Indexing repository...")

        files = self.scanner.scan()

        all_chunks = []

        for file_path in files:

            document = self.reader.read(
                file_path,
                self.repository_root
            )

            if document is None:
                continue

            chunks = self.chunker.split_document(
                document
            )

            all_chunks.extend(chunks)

        print(f"Files found: {len(files)}")
        print(f"Chunks created: {len(all_chunks)}")

        # Clear old repository index
        self.vector_store.clear()

        # Store new chunks
        self.vector_store.add_documents(
            all_chunks
        )

        print("Repository indexing complete.")

        return {
            "files": len(files),
            "chunks": len(all_chunks)
        }

    def search(self, query: str, k: int = 5):

        return self.vector_store.similarity_search(
            query,
            k=k
        )