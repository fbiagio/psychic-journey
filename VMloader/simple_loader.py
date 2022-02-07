from proj.tasks import add


#r=add.apply_async(args=[1, 2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
r=add.delay(4, 4).get()
print(r)


#from celery import Celery
#
#app = Celery('proj',
#             broker='pyamqp://guest:guest@192.168.56.10:5672/',
#             backend='rpc://',
#             )
#
#@app.task
#def add(x, y):
#    return x + y
#
#if __name__ == '__main__':
#    app.start()
#    task.add(1,2)
