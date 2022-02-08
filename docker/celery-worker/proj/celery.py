#root@worker1:/vagrant/src/worker1# celery -A proj worker -l INFO
import os
from celery import Celery
#import celeryconfig


app = Celery('proj',
            broker=str(os.environ["CELERY_AMQP_URL"]),
            backend=str(os.environ["CELERY_BACKEND_URL"]),
            include=['proj.tasks']
            )



# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.config_from_object('celeryconfig')
    app.start()
