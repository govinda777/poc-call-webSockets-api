from fastapi.testclient import TestClient
import pytest
from main import app  # Altere 'your_module_name' para o nome do seu módulo

client = TestClient(app)

def test_start_check():
    response = client.post("/start-check")
    assert response.status_code == 200
    check_id = response.json()
    assert isinstance(check_id, str)

def test_websocket_endpoint():
    # Gerar um check_id para o teste
    check_id = client.post("/start-check").json()

    # Conectar via WebSocket
    with client.websocket_connect(f"/ws/{check_id}") as websocket:
        # A mensagem esperada é "approved"
        assert websocket.receive_text() == "approved"

