from fastapi import APIRouter, Depends, HTTPException

order_router = APIRouter(prefix="/orders", tags=["orders"])

from sqlalchemy.orm import Session
import password_handler  # pyright: ignore[reportImplicitRelativeImport, reportUnusedImport]
from models import Pedido  # pyright: ignore[reportImplicitRelativeImport]
from dependencies import pegar_sessao  # pyright: ignore[reportImplicitRelativeImport]
from schemas import PedidoSchema  # pyright: ignore[reportImplicitRelativeImport]

@order_router.get(path="/")
async def pedidos():
    """
    eventualmente as descrições ficam aqui
    """
    return {"message": "base route for the orders"}

@order_router.post(path="/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}
