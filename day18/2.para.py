# Creator:justice 廖振谊
# Creat time:2022/6/19 21:19
from multiprocessing import Process
import time
nums=[1,2,3]
def son(name,age,**kwargs):
    print('name=%s,age=%d'%(name,age))
    name='lzy'
    print("In the son,name is",name)
    print(kwargs)
    time.sleep(1)
def son1():
    nums.append(4)
    print("in the son1,nums is",nums)
    time.sleep(1)

if __name__ == '__main__':
    name="Justice"
    age=24
    s=Process(target=son,args=(name,age),kwargs={'1':'a'})
    s.start()
    print("In the father,name is",name)
    time.sleep(1)
    s.terminate()
    s1=Process(target=son1)
    s1.start()
    print("in the father,the nums is",nums)
    s1.join()
    time.sleep(1)
    print("after the join,nums is",nums)


