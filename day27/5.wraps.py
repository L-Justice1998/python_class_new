# Creator:justice 廖振谊
# Creat time:2022/6/29 18:07
from functools import wraps
def wrapped_func_para(x,y):
    def wrapped_func(func):
        @wraps(func)
        def wrapped(*args):
            """
            this is wrapped func
            """
            print("this is wrapped func,and x and y are",x,y)
            return func(*args)
        return wrapped
    return wrapped_func

@wrapped_func_para(3,6)
def plus(*args):
    """
    this is plus func
    """

    return sum(args)

@wrapped_func_para(4,6)
def plus1(*args):
    """
    this is plus1 func
    """
    return sum(args)

ob=plus(1,2,3,4,5)
print(ob)
print(plus1.__doc__)
print(plus1.__name__)