from proj.tasks import ping_console, change_power,ping_from_c4ronte
from celery import chain
#chain = step1.si(2) | step2.si(3) | step3.si(4)
#res=chain( step.si(2,"XXXXXXXXXXXXX", 1) , link_error=log_error.s() | step.si(3,"XXXXXXXXXXXXX",2) | step.si(4,"XXXXXXXXXXXXX",3) )()
res=chain( ping_console.si("10.0.0.0") | change_power.si("XXXXXXXXXXXXXXX") | ping_from_c4ronte.si("XXXXXXXXXXXXXXX") )()
#res2=chain( ping_console.si("10.0.0.0") | change_power.si("YYYYYYYYYYYYYY") | ping_from_c4ronte.si("YYYYYYYYYYYYYY") )()
#res3=chain( ping_console.si("10.0.0.0") | change_power.si("ZZZZZZZZZZZZZZ") | ping_from_c4ronte.si("ZZZZZZZZZZZZZZ") )()
#print(res.get())
#print(res.parent.get())
#print(res.parent.parent.get())

#chain = ste.s(url) | parse_page.s() | store_page_info.s(url)
#chain()
#res = chain((add.s(i, i) for i in range(10)))
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