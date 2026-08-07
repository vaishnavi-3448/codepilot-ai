from pathlib import Path


class DocumentLoader:
    """
    Loads text documents from disk.
    Later this class will support PDFs,
    code files and entire repositories.
    """

    SUPPORTED_EXTENSIONS = {".txt"}

    def load(self, file_path: str) -> str:
        """
        Reads a document and returns its contents.

        Args:
            file_path (str): Path to the document.

        Returns:
            str: Document text.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        return text