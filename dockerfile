FROM python:3.9.13-slim-buster

WORKDIR /yoloV5-snap-go

COPY ./requirements.txt .

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ .

CMD [ "python", "main.py" ]

EXPOSE 8000