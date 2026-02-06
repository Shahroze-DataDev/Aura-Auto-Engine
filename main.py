
import os
import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, StreamingResponse
import io
from fpdf import FPDF

app = FastAPI()

# Global stats for all users
stats = {"scanned": 15420, "active_users": 85}

@app.get("/", response_class=HTMLResponse)
async def public_home():
    return f'''
    <body style="background:#0d1117; color:white; font-family:sans-serif; text-align:center; padding-top:50px;">
        <div style="background:#161b22; padding:40px; border-radius:15px; border:1px solid #30363d; display:inline-block;">
            <h1 style="color:#58a6ff;">Aura Public Portal</h1>
            <p>Total Leads Scanned: <strong>{stats['scanned']}</strong></p>
            <hr style="border:0.5px solid #30363d;">
            <form action="/dashboard" method="post">
                <input name="u" placeholder="Your Name" required style="padding:10px; margin:10px; background:#0d1117; color:white; border:1px solid #30363d;"><br>
                <button type="submit" style="background:#238636; color:white; padding:10px 30px; border:none; border-radius:5px; cursor:pointer;">Start Free Scrape</button>
            </form>
            <p style="font-size:12px; color:#8b949e; margin-top:20px;">Powered by Shahroze-DataDev Cloud Infrastructure</p>
        </div>
    </body>
    '''

@app.post("/dashboard", response_class=HTMLResponse)
async def dashboard(u: str = Form(...)):
    return f'''
    <div style="background:#0d1117; color:white; min-height:100vh; padding:30px; font-family:sans-serif;">
        <h2>Global Search: Active for {u}</h2>
        <div style="background:#161b22; padding:20px; border:1px solid #30363d; border-radius:10px;">
            <p>Scanning global directories... Please wait.</p>
            <button disabled style="background:#21262d; color:#8b949e; padding:10px;">Scraping UK Market...</button>
        </div>
    </div>
    '''

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
