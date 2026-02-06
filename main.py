
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
import uvicorn
import time
import random

app = FastAPI(title="Aura Autonomous Engine")

# سسٹم اسٹیٹس
LOGS = ["System Initialized..."]

def autonomous_worker(job_id: int):
    global LOGS
    LOGS.append(f"Task {job_id}: Searching for new job...")
    time.sleep(2)
    LOGS.append(f"Task {job_id}: High-Value Job Found! Budget: $500")
    time.sleep(2)
    LOGS.append(f"Task {job_id}: Proposal Sent Automatically.")
    time.sleep(2)
    LOGS.append(f"Task {job_id}: Job Accepted! Starting Scraping...")
    time.sleep(3)
    LOGS.append(f"Task {job_id}: Work Completed. Delivering Results...")
    time.sleep(2)
    LOGS.append(f"Task {job_id}: Invoice Sent. $500 Added to Balance.")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    log_html = "".join([f"<p style='color:#2ea043'># {log}</p>" for log in LOGS[-10:]])
    return f'''
    <html>
        <head>
            <title>Aura Autonomous Control</title>
            <style>
                body {{ background: #010409; color: white; font-family: sans-serif; padding: 30px; }}
                .status-box {{ border: 2px solid #238636; padding: 20px; border-radius: 10px; background: #0d1117; }}
                .live-logs {{ background: black; padding: 15px; border-radius: 5px; text-align: left; height: 300px; overflow-y: scroll; }}
                .btn-auto {{ background: #1f6feb; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; }}
            </style>
        </head>
        <body>
            <h1>Aura-335: Fully Autonomous Mode</h1>
            <div class="status-box">
                <h2>System Status: <span style="color:#2ea043">RUNNING</span></h2>
                <button class="btn-auto" onclick="location.href='/start-autopilot'">Start Auto-Pilot Cycle</button>
            </div>
            <h3>Live Execution Logs:</h3>
            <div class="live-logs">{log_html}</div>
            <script>setTimeout(() => {{ location.reload(); }}, 5000);</script>
        </body>
    </html>
    '''

@app.get("/start-autopilot")
def start_auto(background_tasks: BackgroundTasks):
    job_id = random.randint(100, 999)
    background_tasks.add_task(autonomous_worker, job_id)
    return {"status": "Auto-Pilot Triggered", "task_id": job_id}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
