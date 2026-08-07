from pathlib import Path

from services.repository_scanner import RepositoryScanner
from services.file_reader import FileReader


repository_root = Path("../").resolve()

scanner = RepositoryScanner(
    str(repository_root)
)

reader = FileReader()

files = scanner.scan()

print(f"\nFound {len(files)} files\n")

for file in files[:5]:

    document = reader.read(
        file,
        repository_root
    )

    if document is None:
        continue

    print("=" * 60)

    print("FILE:", document["file_path"])
    print("LANGUAGE:", document["language"])
    print("EXTENSION:", document["extension"])

    print("\nCONTENT PREVIEW:")
    print(document["content"][:300])