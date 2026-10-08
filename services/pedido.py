from decimal import Decimal, ROUND_HALF_UP

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.pedido import Pedido, StatusPedido
from repositories.pedido import PedidoRepository
from database.pedidos import PedidoCreate


class PedidoService:
    def __init__(self, db: Session):
        self.repository = PedidoRepository(db)

    def criar(self, dados: PedidoCreate) -> Pedido:
        total = (dados.valor_unitario * dados.quantidade).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        pedido = Pedido(
            cliente=dados.cliente,
            produto=dados.produto,
            quantidade=dados.quantidade,
            valor_unitario=dados.valor_unitario,
            valor_total=total,
            status=StatusPedido.CRIADO,
        )
        return self.repository.save(pedido)

    def buscar_por_id(self, pedido_id: int) -> Pedido:
        pedido = self.repository.find_by_id(pedido_id)
        if pedido is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Pedido {pedido_id} não encontrado",
            )
        return pedido

    def listar(self) -> list[Pedido]:
        return self.repository.find_all()

    def atualizar_status(self, pedido_id: int, novo_status: StatusPedido) -> Pedido:
        pedido = self.buscar_por_id(pedido_id)
        if pedido.status == StatusPedido.CANCELADO and novo_status != StatusPedido.CANCELADO:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Não é permitido alterar o status de um pedido cancelado",
            )
        return self.repository.update_status(pedido, novo_status)
