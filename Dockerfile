FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r ./requirements.txt

RUN pip3 install -r requirements.txt