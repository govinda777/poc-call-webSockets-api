#!/bin/bash

HOST="poccallwebsocketsapi-9ef338a96eff.herokuapp.com"

# Passo 1: Iniciar a Verificação
echo "Iniciando a verificação..."
CHECK_ID=$(curl -s -X POST "http://$HOST/start-check")
echo "Check ID obtido: $CHECK_ID"

# Passo 2: Conectar-se ao WebSocket
echo "Conectando ao WebSocket. Aguardando resultado..."
RESULT=$(timeout 30 websocat -v -1 "ws://$HOST/ws/$CHECK_ID")

# Verificar o código de saída do websocat
EXIT_CODE=$?
if [ $EXIT_CODE -eq 124 ]; then
    echo "websocat timed out after 15 seconds."
elif [ $EXIT_CODE -ne 0 ]; then
    echo "websocat encountered an error. Exit code: $EXIT_CODE"
fi

# Passo 3: Avalie os Resultados
echo "Resultado obtido: $RESULT"
if [ "$RESULT" == "approved" ]; then
    echo "Teste bem-sucedido!"
else
    echo "Teste falhou!"
fi
