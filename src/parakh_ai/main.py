from fastapi import FastAPI,WebSocket,WebSocketDisconnect

app = FastAPI()

@app.get('/')
def home():
    return{
        'msg':"Hello from Parakh-AI"
    }

@app.websocket("/interview")
async def interview_start(websocket: WebSocket):
    await websocket.accept()
    print("Candidate Connected")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from candidate: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Candidate Disconnected")