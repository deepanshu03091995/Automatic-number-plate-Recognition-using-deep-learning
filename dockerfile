FROM python:3.9

RUN pip install --upgrade pip

RUN apt-get update 

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN apt-get install ffmpeg libsm6 libxext6  -y
EXPOSE 5000
CMD ["python3", "app.py"]
