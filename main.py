import asyncio
from fastapi import FastAPI, WebSocket, BackgroundTasks
import uuid
from starlette.websockets import WebSocketState

app = FastAPI()


@app.post("/start-check")
async def start_check(background_tasks: BackgroundTasks):
    check_id = str(uuid.uuid4())
    background_tasks.add_task(run_check, check_id)
    return check_id


async def run_check(check_id):
    # Simulando um resultado (aprovado ou reprovado)
    # Como não estamos mais usando o dicionário 'results', esta função não faz nada útil.
    # Mantive apenas para manter a estrutura original.
    pass


@app.websocket("/ws/{check_id}")
async def websocket_endpoint(websocket: WebSocket, check_id: str):
    await websocket.accept()
    await asyncio.sleep(5)

    # Verificar se a conexão WebSocket ainda está aberta antes de enviar a mensagem
    if websocket.client_state == WebSocketState.CONNECTED:
        try:
            await websocket.send_text("approved")
        except Exception as e:
            # Handle the error, e.g., log it.
            print(f"Error sending message: {e}")
