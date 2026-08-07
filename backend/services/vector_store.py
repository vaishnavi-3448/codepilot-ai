from langchain_chroma import Chroma


class VectorStore:

    def __init__(
        self,
        embedding_model,
        collection_name="documents",
        persist_directory="../chroma_db"
    ):
        self.embedding_model = embedding_model
        self.collection_name = collection_name
        self.persist_directory = persist_directory

        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model,
            collection_name=self.collection_name
        )

    def add_documents(self, chunks):
        """
        Add code/text chunks with metadata to ChromaDB.
        """

        texts = [
            chunk["content"]
            for chunk in chunks
        ]

        metadatas = [
            chunk["metadata"]
            for chunk in chunks
        ]

        if not texts:
            return

        self.db.add_texts(
            texts=texts,
            metadatas=metadatas
        )

    def similarity_search(self, query, k=3):
        """
        Retrieve the k most relevant chunks.
        """

        return self.db.similarity_search(
            query,
            k=k
        )

    def get_count(self):
        """
        Return number of stored chunks.
        """

        return self.db._collection.count()

    def clear(self):
        """
        Delete the current collection and recreate it.
        """

        try:
            self.db.delete_collection()
        except Exception:
            pass

        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model,
            collection_name=self.collection_name
        )