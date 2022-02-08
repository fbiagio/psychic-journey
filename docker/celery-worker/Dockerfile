FROM python:3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
COPY requirements.txt ./

WORKDIR / 

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CELERY_AMQP_URL='pyamqp://guest:guest@127.0.0.1:5672/'
ENV CELERY_BACKEND_URL='redis://localhost:6379/0'

WORKDIR /
CMD [ "celery", "-A", "proj", "worker", "-l", "info" ]

# nerdctl build . -f Dockerfile -t takke/celery
# nerdctl run -it --rm takke/celery
# nerdctl rmi takke/celery
 


## TO TEST BUILD 
# nerdctl rmi takke/celery ; nerdctl build . -f Dockerfile -t takke/celery && nerdctl run -it --rm takke/celery


## TO PULL for kube
# nerdctl -n k8s.io build . -f Dockerfile -t local/takke/celery:v1.0
# nerdctl -n k8s.io run -d -exec local/takke/celery:v1.0
