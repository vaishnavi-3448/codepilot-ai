from services.document_loader import DocumentLoader
from services.text_splitter import TextChunker
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore


loader = DocumentLoader()
chunker = TextChunker()

embedding_service = EmbeddingService()

vector_store = VectorStore(
    embedding_service.get_embedding_model()
)

text = loader.load("uploads/sample.txt")

chunks = chunker.split(text)

print(f"Created {len(chunks)} chunks")

vector_store.add_documents(chunks)

print("Stored inside ChromaDB")

results = vector_store.similarity_search(
    "What is LangGraph?"
)

print("\nRetrieved Chunks:\n")

for doc in results:
    print("=" * 50)
    print(doc.page_content)