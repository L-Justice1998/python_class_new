# Creator:justice 廖振谊
# Creat time:2022/6/24 18:25
class goods:
    """
    这是一个关于商品的类
    """
    def __init__(self,value,account):
        self.original_value=value
        self.account=account
    @property
    def price(self):
        return self.account*self.original_value

    @price.setter
    def price(self,value):
        self.original_value=value
        print("the original price is set to be",self.original_value)

    @price.deleter
    def price(self):
        print("the price is deleted")

    def __call__(self, *args, **kwargs):
        print("this is a call function")
apple=goods(5,0.8)
print(goods.__doc__)
apple()
print(goods.__dict__)
print(apple.__dict__)
