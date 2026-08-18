from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import password_handler  # pyright: ignore[reportImplicitRelativeImport, reportUnusedImport]
from models import Usuario  # pyright: ignore[reportImplicitRelativeImport]
from dependencies import pegar_sessao  # pyright: ignore[reportImplicitRelativeImport]
from schemas import UsuarioSchema  # pyright: ignore[reportImplicitRelativeImport]

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Rota padrão do sistema de autenticação.
    """

    return {"mensagem": "Rota padrão do sistema de autenticação.", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuarioSchema:UsuarioSchema, session:Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == usuarioSchema.email).first()  # pyright: ignore[reportGeneralTypeIssues]

    if usuario:
        # ja existe um usuário com esse email
        raise HTTPException(status_code=400, detail="ja existe um usuario com esse email")
    else:
        senha_criptografada = password_handler.hash_password(usuarioSchema.senha)
        novo_usuario = Usuario(usuarioSchema.nome, usuarioSchema.email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuario cadastrado com sucesso"}
