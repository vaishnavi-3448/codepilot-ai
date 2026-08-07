from services.repository_scanner import RepositoryScanner


repository_path = "../"

scanner = RepositoryScanner(repository_path)

files = scanner.scan()

print(f"\nFound {len(files)} supported files\n")

for file in files:
    language = scanner.get_language(file)

    print(
        f"{file}  →  {language}"
    )