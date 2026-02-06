
import os
import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, StreamingResponse
import io
import csv
from fpdf import FPDF

app = FastAPI()

data_vault = {
    "UK": [{"Business": "London Tech", "Email": "info@londontech.co.uk", "Status": "Verified"}],
    "UAE": [{"Business": "Dubai Digital", "Email": "sales@dubaidigital.ae", "Status": "Verified"}]
}

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Aura Engine v17.0: System Online 24/7</h1><form action='/dash' method='post'><input name='u'><button>Login</button></form>"

@app.post("/dash", response_class=HTMLResponse)
async def dash(u: str = Form(...)):
    return f"<h2>Welcome {u}</h2><p>Balance: $450.00</p><a href='/export-pdf'>Download PDF Report</a>"

@app.get("/export-pdf")
async def pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Aura Global Report", ln=True, align='C')
    res = io.BytesIO(pdf.output(dest='S').encode('latin-1'))
    return StreamingResponse(res, media_type="application/pdf")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
