# Creator:justice 廖振谊
# Creat time:2022/6/19 22:59
from multiprocessing import Pool,Manager
import os,time
def write(q):
    print("write pid",os.getpid())
    for i in ['A','B','C']:
        if not q.full():
            q.put(i)
            print("the queue put in ",i)
    time.sleep(2)
def read(q):
    print("read pid",os.getpid())
    while not q.empty():
        temp=q.get()
        print("the queue get ",temp)

if __name__ == '__main__':
    print("father pid",os.getpid())
    q=Manager().Queue(3)
    po=Pool()
    po.apply_async(write,args=(q,))
    po.apply_async(read,args=(q,))
    po.close()
    po.join()
