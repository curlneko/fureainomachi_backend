from fastapi import FastAPI

app = FastAPI(title="Fureainomachi API", version="0.1.0")


@app.get("/home")
def read_root():
    return {"message": "Hello World"}
