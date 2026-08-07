from pathlib import Path

from services.repository_scanner import RepositoryScanner


class FileReader:
    """
    Safely reads source files from a repository
    and returns their content with metadata.
    """

    def read(
        self,
        file_path: Path,
        repository_root: Path
    ):
        """
        Read a source file and return structured metadata.
        """

        try:
            content = file_path.read_text(
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            return None

        relative_path = file_path.relative_to(
            repository_root
        )

        language = RepositoryScanner.SUPPORTED_EXTENSIONS.get(
            file_path.suffix.lower(),
            "unknown"
        )

        return {
            "content": content,
            "file_path": str(relative_path),
            "file_name": file_path.name,
            "extension": file_path.suffix.lower(),
            "language": language,
        }