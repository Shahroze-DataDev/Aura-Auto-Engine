from fastapi import FastAPI, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from reportlab.pdfgen import canvas
import os

app = FastAPI()

# ڈیٹا اسٹور کرنے کے لیے لسٹ (سرور ری اسٹارٹ ہونے تک ڈیٹا رہے گا)
H = []

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 50px; background: #eef2f3; }
                .box { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
                input { margin: 10px; padding: 10px; width: 80%; border: 1px solid #ddd; border-radius: 5px; }
                button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="box">
                <h2>🚀 Aura Auto Engine</h2>
                <form action="/generate" method="post">
                    <input type="text" name="n" placeholder="نام درج کریں" required><br>
                    <input type="text" name="a" placeholder="رقم یا تفصیل" required><br>
                    <button type="submit">انوائس بنائیں</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/generate")
async def generate(n: str = Form(...), a: str = Form(...)):
    import datetime
    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    H.append((d, n, a))
    
    path = "invoice.pdf"
    c = canvas.Canvas(path)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Aura Engine - Official Invoice")
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Date: {d}")
    c.drawString(100, 700, f"Customer Name: {n}")
    c.drawString(100, 680, f"Amount/Details: {a}")
    c.save()
    return FileResponse(path, filename=f"{n}_invoice.pdf")

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel():
    style = """
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background: #f0f2f5; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2 { color: #1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom: 10px; }
        #searchInput { width: 100%; padding: 12px; margin: 20px 0; border: 1px solid #ddd; border-radius: 25px; outline: none; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #1a73e8; color: white; border-radius: 4px 4px 0 0; }
        tr:hover { background-color: #f8f9fa; }
    </style>
    """
    
    script = """
    <script>
    function searchTable() {
        let input = document.getElementById("searchInput").value.toUpperCase();
        let rows = document.getElementById("adminTable").getElementsByTagName("tr");
        for (let i = 1; i < rows.length; i++) {
            let text = rows[i].textContent || rows[i].innerText;
            rows[i].style.display = text.toUpperCase().includes(input) ? "" : "none";
        }
    }
    </script>
    """
    
    table_rows = "".join([f"<tr><td>{d}</td><td>{n}</td><td>{a}</td></tr>" for d, n, a in H])
    
    content = f"""
    <html>
        <head><title>Aura Admin</title>{style}{script}</head>
        <body>
            <div class="container">
                <h2>🛡️ Aura Advanced Admin Panel</h2>
                <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="کسی بھی ریکارڈ کو تلاش کریں (نام، تاریخ، رقم)...">
                <table id="adminTable">
                    <tr><th>ٹائم اسٹیمپ</th><th>نام</th><th>ڈیٹا</th></tr>
                    {table_rows}
                </table>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=content)
from fastapi import FastAPI, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from reportlab.pdfgen import canvas
import os

app = FastAPI()

# ڈیٹا اسٹور کرنے کے لیے لسٹ (سرور ری اسٹارٹ ہونے تک ڈیٹا رہے گا)
H = []

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 50px; background: #eef2f3; }
                .box { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
                input { margin: 10px; padding: 10px; width: 80%; border: 1px solid #ddd; border-radius: 5px; }
                button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="box">
                <h2>🚀 Aura Auto Engine</h2>
                <form action="/generate" method="post">
                    <input type="text" name="n" placeholder="نام درج کریں" required><br>
                    <input type="text" name="a" placeholder="رقم یا تفصیل" required><br>
                    <button type="submit">انوائس بنائیں</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/generate")
async def generate(n: str = Form(...), a: str = Form(...)):
    import datetime
    d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    H.append((d, n, a))
    
    path = "invoice.pdf"
    c = canvas.Canvas(path)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Aura Engine - Official Invoice")
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Date: {d}")
    c.drawString(100, 700, f"Customer Name: {n}")
    c.drawString(100, 680, f"Amount/Details: {a}")
    c.save()
    return FileResponse(path, filename=f"{n}_invoice.pdf")

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel():
    style = """
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background: #f0f2f5; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2 { color: #1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom: 10px; }
        #searchInput { width: 100%; padding: 12px; margin: 20px 0; border: 1px solid #ddd; border-radius: 25px; outline: none; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #1a73e8; color: white; border-radius: 4px 4px 0 0; }
        tr:hover { background-color: #f8f9fa; }
    </style>
    """
    
    script = """
    <script>
    function searchTable() {
        let input = document.getElementById("searchInput").value.toUpperCase();
        let rows = document.getElementById("adminTable").getElementsByTagName("tr");
        for (let i = 1; i < rows.length; i++) {
            let text = rows[i].textContent || rows[i].innerText;
            rows[i].style.display = text.toUpperCase().includes(input) ? "" : "none";
        }
    }
    </script>
    """
    
    table_rows = "".join([f"<tr><td>{d}</td><td>{n}</td><td>{a}</td></tr>" for d, n, a in H])
    
    content = f"""
    <html>
        <head><title>Aura Admin</title>{style}{script}</head>
        <body>
            <div class="container">
                <h2>🛡️ Aura Advanced Admin Panel</h2>
                <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="کسی بھی ریکارڈ کو تلاش کریں (نام، تاریخ، رقم)...">
                <table id="adminTable">
                    <tr><th>ٹائم اسٹیمپ</th><th>نام</th><th>ڈیٹا</th></tr>
                    {table_rows}
                </table>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=content)
