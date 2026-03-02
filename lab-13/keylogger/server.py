from fastapi import FastAPI, UploadFile, File
from datetime import datetime
import os

app = FastAPI()
os.makedirs("uploads", exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    filename = f"uploads/{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "wb") as f:
        f.write(content)
    return {"status": "ok", "size": len(content)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

