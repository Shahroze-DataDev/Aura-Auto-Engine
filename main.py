
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Aura-335 Integrated Engine")

# 1. ہوم پیج (پروٹوزون)
@app.get("/")
def home():
    return {"status": "Online", "owner": "Shahroz", "engine": "335 Tasks Ready"}

# 2. پہلا ٹاسک (آپ کا نیا کوڈ)
@app.get("/run-task-1")
def task_one():
    # یہاں آپ کا اصل آٹومیشن لاجک آئے گا
    return {"task_id": 1, "status": "Executing", "details": "Processing Data..."}

# 3. دوسرا ٹاسک (مستقبل کے لیے)
@app.get("/task2")
def second_task():
    return {"task": 2, "status": "Pending"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
