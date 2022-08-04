# Creator:justice 廖振谊
# Creat time:2022/6/24 18:06
class goods:
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

apple=goods(3,0.8)
print(apple.price)
apple.price=5
print(apple.price)
del apple.price