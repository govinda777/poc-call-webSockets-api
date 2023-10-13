# poc-call-webSockets-api

## Security Check via WebSockets

Este projeto implementa uma verificação de segurança que é acionada por uma pipeline do GitHub. A verificação é realizada por uma API FastAPI e o resultado é comunicado de volta à pipeline via WebSockets.

## Estrutura do Projeto

```
.
├── .github
│   └── workflows
│       └── main.yml       # GitHub Actions pipeline
└── README.md
```

## Como Funciona

1. Um commit é feito no GitHub.
2. A pipeline do GitHub Actions é acionada.
3. A pipeline envia uma requisição para a API FastAPI solicitando uma verificação de segurança.
4. A API inicia a verificação em segundo plano e envia um identificador único de volta à pipeline.
5. A pipeline abre uma conexão WebSocket usando o identificador único.
6. Após a conclusão da verificação, a API envia o resultado através da conexão WebSocket.
7. A pipeline processa o resultado e toma a ação apropriada (por exemplo, falhar se a verificação não for aprovada).

## Configuração e Uso

### Pré-requisitos

- Uma conta no GitHub com acesso para criar e modificar pipelines

### Configuração

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Configure a pipeline no GitHub usando o arquivo `.github/workflows/main.yml`.

### Uso

1. Faça um commit e push para o repositório.
2. A pipeline do GitHub Actions será acionada automaticamente.
3. Acompanhe o progresso da pipeline no GitHub para ver os resultados da verificação de segurança.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
