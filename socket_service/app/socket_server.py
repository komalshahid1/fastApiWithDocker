# socket_service/app/main.py
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
async def get():
    with open(os.path.join(BASE_DIR, "templates/index.html")) as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You said: {data}")

