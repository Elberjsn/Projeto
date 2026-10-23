from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.pedidos import router as pedidos_router
from database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield



app = FastAPI(
    title="API de Pedidos",
    description="API para criação, consulta, listagem e atualização de status de pedidos.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(pedidos_router)

@app.get("/health",tags=["Status Saude"])
def health():
    return {"status": "ok"}