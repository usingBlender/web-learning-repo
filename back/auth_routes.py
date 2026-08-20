from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import password_handler  # pyright: ignore[reportImplicitRelativeImport, reportUnusedImport]
from models import Usuario  # pyright: ignore[reportImplicitRelativeImport]
from dependencies import pegar_sessao  # pyright: ignore[reportImplicitRelativeImport]
from schemas import UsuarioSchema, LoginSchema  # pyright: ignore[reportImplicitRelativeImport]
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from main import ALGORITHM, AT_TIMEOUT, SECRET_KEY

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(uid, time_delta:timedelta = timedelta(minutes=int(AT_TIMEOUT))):
    data_expiracao = datetime.now(timezone.utc) + time_delta  # pyright: ignore[reportArgumentType]
    dic_info = {
            "sub": uid,
            "exp": data_expiracao
            }

    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)

    return jwt_codificado

def autenticar_usuario(email, senha, session:Session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if not usuario:
        return False
    elif not password_handler.verify_password(senha, usuario.senha):
        return False
    return usuario

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

@auth_router.post("/login")
async def login(login_schema:LoginSchema, session:Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)

    if not usuario:
        raise HTTPException(status_code=400, detail="login falho, usuario ou senha errados")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, timedelta(days=7)
        
        return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer"
                }
