
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Aura Auto Engine")

@app.get("/")
def home():
    return {"status": "Online", "owner": "Shahroz", "engine": "335 Tasks Ready"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
