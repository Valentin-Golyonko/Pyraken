FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    python3-dev \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pyraken
RUN python -m pip install --upgrade setuptools pip wheel \
    && pip install uwsgi \
    && pip install -U git+git://github.com/chibisov/drf-extensions.git@8001a440c7322be26bbe2d16f3a334a8b0b5860b
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

