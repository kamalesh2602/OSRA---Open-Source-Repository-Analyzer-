from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="OSRA API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "OSRA Backend Running"
    }