# Creator:justice 廖振谊
# Creat time:2022/6/29 18:03
class test():
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        print("this is call func")
        return self.func(*args,**kwargs)
@test
def test1(*args,**kwargs):
    print("this is test1")

test1()