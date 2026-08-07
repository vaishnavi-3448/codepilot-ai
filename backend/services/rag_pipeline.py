import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class RAGPipeline:
    """
    Retrieval-Augmented Generation pipeline.

    Retrieves relevant documents from ChromaDB
    and uses Gemini to generate an answer.
    """

    def __init__(self, vector_store):
        self.vector_store = vector_store

        api_key = os.getenv("GEMINI_API_KEY")
        model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.6-flash"
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set in the environment."
            )

        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key
        )

    def ask(self, question: str):
        """
        Retrieve relevant chunks and generate
        an answer using Gemini.
        """

        documents = self.vector_store.similarity_search(
            question,
            k=3
        )

        if not documents:
            return {
                "answer": "I couldn't find relevant information.",
                "sources": []
            }

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = f"""
You are CodePilot AI, an AI engineering assistant.

Answer the user's question using ONLY the
provided context.

If the context does not contain enough information
to answer the question, say:

"I couldn't find that information in the provided documents."

Do not invent information.

--- CONTEXT ---

{context}

--- QUESTION ---

{question}

--- ANSWER ---
"""

        response = self.llm.invoke(prompt)
        answer = response.content

        if isinstance(answer, list):
            answer = "\n".join(
                item.get("text", "")
                for item in answer
                if isinstance(item, dict) and item.get("text")
            )

        return {
            "answer": answer,
            "sources": documents
        }
        