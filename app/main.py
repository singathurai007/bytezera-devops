from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Bytezera FastAPI application"}


@app.get("/health")
def health():
    return {"status": "healthy"}