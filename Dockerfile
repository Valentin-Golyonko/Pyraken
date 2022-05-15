FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pyraken
COPY . .

RUN python -m pip install --upgrade pip setuptools wheel pip-tools
RUN pip-sync && pip install -r requirements.txt

RUN chmod +x ./start_django.sh
