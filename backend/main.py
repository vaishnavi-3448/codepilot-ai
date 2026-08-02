from fastapi import FastAPI

app = FastAPI(
    title="CodePilot AI",
    description="Multi-Agent AI Engineering Copilot",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CodePilot AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }