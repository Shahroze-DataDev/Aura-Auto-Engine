
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI(title="Shahroze Fiverr Portfolio")

@app.get("/", response_class=HTMLResponse)
def portfolio():
    return '''
    <html>
        <head>
            <title>Shahroze | Python & Automation Expert</title>
            <style>
                body { background: #0a0a0a; color: #1dbf73; font-family: 'Helvetica', sans-serif; padding: 40px; }
                .gig-card { border: 2px solid #1dbf73; padding: 20px; border-radius: 15px; background: #1a1a1a; max-width: 700px; margin: auto; }
                .feature { color: white; margin: 10px 0; font-size: 18px; }
                .highlight { color: #58a6ff; font-weight: bold; }
                .btn-fiverr { background: #1dbf73; color: white; padding: 15px 30px; border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="gig-card">
                <h1>Professional Automation Services</h1>
                <p class="feature">✅ <b>Web Scraping:</b> Extracting data from any public site.</p>
                <p class="feature">✅ <b>Custom Bots:</b> Building self-running Python engines.</p>
                <p class="feature">✅ <b>API Integration:</b> Connecting systems via FastAPI.</p>
                <hr style="border: 0.5px solid #333;">
                <p class="feature">Current Status: <span class="highlight">Aura Engine v10.0 is Live & Monitoring</span></p>
                <a href="#" class="btn-fiverr">Contact Me on Fiverr</a>
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
