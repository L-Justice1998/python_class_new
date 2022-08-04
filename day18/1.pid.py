# Creator:justice 廖振谊
# Creat time:2022/6/19 16:07
from multiprocessing import Process
import time
import os

def son():
    print("this is son process,and the pid of the son is ",os.getpid())
    while True:
        time.sleep(1)
if __name__ == '__main__':
    print("this is father process,and the pid of the father is ",os.getpid())
    p=Process(target=son)
    p.start()

