from services.repository_indexer import RepositoryIndexer


repository = RepositoryIndexer("../")

result = repository.index()

print("\nINDEX RESULT")
print("=" * 50)

print(f"Files  : {result['files']}")
print(f"Chunks : {result['chunks']}")