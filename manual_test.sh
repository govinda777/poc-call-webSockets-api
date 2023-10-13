#!/bin/bash

# Passo 1: Iniciar a Verificação
echo "Iniciando a verificação..."
CHECK_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/start-check")
CHECK_ID=$(echo $CHECK_RESPONSE | jq -r '.check_id')
echo "Check ID obtido: $CHECK_ID"

# Passo 2: Conectar-se ao WebSocket
echo "Conectando ao WebSocket. Aguardando resultado..."
RESULT=$(websocat -1 "ws://127.0.0.1:8000/ws/$CHECK_ID")

# Passo 3: Avalie os Resultados
echo "Resultado obtido: $RESULT"
if [ "$RESULT" == "approved" ]; then
    echo "Teste bem-sucedido!"
else
    echo "Teste falhou!"
fi
