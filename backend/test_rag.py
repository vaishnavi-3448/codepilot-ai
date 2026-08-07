from services.document_loader import DocumentLoader
from services.text_splitter import TextChunker
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore
from services.rag_pipeline import RAGPipeline


loader = DocumentLoader()

chunker = TextChunker(
    chunk_size=80,
    chunk_overlap=20
)

embedding_service = EmbeddingService()

vector_store = VectorStore(
    embedding_service.get_embedding_model()
)

text = loader.load("uploads/sample.txt")

chunks = chunker.split(text)
vector_store.clear()
vector_store.add_documents(chunks)

rag = RAGPipeline(vector_store)

result = rag.ask(
    "What does ChromaDB do?"
)

print("\n" + "=" * 60)
print("GEMINI ANSWER")
print("=" * 60)
print(result["answer"])

print("\n" + "=" * 60)
print("RETRIEVED SOURCES")
print("=" * 60)

for i, source in enumerate(result["sources"], start=1):
    print(f"\nSOURCE {i}")
    print("-" * 40)
    print(source.page_content)