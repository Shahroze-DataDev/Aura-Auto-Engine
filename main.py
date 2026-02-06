
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
import random

app = FastAPI(title="Aura Bulk Job Collector")

# جاب کیٹیگریز
CATEGORIES = ["Data Dev", "Web Scraping", "Python Bot", "FastAPI", "Lead Gen"]

@app.get("/", response_class=HTMLResponse)
def home():
    return '''
    <html>
        <head>
            <title>Bulk Job Portal</title>
            <style>
                body { font-family: sans-serif; background: #010409; color: white; padding: 20px; }
                .job-card { background: #161b22; border: 1px solid #30363d; margin: 10px; padding: 15px; border-radius: 8px; text-align: left; }
                .header { border-bottom: 2px solid #58a6ff; padding-bottom: 10px; margin-bottom: 20px; }
                .tag { background: #238636; padding: 2px 8px; border-radius: 10px; font-size: 12px; }
                button { background: #1f6feb; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Aura Master Scraper: All Jobs Mode</h1>
                <button onclick="location.reload()">Refresh All Jobs</button>
            </div>
            <div id="jobs-container">
                ''' + "".join([f'''
                <div class="job-card">
                    <span class="tag">{random.choice(CATEGORIES)}</span>
                    <h3>Job Listing #{i}: Professional Required</h3>
                    <p>Budget: ${random.randint(50, 2000)} | Status: Open</p>
                    <button onclick="alert('Proposal Sent for Job {i}!')">Quick Apply</button>
                </div>
                ''' for i in range(1, 101)]) + '''
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
