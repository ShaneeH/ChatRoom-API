from fastapi import FastAPI, WebSocket
from models.user import User
import time

app = FastAPI()

start_time = time.time()
chatrooms = ['Europe' , 'USA']

@app.get("/test")
def home():
    uptime_seconds = int(time.time() - start_time)
    return {
        "status": "online",
        "uptime_minutes": uptime_seconds / 60,
        "chatrooms_available": len(chatrooms)
    }

@app.post("/user")
def create_user(body: User):
    return {"msg": "Received user", "data": body}

@app.get("/rooms")
def get_rooms():
    return {"chatrooms": chatrooms}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Connected")
    while True:
        msg = await ws.receive_text()
        await ws.send_text(f"Echo: {msg}")
        print(f"msg Success: {msg}")
