from fastapi import FastAPI, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from reportlab.pdfgen import canvas
from datetime import date

app = FastAPI()
sec = HTTPBasic()
U, P = "shahroze", "aura2026"
H = []

def get_u(c: HTTPBasicCredentials = Depends(sec)):
    if c.username != U or c.password != P:
        raise HTTPException(status_code=401)
    return c.username

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<html><body><h1>Aura</h1><form action='/g' method='post'><input name='n' placeholder='Name'><br><input name='a' placeholder='Amount'><br><button>GO</button></form></body></html>"

@app.post("/g")
async def g(n: str = Form(...), a: int = Form(...)):
    H.append({"n": n, "a": a, "d": str(date.today())})
    f = f"I_{n}.pdf"
    c = canvas.Canvas(f)
    c.drawString(100, 700, f"Invoice: {n} - ${a}")
    c.save()
    return FileResponse(f, filename=f)

@app.get("/admin", response_class=HTMLResponse)
async def admin(u: str = Depends(get_u)):
    rows = "".join([f"<tr><td>{i['d']}</td><td>{i['n']}</td><td>${i['a']}</td></tr>" for i in H])
    return f"<html><body><h1>Admin</h1><table border='1'><tr><th>Date</th><th>Name</th><th>$</th></tr>{rows}</table></body></html>"
