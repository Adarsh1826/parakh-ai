from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import os
from starlette.concurrency import run_in_threadpool
from parakh_ai.agent.agent import parakh
from dotenv import load_dotenv
from parakh_ai.utils.tts import text_to_speech
import base64
import json

load_dotenv()

app = FastAPI()

SYSTEM_PROMPT = """
You are ParakhAI, a professional technical interviewer.

Ask one question at a time.
Analyze the candidate's previous answer.
Ask relevant follow-up questions.
Evaluate the candidate's technical knowledge.
Keep the interview natural and concise.
"""


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return str(content)


async def send_audio(websocket: WebSocket, text: str):
    """Generate speech and send it as base64 JSON over the websocket."""
    audio_bytes = await run_in_threadpool(lambda: text_to_speech(text).read())
    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
    await websocket.send_text(json.dumps({
        "type": "audio",
        "data": audio_b64,
        "format": "mp3"
    }))


@app.get('/')
def home():
    return {'msg': "Hello from Parakh-AI"}


@app.websocket("/interview")
async def interview_start(websocket: WebSocket):
    await websocket.accept()
    print("Candidate Connected")

    messages = [{"role": "user", "content": "Begin the interview."}]

    try:
        # opening question
        response = await run_in_threadpool(parakh.invoke, {"messages": messages})
        messages = response["messages"]
        question_text = extract_text(messages[-1].content)
        print(f"Agent: {question_text}")

        await send_audio(websocket, question_text)

        while True:
            candidate_text = await websocket.receive_text()
            print(f"Candidate: {candidate_text}")

            messages.append({"role": "user", "content": candidate_text})

            response = await run_in_threadpool(parakh.invoke, {"messages": messages})
            messages = response["messages"]
            next_question = extract_text(messages[-1].content)
            print(f"Agent: {next_question}")

            await send_audio(websocket, next_question)

    except WebSocketDisconnect:
        print("Candidate Disconnected")