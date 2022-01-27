from celery import Celery
#import celeryconfig

app = Celery('proj',
             broker='pyamqp://guest:guest@192.168.56.10:5672/',
             backend='rpc://',
             include=['proj.tasks'])


task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})

app.task.add.apply_async(args=[1, 2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})



#tasks.apply_async(args=[1, 2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})

 #send_task(name, args=None, kwargs=None, countdown=None, eta=None, task_id=None, producer=None, connection=None, router=None, result_cls=None, expires=None, publisher=None, link=None, link_error=None, add_to_parent=True, group_id=None, group_index=None, retries=0, chord=None, reply_to=None, time_limit=None, soft_time_limit=None, root_id=None, parent_id=None, route_name=None, shadow=None, chain=None, task_type=None, **options)[source]


#chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
#chain()

#
#for i in range(1,20):
#    print(i)
#    xdiv.
#
#
#
#res=chain(
#    add.s(4, 4) | mul.s(8)
#    )().get()
#print(res)