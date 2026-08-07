from services.repository_indexer import RepositoryIndexer


repository_path = "../"

indexer = RepositoryIndexer(
    repository_path
)

result = indexer.index()

print("\n" + "=" * 60)
print("REPOSITORY INDEXING COMPLETE")
print("=" * 60)

print(
    f"Files indexed: {result['files']}"
)

print(
    f"Chunks created: {result['chunks']}"
)

print(
    f"Chunks stored: "
    f"{indexer.vector_store.get_count()}"
)