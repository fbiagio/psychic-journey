FROM python:latest
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
COPY requirements.txt ./

WORKDIR / 

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CELERY_AMQP_URL='pyamqp://guest:guest@127.0.0.1:5672/'
ENV CELERY_BACKEND_URL='redis://localhost:6379/0'
ENV LOGLEVEL="info"
ENV CONCURR=1

WORKDIR /

CMD celery -A proj worker -l $LOGLEVEL --concurrency=$CONCURR


