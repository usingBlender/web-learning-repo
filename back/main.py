from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")

app = FastAPI()

from auth_routes import auth_router  # pyright: ignore[reportImplicitRelativeImport]
from order_routes import order_router  # pyright: ignore[reportImplicitRelativeImport]

app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
