from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from config import get_db
from database.pedidos import PedidoCreate, PedidoResponse, PedidoStatusUpdate
from services.pedido import PedidoService

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def criar_pedido(dados: PedidoCreate, db: Session = Depends(get_db)):

    return PedidoService(db).criar(dados)


@router.get("", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):

    return PedidoService(db).listar()


@router.get("/{pedido_id}", response_model=PedidoResponse)
def consultar_pedido(pedido_id: int, db: Session = Depends(get_db)):

    return PedidoService(db).buscar_por_id(pedido_id)


@router.patch("/{pedido_id}/status", response_model=PedidoResponse)
def atualizar_status(pedido_id: int, dados: PedidoStatusUpdate, db: Session = Depends(get_db)):

    return PedidoService(db).atualizar_status(pedido_id, dados.status)






