from pathlib import Path


class RepositoryScanner:
    """
    Scans a repository and returns relevant source files.
    """

    # Files/directories that should not be indexed
    IGNORED_DIRECTORIES = {
        ".git",
        ".github",
        "__pycache__",
        "node_modules",
        "venv",
        ".venv",
        "env",
        ".env",
        "dist",
        "build",
        ".next",
        ".vite",
        "coverage",
        "chroma_db",
    }

    # File extensions that we currently understand
    SUPPORTED_EXTENSIONS = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".java": "java",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".c": "c",
        ".h": "c",
        ".hpp": "cpp",
        ".cs": "csharp",
        ".go": "go",
        ".rs": "rust",
        ".php": "php",
        ".html": "html",
        ".css": "css",
        ".scss": "scss",
        ".sql": "sql",
        ".md": "markdown",
        ".txt": "text",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
    }

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path)

        if not self.repository_path.exists():
            raise FileNotFoundError(
                f"Repository not found: {repository_path}"
            )

        if not self.repository_path.is_dir():
            raise ValueError(
                f"Path is not a directory: {repository_path}"
            )

    def scan(self):
        """
        Scan repository and return supported files.
        """

        files = []

        for path in self.repository_path.rglob("*"):

            if not path.is_file():
                continue

            if self._should_ignore(path):
                continue

            extension = path.suffix.lower()

            if extension not in self.SUPPORTED_EXTENSIONS:
                continue

            files.append(path)

        return files

    def _should_ignore(self, path: Path):
        """
        Check whether a file belongs to an ignored directory.
        """

        return any(
            directory in self.IGNORED_DIRECTORIES
            for directory in path.parts
        )

    def get_language(self, file_path: Path):
        """
        Return programming language based on file extension.
        """

        return self.SUPPORTED_EXTENSIONS.get(
            file_path.suffix.lower(),
            "unknown"
        )