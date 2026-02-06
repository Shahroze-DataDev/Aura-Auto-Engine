
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
import uvicorn
import os
import random

app = FastAPI(title="Aura Finance & Billing")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return '''
    <html>
        <head>
            <title>Shahroze Finance Portal</title>
            <style>
                body { font-family: sans-serif; background: #0d1117; color: white; padding: 20px; text-align: center; }
                .box { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin: 10px auto; max-width: 500px; }
                .btn { background: #238636; color: white; border: none; padding: 12px 25px; border-radius: 5px; cursor: pointer; font-size: 16px; text-decoration: none; display: inline-block; }
                input { padding: 10px; border-radius: 5px; border: 1px solid #30363d; background: #0d1117; color: white; margin-bottom: 10px; width: 80%; }
                h1 { color: #58a6ff; }
            </style>
        </head>
        <body>
            <h1>Aura Billing System</h1>
            <div class="box">
                <h3>Generate Client Invoice</h3>
                <input type="text" id="client" placeholder="Client Name">
                <input type="number" id="amount" placeholder="Amount ($)">
                <br>
                <button class="btn" onclick="generate()">Download PDF Invoice</button>
            </div>
            
            <script>
                function generate() {
                    const c = document.getElementById('client').value || 'Global-Client';
                    const a = document.getElementById('amount').value || '0';
                    window.location.href = `/generate-invoice?client=${c}&amount=${a}`;
                }
            </script>
        </body>
    </html>
    '''

@app.get("/generate-invoice")
def make_invoice(client: str, amount: int):
    # یہ فنکشن ایک سادہ ٹیکسٹ فائل بنائے گا جسے کلائنٹ رسید کے طور پر دیکھ سکتا ہے
    invoice_content = f"--- AURA ENGINE INVOICE ---\nID: INV-{random.randint(1000, 9999)}\nClient: {client}\nAmount: ${amount}\nStatus: Pending Payment\nDeveloper: Shahroze Data Dev\nDate: {random.randint(1, 30)}-02-2026"
    return Response(content=invoice_content, media_type="text/plain", headers={"Content-Disposition": f"attachment; filename=invoice_{client}.txt"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
