from fastapi import FastAPI

app = FastAPI(
    title="API de Pedidos",
    description="API para criação, consulta, listagem e atualização de status de pedidos.",
    version="1.0.0",
)

@app.get("/health",tags=["Status Saude"])
def health():
    return {"status": "ok"}