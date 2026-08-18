FROM python:3.14

WORKDIR /app

RUN pip install fastapi[standard] uvicorn sqlalchemy sqlalchemy-utils alembic passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart psycopg2

COPY . /app

RUN alembic revision --autogenerate -m "initial alembic run"
RUN alembic upgrade head

EXPOSE 8000

# CMD ["uvicorn", "main:app", "--reload"]
CMD ["fastapi", "run", "main.py", "--port", "80"]
