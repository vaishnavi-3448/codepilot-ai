import os
from pathlib import Path

from dotenv import load_dotenv


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR / ".env")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Check your .env file."
    )