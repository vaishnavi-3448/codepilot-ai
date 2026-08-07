from services.repository_indexer import RepositoryIndexer
from services.retriever import CodeRetriever


indexer = RepositoryIndexer("../")

retriever = CodeRetriever(
    indexer
)


query = "Where is the FastAPI application created?"

results = retriever.search(
    query,
    k=5
)


print("\nRETRIEVAL RESULTS")
print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nSOURCE {i}")
    print("-" * 60)

    print(
        "File:",
        result.metadata.get(
            "file_path",
            "unknown"
        )
    )

    print(
        "Language:",
        result.metadata.get(
            "language",
            "unknown"
        )
    )

    print("\nContent:")
    print(result.page_content)