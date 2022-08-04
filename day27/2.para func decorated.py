# Creator:justice 廖振谊
# Creat time:2022/6/29 17:05
def wrapped_func(func):
    def wrapped(*args,**kwargs):
        print("this is wrapped func")
        func(*args,**kwargs)
    return wrapped

@wrapped_func
def plus(*args,**kwargs):
    print("the sum of arr is",sum(args))
    print(kwargs)

ob=plus(1,2,3,4,5,di=10)
