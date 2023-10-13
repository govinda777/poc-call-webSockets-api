import asyncio

from fastapi import FastAPI, WebSocket, BackgroundTasks
import time
import uuid

app = FastAPI()

# Simulando um armazenamento em memória para os resultados
results = {}

@app.post("/start-check")
async def start_check(background_tasks: BackgroundTasks):
    check_id = str(uuid.uuid4())
    background_tasks.add_task(run_check, check_id)
    return check_id

async def run_check(check_id):
    # Simulando um resultado (aprovado ou reprovado)
    results[check_id] = "approved"

@app.websocket("/ws/{check_id}")
async def websocket_endpoint(websocket: WebSocket, check_id: str):
    await websocket.accept()
    await asyncio.sleep(5)
    await websocket.send_text(f"{results[check_id]}")
    await asyncio.sleep(5)



