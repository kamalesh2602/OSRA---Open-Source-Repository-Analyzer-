from fastapi import FastAPI
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OSRA API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://osra-v1.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "OSRA Backend Running"
    }