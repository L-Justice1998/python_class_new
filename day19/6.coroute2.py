# Creator:justice 廖振谊
# Creat time:2022/6/20 22:43
from gevent import monkey
monkey.patch_all()
import gevent
import time

def func(n,k):
    for i in range(n):
        print(gevent.getcurrent(),i,k)
        gevent.sleep(0.5)

g=gevent.spawn(func,5,1)
f=gevent.spawn(func,5,2)
l=gevent.spawn(func,5,3)
g.join()
f.join()
l.join()