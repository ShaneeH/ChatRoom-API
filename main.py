from fastapi import FastAPI, WebSocket
from models.user import User

app = FastAPI()

chatrooms = ["Sport", "Movies", "TV"]

@app.get("/test")
def home():
    return {"API is Online"}

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
