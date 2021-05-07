FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app