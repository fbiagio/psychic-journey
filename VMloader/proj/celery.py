#root@worker1:/vagrant/src/worker1# celery -A proj worker -l INFO
from celery import Celery
#import celeryconfig

app = Celery('proj',
            broker='pyamqp://guest:guest@192.168.56.10:5672/',
            backend='redis://192.168.56.10:6379/0',
            include=['proj.tasks']
            )



# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.config_from_object('celeryconfig')
    app.start()
