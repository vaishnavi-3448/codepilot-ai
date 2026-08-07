from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """
    Splits documents into overlapping chunks
    for embedding and retrieval.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def split(self, text: str):
        """
        Returns a list of text chunks.
        """
        return self.splitter.split_text(text)