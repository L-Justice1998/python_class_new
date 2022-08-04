# Creator:justice 廖振谊
# Creat time:2022/6/19 23:21
import time
from threading import Thread
def say_hello(i):
    print(i)
    time.sleep(1)

if __name__ == '__main__':
    for i in range(10):
        say_hello(i)
    for i in range(10):
        t=Thread(target=say_hello,args=(i,))
        t.start()
    t.join()

