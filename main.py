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
    return {"check_id": check_id}

async def run_check(check_id):
    # Simulando um processo demorado
    await asyncio.sleep(1)
    # Simulando um resultado (aprovado ou reprovado)
    results[check_id] = "approved"

@app.websocket("/ws/{check_id}")
async def websocket_endpoint(websocket: WebSocket, check_id: str):
    await websocket.accept()
    print(f"WebSocket connection accepted for check_id: {check_id}")
    for _ in range(10):  # Espera até 10 segundos
        if check_id in results:
            await websocket.send_text(results[check_id])
            print(f"Sent result for check_id: {check_id}")
            await asyncio.sleep(2)  # Mantém a conexão aberta por 2 segundos após enviar o resultado
            return
        await asyncio.sleep(1)
    print(f"No result found for check_id: {check_id} after waiting")


