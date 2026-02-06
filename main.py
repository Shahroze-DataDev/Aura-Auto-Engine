
import os
import uvicorn
import nest_asyncio
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root(): return {"status": "Aura Engine Online"}
if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)
    