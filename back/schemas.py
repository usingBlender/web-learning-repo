from multiprocessing import BoundedSemaphore

from pydantic import BaseModel
# from typing import Optional # -> use '| NONE' instead

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: bool | None
    admin: bool | None

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    usuario:int
