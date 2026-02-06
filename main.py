
import os
import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
users_vault = {}
revenue_logs = []

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Aura Autonomous Engine</h1><p>Plan: $10 for 1000 Credits</p><a href='/signup'>Register Now</a>"

@app.get("/signup", response_class=HTMLResponse)
async def signup():
    return "<h2>Sign Up</h2><form action='/activate' method='post'><input name='user' placeholder='User'><input name='txid' placeholder='TXID'><button>Activate</button></form>"

@app.post("/activate", response_class=HTMLResponse)
async def activate(user: str = Form(...), txid: str = Form(...)):
    users_vault[user] = {"credits": 1000}
    revenue_logs.append({"user": user, "txid": txid, "amt": 10})
    return f"<h1>Success!</h1><p>Welcome {user}. Status: Active</p>"

@app.get("/shahroze-admin-access", response_class=HTMLResponse)
async def admin():
    total = sum(log['amt'] for log in revenue_logs)
    return f"<h1>Admin Panel</h1><p>Total Revenue: ${total}</p><p>Total Users: {len(users_vault)}</p>"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
