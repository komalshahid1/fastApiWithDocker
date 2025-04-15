# socket_service/app/main.py
from fastapi import FastAPI, WebSocket , Request
from fastapi.responses import HTMLResponse
import os
import traceback
from app.broadcast import connected_clients 

app = FastAPI()
connections = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
async def get():
    with open(os.path.join(BASE_DIR, "templates/index.html")) as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)  # ✅ Add to list
    print("🟢 Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You said: {data}")
    except Exception as e:
        print("🔴 Client disconnected", e)
    finally:
        connected_clients.remove(websocket)



@app.post("/notify")
async def notify(request: Request):
    try:
        data = await request.json()
        print("📥 Received notify data:", data)

        from app.broadcast import broadcast_message
        await broadcast_message(data.get("message", ""))
        print("✅ Notification broadcasted")
        return {"status": "notified"}

    except Exception as e:
        print("❌ Error in /notify:", repr(e))
        traceback.print_exc()  # ✅ Full traceback
        return {"error": str(e)}

