from fastapi import FastAPI, WebSocket
from models.user import User

app = FastAPI()

@app.get("/test")
def home():
    return {"API is Online"}

