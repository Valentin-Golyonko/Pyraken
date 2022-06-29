FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends --fix-missing \
    gcc \
    musl-dev \
    python3-dev python3-pip libpq-dev \
    nano gnupg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pyraken
COPY . .

RUN pip install -U pip setuptools wheel --timeout 100
COPY requirements.txt .
RUN python -V && pip -V && pip install -r requirements.txt --timeout 100

COPY . .

RUN chmod +x ./start_django.sh
