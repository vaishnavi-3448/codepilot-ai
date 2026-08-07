class CodeRetriever:
    """
    Shared retrieval layer for CodePilot agents.
    """

    def __init__(self, repository_indexer):
        self.repository_indexer = repository_indexer

    def search(self, query: str, k: int = 5):

        results = self.repository_indexer.search(
            query,
            k=k
        )

        return results