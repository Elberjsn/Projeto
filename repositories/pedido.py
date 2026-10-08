from sqlalchemy.orm import Session

from models.pedido import Pedido, StatusPedido


class PedidoRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, pedido: Pedido) -> Pedido:
        self.db.add(pedido)
        self.db.commit()
        self.db.refresh(pedido)
        return pedido

    def find_by_id(self, pedido_id: int) -> Pedido | None:
        return self.db.query(Pedido).filter(Pedido.id == pedido_id).first()

    def find_all(self) -> list[Pedido]:
        return self.db.query(Pedido).order_by(Pedido.id.desc()).all()

    def update_status(self, pedido: Pedido, status: StatusPedido) -> Pedido:
        pedido.status = status
        self.db.commit()
        self.db.refresh(pedido)
        return pedido
