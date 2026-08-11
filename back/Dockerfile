FROM python:3.14

WORKDIR /test

RUN pip install fastapi[standard] uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

COPY . /test

EXPOSE 8000

# CMD ["uvicorn", "main:app", "--reload"]
CMD ["fastapi", "run", "main.py", "--port", "80"]
