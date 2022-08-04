# Creator:justice 廖振谊
# Creat time:2022/6/29 17:44

def wrapped_func_para(x,y):
    def wrapped_func(func):
        def wrapped(*args):
            print("this is wrapped func,and x and y are",x,y)
            return func(*args)
        return wrapped
    return wrapped_func

@wrapped_func_para(3,6)
def plus(*args):
    return sum(args)

@wrapped_func_para(4,6)
def plus1(*args):
    return sum(args)

ob=plus(1,2,3,4,5)
print(ob)
ob1=plus1(1,2,3,4,5)
print(ob1)
