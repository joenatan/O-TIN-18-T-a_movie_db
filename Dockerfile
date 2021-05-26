FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update && apt install gcc python3-mysqldb default-libmysqlclient-dev -y

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system