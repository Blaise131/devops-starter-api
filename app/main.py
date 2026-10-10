from fastapi import FastAPI

app = FastAPI(
    title="DevOps Starter API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "DevOps Starter API"}


@app.get("/health")
def health():
    return {"status": "healthy"}