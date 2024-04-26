FROM python:3.9-alpine

RUN pip install --upgrade pip

RUN apt update && apt upgrade -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN apt install ffmpeg libsm6 libxext6  -y

CMD ["python3", "app.py"]
