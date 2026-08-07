from services.repository_indexer import RepositoryIndexer


repository_path = "../"

indexer = RepositoryIndexer(
    repository_path
)

indexer.index()

query = "Where is the FastAPI application created?"

results = indexer.vector_store.similarity_search(
    query,
    k=3
)

print("\n" + "=" * 60)
print("CODE SEARCH")
print("=" * 60)

print(f"\nQuery: {query}")

for i, result in enumerate(results, start=1):

    print("\n" + "-" * 60)

    print(f"RESULT {i}")

    print("\nFILE:")
    print(
        result.metadata.get(
            "file_path"
        )
    )

    print("\nLANGUAGE:")
    print(
        result.metadata.get(
            "language"
        )
    )

    print("\nCHUNK:")
    print(result.page_content)