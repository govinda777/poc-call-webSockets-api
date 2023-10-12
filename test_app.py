from fastapi.testclient import TestClient
import pytest
from main import app, run_check, results  # Importe as funções e variáveis necessárias
import time

client = TestClient(app)

def test_start_check():
    response = client.post("/start-check")
    assert response.status_code == 200
    data = response.json()
    assert "check_id" in data
    check_id = data["check_id"]
    assert isinstance(check_id, str)

    # Mock the run_check function to make it faster
    results[check_id] = "approved"

    # Test the WebSocket with the provided check_id
    with client.websocket_connect(f"/ws/{check_id}") as websocket:
        assert websocket.receive_text() == "approved"

# Se você ainda quiser testar o WebSocket isoladamente:
def test_websocket_endpoint():
    # Mock a result
    mock_check_id = "mocked-check-id"
    results[mock_check_id] = "approved"

    with client.websocket_connect(f"/ws/{mock_check_id}") as websocket:
        assert websocket.receive_text() == "approved"
