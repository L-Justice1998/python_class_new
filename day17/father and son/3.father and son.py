# Creator:justice 廖振谊
# Creat time:2022/6/17 21:58
from multiprocessing import Process
import time
def func():
    while True:
        print("-----2-----")
        time.sleep(1)

if __name__ == '__main__':
    p=Process(target=func)
    p.start()
    while True:
        print("-----1-----")
        time.sleep(1)
