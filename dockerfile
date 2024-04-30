FROM python:3.9-slim-buster

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt



CMD ["python3", "app.py"]
