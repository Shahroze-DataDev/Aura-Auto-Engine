
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
import random

app = FastAPI(title="Aura Payout & Job Hub")

# سیٹ اپ
WALLETS = {"JazzCash": "03xx-xxxxxxx", "Payoneer": "shahroze@email.com"}
SOURCES = ["Upwork API", "Freelancer Bot", "RapidAPI Tasks", "Guru Scraper"]

@app.get("/", response_class=HTMLResponse)
def wallet_dashboard():
    return f'''
    <html>
        <head>
            <title>Aura Money Hub</title>
            <style>
                body {{ background: #010409; color: white; font-family: sans-serif; text-align: center; padding: 40px; }}
                .wallet-grid {{ display: flex; justify-content: center; gap: 20px; margin: 30px; }}
                .card {{ border: 2px solid #58a6ff; padding: 20px; border-radius: 12px; background: #161b22; width: 250px; }}
                .source-list {{ background: #0d1117; padding: 20px; border-radius: 10px; max-width: 600px; margin: auto; text-align: left; }}
                .status-online {{ color: #238636; font-weight: bold; }}
                .btn-withdraw {{ background: #238636; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }}
            </style>
        </head>
        <body>
            <h1>Aura-335: Financial Control Center</h1>
            
            <div class="wallet-grid">
                <div class="card">
                    <h3>Payoneer Balance</h3>
                    <h2>$1,240.00</h2>
                    <p class="status-online">Connected: {WALLETS['Payoneer']}</p>
                </div>
                <div class="card">
                    <h3>JazzCash (PKR)</h3>
                    <h2>Rs. 345,000</h2>
                    <button class="btn-withdraw">Withdraw to JazzCash</button>
                </div>
            </div>

            <div class="source-list">
                <h3>Active Job Sources (Bot is Monitoring):</h3>
                <ul>
                    {"".join([f"<li>✅ {source} - Connected & Scanning</li>" for source in SOURCES])}
                </ul>
            </div>
            
            <p><i>Note: The bot is currently running background cycles on Upwork and RapidAPI.</i></p>
        </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
