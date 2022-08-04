# Creator:justice 廖振谊
# Creat time:2022/6/29 16:46
import time
def time_check(func):
    def time_check1():
        start=time.time()
        func()
        end=time.time()
        print("the lasting time is",end-start)
    return time_check1

@time_check
def loop():
    for i in range(1000000):
        pass

ob=loop()

