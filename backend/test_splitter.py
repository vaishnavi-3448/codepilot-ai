from services.document_loader import DocumentLoader
from services.text_splitter import TextChunker


loader = DocumentLoader()
chunker = TextChunker(
    chunk_size=80,
    chunk_overlap=20
)

text = loader.load("uploads/sample.txt")

chunks = chunker.split(text)

print(f"\nTotal Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print("=" * 50)
    print(chunk)
    print()