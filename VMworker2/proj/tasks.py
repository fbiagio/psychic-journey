from .celery import app
from celery.utils.log import get_task_logger
import time
import random

logger = get_task_logger(__name__)

# default_retry_delay - Default time in seconds before a retry of the task should be executed.
# max_retries - the maximum number of attempted retries before giving up
# time_limit - the hard time limit, in seconds, for this task
@app.task( bind=True, max_retries=3, default_retry_delay=120, time_limit=60, autoretry_for=(Exception,) )
def ping_console(self,servername):
    logger.info('try to ping servername:  %s' % (servername))
    time.sleep(random.randint(1,4))
    return True

@app.task( bind=True, max_retries=3, default_retry_delay=120, time_limit=60, autoretry_for=(Exception,) )
def change_power(self,servername):
    logger.info('try to change powerstatus of server:  %s' % (servername))
    try:
        raise "test retry"
    except Exception as exc:
        raise self.retry(exc=exc)

@app.task( bind=True, max_retries=3, default_retry_delay=10, time_limit=60, autoretry_for=(Exception,) )
def ping_from_c4ronte(self,servername):
    logger.info('try to ping from Caronte servername:  %s' % (servername))
    time.sleep(random.randint(1,4))
    return True
