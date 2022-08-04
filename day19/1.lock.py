# Creator:justice 廖振谊
# Creat time:2022/6/20 20:27
from threading import Thread,Lock
import time
num=0
def plus1(mutex:Lock):
    global num
    mutex.acquire()
    for i in range(1000000):
        num+=1
    mutex.release()

def plus2(mutex):
    global num
    mutex.acquire()
    for i in range(1000000):
        num += 1
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    t1=Thread(target=plus1,args=(mutex,))
    t2=Thread(target=plus2,args=(mutex,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)


