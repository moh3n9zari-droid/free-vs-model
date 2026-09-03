from fastapi import FastAPI

app = FastAPI(
    title="Free VS Model AI Gateway"
)


@app.get("/")
def health():
    return {
        "status": "online",
        "service": "AI Gateway"
    }


@app.get("/models")
def models():
    return {
        "available": [
            "premium",
            "open_source",
            "local"
        ]
    }
