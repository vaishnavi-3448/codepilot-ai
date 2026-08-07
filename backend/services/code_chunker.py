from langchain_text_splitters import RecursiveCharacterTextSplitter


class CodeChunker:
    """
    Splits source code into chunks while attempting
    to preserve programming-language structure.
    """

    LANGUAGE_SEPARATORS = {
        "python": [
            "\nclass ",
            "\ndef ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "javascript": [
            "\nclass ",
            "\nfunction ",
            "\nconst ",
            "\nlet ",
            "\nvar ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "typescript": [
            "\nclass ",
            "\nfunction ",
            "\nconst ",
            "\nlet ",
            "\ninterface ",
            "\ntype ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "java": [
            "\nclass ",
            "\npublic ",
            "\nprivate ",
            "\nprotected ",
            "\nstatic ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "cpp": [
            "\nclass ",
            "\nvoid ",
            "\nint ",
            "\nfloat ",
            "\ndouble ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "c": [
            "\nstruct ",
            "\nvoid ",
            "\nint ",
            "\nfloat ",
            "\ndouble ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "go": [
            "\ntype ",
            "\nfunc ",
            "\n\n",
            "\n",
            " ",
            "",
        ],

        "rust": [
            "\nstruct ",
            "\nimpl ",
            "\nfn ",
            "\n\n",
            "\n",
            " ",
            "",
        ],
    }

    DEFAULT_SEPARATORS = [
        "\n\n",
        "\n",
        " ",
        "",
    ]

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 150,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_document(self, document: dict):
        """
        Split a document and attach metadata to every chunk.
        """

        content = document["content"]
        language = document["language"]

        separators = self.LANGUAGE_SEPARATORS.get(
            language,
            self.DEFAULT_SEPARATORS
        )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=separators,
        )

        chunks = splitter.split_text(content)

        documents = []

        for index, chunk in enumerate(chunks):

            metadata = {
                "file_path": document["file_path"],
                "file_name": document["file_name"],
                "extension": document["extension"],
                "language": language,
                "chunk_id": index,
            }

            documents.append({
                "content": chunk,
                "metadata": metadata,
            })

        return documents