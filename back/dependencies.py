from models import db  # pyright: ignore[reportImplicitRelativeImport]
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()  # pyright: ignore[reportPossiblyUnboundVariable]
