from celery import Celery
celery = Celery('proj',
             broker='pyamqp://guest:guest@192.168.56.10:5672/',
             backend='rpc://')
             #,include=['proj.tasks'])

#ref https://docs.celeryproject.org/en/stable/reference/celery.html#celery.Celery.send_task
r=celery.send_task('sum-of-two-numbers', (2,2))
print(r.result)