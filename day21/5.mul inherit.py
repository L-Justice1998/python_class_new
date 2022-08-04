# Creator:justice 廖振谊
# Creat time:2022/6/22 21:32
class parent():
    def __init__(self,name,*args,**kwargs):
        print("this is parent init starting")
        self.name=name
        print("this is parent init ending")


class son1(parent):
    def __init__(self, name,age,  *args, **kwargs):
        print("this is son1 init starting")
        self.age=age
        super().__init__(name, *args, **kwargs)
        print("this is son1 init ending")

class son2(parent):
    def __init__(self,name, gender, *args, **kwargs):
        print("this is son2 init starting")
        self.gender = gender
        super().__init__( name,*args, **kwargs)
        print("this is son2 init ending")

class grandson(son1,son2):
    def __init__(self, name,age, gender, *args, **kwargs):
        print("this is grandson init starting")
        super().__init__(name,age,gender)
        print("this is grandson init ending")

people=grandson("lzy",'24','male')
print(people.name)
print(people.age)
print(people.gender)
print(grandson.__mro__)