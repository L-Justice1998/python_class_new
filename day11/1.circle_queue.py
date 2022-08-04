# Creator:justice 廖振谊
# Creat time:2022/6/10 18:55
class circle_queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list1 = [None] * max_size
        self.front = self.rear = 0

    def insert_ele(self, element):
        """
        insert an element
        if full print the info
        :return:
        """
        if (self.rear + 1) % self.max_size == self.front:
            print("the circle queue is full which can not insert any element")
        else:
            self.list1[self.rear] = element
            self.rear = (self.rear + 1) % self.max_size

    def delete_ele(self):
        """
        delete an element and ruturn it
        if empty print the info
        :return:
        """
        if self.rear == self.front:
            print("the circle queue is empty which can not delete any element")
        else:
            temp = self.list1[self.front]
            self.list1[self.front] = None
            self.front = (self.front + 1) % self.max_size
            return temp


if __name__ == '__main__':
    c = circle_queue(5)
    c.insert_ele(1)
    c.insert_ele(2)
    c.insert_ele(3)
    c.insert_ele(4)
    c.insert_ele(5)
    print(c.list1)
    c.delete_ele()
    print(c.front, c.rear)
    c.delete_ele()
    print(c.list1)
