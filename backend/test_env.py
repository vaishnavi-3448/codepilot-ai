import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print("Gemini API key loaded successfully.")
    print("Key starts with:", key[:6] + "...")
else:
    print("Gemini API key NOT FOUND.")