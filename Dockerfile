FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pyraken
RUN python -m pip install --upgrade setuptools pip wheel uwsgi pip-tools

COPY . .

COPY requirements.txt .
RUN pip-sync

COPY start_django.sh .
RUN chmod +x ./start_django.sh
