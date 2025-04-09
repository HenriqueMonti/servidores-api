FROM python:3.10

WORKDIR /code

COPY requirements.txt .
COPY wait-for-db.sh .

RUN apt-get update && \
    apt-get install -y netcat-openbsd dos2unix && \
    dos2unix wait-for-db.sh && \
    chmod +x wait-for-db.sh

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./wait-for-db.sh", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
