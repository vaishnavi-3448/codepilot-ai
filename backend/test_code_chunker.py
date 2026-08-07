from pathlib import Path

from services.repository_scanner import RepositoryScanner
from services.file_reader import FileReader
from services.code_chunker import CodeChunker


repository_root = Path("../").resolve()

scanner = RepositoryScanner(
    str(repository_root)
)

reader = FileReader()

chunker = CodeChunker(
    chunk_size=500,
    chunk_overlap=100
)

files = scanner.scan()

print(f"\nFound {len(files)} files\n")

for file in files[:3]:

    document = reader.read(
        file,
        repository_root
    )

    if document is None:
        continue

    chunks = chunker.split_document(document)

    print("=" * 70)
    print(f"FILE: {document['file_path']}")
    print(f"LANGUAGE: {document['language']}")
    print(f"CHUNKS: {len(chunks)}")

    for chunk in chunks:

        print("\n" + "-" * 50)

        print("CHUNK ID:", chunk["metadata"]["chunk_id"])

        print("CONTENT:")
        print(chunk["content"])

        print("\nMETADATA:")
        print(chunk["metadata"])