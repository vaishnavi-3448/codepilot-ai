from dotenv import load_dotenv

load_dotenv()
from services.repository_indexer import RepositoryIndexer
from langchain_google_genai import ChatGoogleGenerativeAI


class CodeRAG:

    def __init__(self, repository_path: str):

        self.indexer = RepositoryIndexer(
            repository_path
        )

        self.llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    def index_repository(self):

        return self.indexer.index()

    def ask(self, question: str, k: int = 5):

        results = (
            self.indexer.vector_store.similarity_search(
                question,
                k=k
            )
        )

        if not results:
            return {
                "answer": "I could not find relevant code.",
                "sources": []
            }

        context_parts = []

        for result in results:

            file_path = result.metadata.get(
                "file_path",
                "unknown"
            )

            language = result.metadata.get(
                "language",
                "unknown"
            )

            context_parts.append(
                f"""
FILE: {file_path}
LANGUAGE: {language}

CODE:
{result.page_content}
"""
            )

        context = "\n\n".join(
            context_parts
        )

        prompt = f"""
You are CodePilot AI, an AI engineering copilot.

Answer the user's question using ONLY the
repository code provided below.

If the answer cannot be determined from the
provided code, clearly say so.

Always mention the relevant file paths when
possible.

Do not invent code or files.

REPOSITORY CODE:

{context}

USER QUESTION:

{question}
"""

        response = self.llm.invoke(
            prompt
        )

        answer = response.content

        if isinstance(answer, list):

            answer = "\n".join(
                item.get("text", "")
                for item in answer
                if isinstance(item, dict)
                and item.get("text")
            )

        sources = []

        for result in results:

            sources.append({
                "file_path": result.metadata.get(
                    "file_path"
                ),
                "language": result.metadata.get(
                    "language"
                ),
                "content": result.page_content
            })

        return {
            "answer": answer,
            "sources": sources
        }