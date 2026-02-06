
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import os
import random

app = FastAPI(title="Aura Business Engine")

@app.get("/", response_class=HTMLResponse)
def business_dashboard():
    return '''
    <html>
        <head>
            <title>Shahroze Business Portal</title>
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: #010409; color: #c9d1d9; padding: 20px; }
                .stat-container { display: flex; gap: 20px; justify-content: center; margin-bottom: 30px; }
                .stat-box { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; width: 200px; }
                .btn-group { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; max-width: 800px; margin: auto; }
                button { background: #238636; color: white; border: none; padding: 15px; border-radius: 6px; cursor: pointer; font-weight: bold; }
                button:hover { background: #2ea043; }
                .live-feed { background: #0d1117; border-left: 5px solid #1f6feb; padding: 15px; margin-top: 30px; text-align: left; }
                h1 { color: #58a6ff; }
            </style>
        </head>
        <body>
            <h1>Aura-335: Earning Mode Active</h1>
            <div class="stat-container">
                <div class="stat-box"><h3>USD/PKR</h3><p id="rate">Loading...</p></div>
                <div class="stat-box"><h3>Active Jobs</h3><p>12 Found</p></div>
                <div class="stat-box"><h3>Health</h3><p style="color: #238636;">Stable</p></div>
            </div>
            
            <div class="btn-group">
                <button onclick="location.href='/task-01/scout-bulk'">Scout New Jobs</button>
                <button onclick="location.href='/task-11/proposal-ai'">Generate AI Proposal</button>
                <button onclick="location.href='/task-21/email-extractor'">Extract Client Leads</button>
                <button onclick="location.href='/task-41/invoice-gen'">Create Invoice</button>
                <button onclick="location.href='/task-42/dollar-tracker'">Check Profit Rate</button>
                <button style="background: #da3633;" onclick="location.href='/'">Refresh Feed</button>
            </div>

            <div class="live-feed">
                <h3>Live Business Intelligence:</h3>
                <p># System is monitoring Upwork for 'Data Developer' roles...</p>
                <p># Ready to automate your first $100 project.</p>
            </div>

            <script>
                fetch('/task-42/dollar-tracker').then(res => res.json()).then(data => {
                    document.getElementById('rate').innerText = 'Rs. ' + data.live_rate;
                });
            </script>
        </body>
    </html>
    '''

# --- بزنس فنکشنز ---
@app.get("/task-42/dollar-tracker")
def t42():
    return {"live_rate": random.uniform(278.5, 282.0)}

@app.get("/task-01/scout-bulk")
def t1():
    return {"status": "Monitoring", "jobs": [{"title": "FastAPI Dev", "budget": "$200"}]}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
