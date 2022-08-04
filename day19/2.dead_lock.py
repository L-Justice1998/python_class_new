# Creator:justice 廖振谊
# Creat time:2022/6/20 20:36
from threading import Thread,Lock
import time
def func1(mutexA:Lock,mutexB:Lock):
    mutexA.acquire()
    print("A lock locks")
    time.sleep(1)
    mutexB.acquire()
    print("B lock locks")
    time.sleep(1)
    mutexA.release()
    print("A lock releases")
    time.sleep(1)
    mutexB.release()
    print("B lock releases")
    time.sleep(1)


def func2(mutexA:Lock,mutexB:Lock):
    mutexB.acquire()
    print("B lock locks")
    time.sleep(1)
    mutexA.acquire()
    print("A lock locks")
    time.sleep(1)
    mutexA.release()
    print("A lock releases")
    time.sleep(1)
    mutexB.release()
    print("B lock releases")
    time.sleep(1)




if __name__ == '__main__':
    mutexA=Lock()
    mutexB=Lock()
    t1=Thread(target=func1,args=(mutexA,mutexB))
    t2 = Thread(target=func2, args=(mutexA, mutexB))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("threads end")