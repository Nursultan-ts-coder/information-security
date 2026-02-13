# app.py
from fastapi import FastAPI

app = FastAPI()

# Single POST endpoint
@app.post("/upload")
async def process_upload(logs):
    # Example logic: just return the data with a message
    print(f"Received data: {logs}")
