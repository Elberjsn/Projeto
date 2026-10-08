import enum
from sqlalchemy import Column, DateTime, Enum, Integer, Numeric, String, func

from config.banco import Base

class StatusPedido(str, enum.Enum):
    CRIADO = "CRIADO"
    CONFIRMADO = "CONFIRMADO"
    CANCELADO = "CANCELADO"
    EM_ANDAMENTO = "EM ANDAMENTO"


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String(150), nullable=False)
    produto = Column(String(150), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Numeric(12, 2), nullable=False)
    valor_total = Column(Numeric(14, 2), nullable=False)
    status = Column(Enum(StatusPedido, name="status_pedido"), nullable=False,
                    default=StatusPedido.CRIADO)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
