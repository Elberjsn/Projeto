# API de Pedidos - Projeto

Esse projeto de API REST usa FastAPI, PostgreSQL e Docker Compose.

## Requisitos

- Docker e Docker Compose
- Porta `8000` disponível
`
### Exemplo de variaveis de ambiente .env

```bash
POSTGRES_DB=pedidos
POSTGRES_USER=pedidos
POSTGRES_PASSWORD=
```

## Executar

1. Copie `.env` para `.env`.
2. Altere `POSTGRES_PASSWORD` para uma senha local.
3. Inicie os serviços:

   ```bash
   docker compose up --build
   ```

A API ficará disponível em `http://localhost:8000`

## Endpoints

| Método | Caminho | Descrição |
|---|---|---|
| `GET` | `/health` | Status da API |
| `POST` | `/pedidos` | Criar pedido |
| `GET` | `/pedidos` | Listar todos os pedidos |
| `GET` | `/pedidos/{id}` | Consultar pedido |
| `PATCH` | `/pedidos/{id}/status` | Alterar status |

### Criar pedido

`POST /pedidos`

```json
{
  "cliente": "Maria",
  "produto": "Teclado",
  "quantidade": 2,
  "valor_unitario": "89.90"
}
```

A API calcula `valor_total` a resposta se tudo der certo `201 Created`.

### Alterar status

`PATCH /pedidos/1/status`

```json
{
  "status": "CONFIRMADO"
}
```

Status aceitos: `CRIADO`, `CONFIRMADO`, `EM_ANDAMENTO` e `CANCELADO`

## Testar persistência

1. Crie um pedido e guarde o `id` retornado.
2. Consulte `GET /pedidos/{id}`.
3. Reinicie somente a API: `docker compose restart pedidos`.
4. Consulte novamente o pedido. 
5. Ele deve  existir porque os dados ficam no PostgreSQL.

## Comandos uteis

```bash
docker compose logs -f pedidos
docker compose ps
docker compose down
```

`docker compose down` mantem os dados do banco. Para apagar os dados, use `docker compose down -v`.

## Estrutura em camadas

- `api/`: endpoints HTTP.
- `database/`: validação e formato de entrada/saída.
- `services/`: regras de negócio e cálculo do total.
- `repositories/`: consultas e persistência.
- `models/`: mapeamento das tabelas SQL.
- `config/`: configurações, conexão e sessões com PostgreSQL.
