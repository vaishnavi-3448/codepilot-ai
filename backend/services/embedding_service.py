from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:
    """
    Generates embeddings using a local HuggingFace model.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def get_embedding_model(self):
        return self.embedding_model