FROM python:3

ENV PYTHONUNBUFFERED 1

RUN pip install psycopg2-binary
RUN pip install psycopg2

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
