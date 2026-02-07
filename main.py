import os
import threading
import pandas as pd
import datetime
import nest_asyncio
import uvicorn
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse

nest_asyncio.apply()

app = FastAPI()

GEMINI_KEY = os.getenv("GEMINI_KEY")
genai.configure(api_key=GEMINI_KEY)

def aura_web_scraper(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_data = soup.get_text()[:2000]
        return text_data
    except:
        return "Error fetching data"

def aura_financial_admin(client, amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AURA ENGINE - OFFICIAL INVOICE", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Client: {client}", ln=2, align='L')
    pdf.cell(200, 10, txt=f"Amount: ${amount}", ln=3, align='L')
    pdf.cell(200, 10, txt=f"Date: {datetime.date.today()}", ln=4, align='L')
    path = f"Invoice_{client}.pdf"
    pdf.output(path)
    return path

@app.get("/", response_class=HTMLResponse)
async def admin_dashboard():
    return """
    <html>
        <head>
            <title>Aura Engine Cloud</title>
            <style>
                body { font-family: sans-serif; background: #f0f2f5; padding: 20px; text-align: center; }
                .card { background: white; padding: 20px; border-radius: 10px; max-width: 500px; margin: auto; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
                input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; }
                button { width: 90%; padding: 10px; background: #1a73e8; color: white; border: none; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Aura Engine Live</h1>
                <p>300+ Automation Skills Active</p>
                <form action="/generate-invoice" method="post">
                    <input name="client" placeholder="Client Name" required>
                    <input name="amount" placeholder="Amount ($)" required>
                    <button type="submit">Generate PDF Invoice</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/generate-invoice")
async def handle_invoice(client: str = Form(...), amount: str = Form(...)):
    file_path = aura_financial_admin(client, amount)
    return FileResponse(file_path, filename=file_path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
