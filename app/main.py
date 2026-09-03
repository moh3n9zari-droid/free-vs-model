from fastapi import FastAPI

from app.router_api import router


app = FastAPI(
    title="Free VS Model AI Gateway"
)


app.include_router(router)


@app.get("/")
def health():

    return {
        "status": "online",
        "service": "AI Gateway"
    }
