from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from reportlab.pdfgen import canvas
import os

app = FastAPI()
security = HTTPBasic()

# Admin Credentials (آپ کا خفیہ پاس ورڈ)
ADMIN_USER = "shahroze"
ADMIN_PASS = "aura2026"

# انوائسز کا ریکارڈ رکھنے کے لیے ایک سادہ لسٹ (ڈیٹا بیس کا کام کرے گی)
invoice_history = []

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != ADMIN_USER or credentials.password != ADMIN_PASS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/", response_class=HTMLResponse)
async def client_portal():
    return """
    <html>
        <head><title>Aura Client Portal</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px; background-color: #f4f7f9;">
            <div style="background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h1>🚀 Aura Engine - Client Portal</h1>
                <p>Generate your official invoice below</p>
                <form action="/generate-invoice" method="post">
                    <input type="text" name="client_name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin: 10px 0;"><br>
                    <input type="number" name="amount" placeholder="Amount ($)" required style="width: 100%; padding: 10px; margin: 10px 0;"><br>
                    <button type="submit" style="background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 100%;">Generate PDF Invoice</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/generate-invoice")
async def generate_invoice(client_name: str = Form(...), amount: int = Form(...)):
    from datetime import date
    today = date.today()
    invoice_history.append({"client": client_name, "amount": amount, "date": str(today)})
    
    file_path = f"Invoice_{client_name}.pdf"
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, "AURA ENGINE - OFFICIAL INVOICE")
    c.drawString(100, 720, f"Client: {client_name}")
    c.drawString(100, 700, f"Amount: ${amount}")
    c.drawString(100, 680, f"Date: {today}")
    c.save()
    return FileResponse(file_path, filename=file_path)

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(username: str = Depends(get_current_user)):
    rows = "".join([f"<tr><td>{i['date']}</td><td>{i['client']}</td><td>${i['amount']}</td></tr>" for i in invoice_history])
    return f"""
    <html>
        <head><title>Admin Dashboard</title></head>
        <body style="font-family: sans-serif; padding: 50px;">
            <h1>🛡️ Admin Control Panel</h1>
            <p>Welcome, {username}! Here is your business data:</p>
            <table border="1" style="width: 100%; text-align: left; border-collapse: collapse;">
                <tr style="background: #eee;"><th>Date</th><th>Client Name</th><th>Amount</th></tr>
                {rows}
            </table>
            <br>
            <a href="/">Go to Client Portal</a>
        </body>
    </html>
    """
