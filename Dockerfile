FROM python:3.11-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
EXPOSE 8000

RUN apk add postgresql-client

RUN pip3 install -r requirements.txt