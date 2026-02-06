
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return '''
    <html>
        <head>
            <title>Aura Control Panel</title>
            <style>
                body { font-family: sans-serif; background: #0d1117; color: white; text-align: center; }
                .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; padding: 20px; }
                .card { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; cursor: pointer; }
                .card:hover { background: #1f6feb; }
                h1 { color: #58a6ff; }
            </style>
        </head>
        <body>
            <h1>Aura-335 Master Control</h1>
            <p>Developer: Shahroze | Status: Healthy</p>
            <div class="grid">
                ''' + "".join([f'<div class="card" onclick="location.href=\'/task-{i}/run\' ">Task {i}</div>' for i in range(1, 51)]) + '''
            </div>
        </body>
    </html>
    '''

# یہاں آپ کے وہ تمام 50 ٹاسکس کے روٹس پہلے کی طرح موجود رہیں گے
@app.get("/task-{id}/run")
def run_task(id: int):
    return {"status": "Executing", "task_id": id, "owner": "Shahroze"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
