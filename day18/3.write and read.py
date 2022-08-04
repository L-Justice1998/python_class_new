# Creator:justice 廖振谊
# Creat time:2022/6/19 22:20
from multiprocessing import Queue,Process
import os,time
def write(q:Queue):
    for i in ['A','B','C']:
        if not q.full():
            q.put(i)
            print("the queue put in ",i)
def read(q:Queue):
    while not q.empty():
        temp=q.get()
        print("the queue get ",temp)
if __name__ == '__main__':
    q=Queue(3)
    w=Process(target=write,args=(q,))
    r=Process(target=read,args=(q,))
    w.start()
    time.sleep(0.2)
    r.start()

