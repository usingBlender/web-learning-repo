from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from back.models import Usuario
from back.dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Rota padrão do sistema de autenticação.
    """

    return {"mensagem": "Rota padrão do sistema de autenticação.", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha:str, nome:str, session:Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()

    if usuario:
        # ja existe um usuário com esse email
        return {"mensagem": "ja existe um usuario com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuario cadastrado com sucesso"}
