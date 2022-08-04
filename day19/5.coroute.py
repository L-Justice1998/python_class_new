# Creator:justice 廖振谊
# Creat time:2022/6/20 22:25
from greenlet import greenlet
import time

def func1():
    while True:
        print("this is func1")
        gr2.switch()
        time.sleep(0.5)

def func2():
    while True:
        print("this is func2")
        gr1.switch()
        time.sleep(0.5)

gr1=greenlet(func1)
gr2=greenlet(func2)

gr1.switch()