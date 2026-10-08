from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field, StringConstraints
from typing import Annotated

from models.pedido import StatusPedido

TextoObrigatorio = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=150)]


class PedidoCreate(BaseModel):
    cliente: TextoObrigatorio
    produto: TextoObrigatorio
    quantidade: int = Field(gt=0)
    valor_unitario: Decimal = Field(gt=0, max_digits=12, decimal_places=2)


class PedidoStatusUpdate(BaseModel):
    status: StatusPedido


class PedidoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cliente: str
    produto: str
    quantidade: int
    valor_unitario: Decimal
    valor_total: Decimal
    status: StatusPedido
    data_criacao: datetime
