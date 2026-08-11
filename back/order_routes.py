from fastapi import APIRouter
order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get(path="/")
async def pedidos():
    """
    eventualmente as descrições ficam aqui
    """
    return {"message": "base route for the orders"}
