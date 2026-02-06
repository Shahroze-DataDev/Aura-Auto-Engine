
from fastapi import FastAPI
import uvicorn
import os
import datetime

app = FastAPI(title="Aura-335 Master Engine")

@app.get("/")
def home():
    return {
        "status": "Online", 
        "owner": "Shahroz", 
        "engine": "335 Tasks Ready",
        "server_time": str(datetime.datetime.now())
    }

@app.get("/run-task-1")
def task_one():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "task_id": 1,
        "name": "System Health & Automation Check",
        "status": "Completed Successfully",
        "execution_time": current_time,
        "message": "Shahroz, your first automated task is live!"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
