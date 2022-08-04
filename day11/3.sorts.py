# Creator:justice 廖振谊
# Creat time:2022/6/10 20:06
import random


class sorts:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.help_arr = [0 * self.n]

    def bubble_sort(self):
        n = self.n
        arr = self.arr
        for i in range(n - 1, 1, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def choose_sort(self):
        n = self.n
        arr = self.arr
        current_index = 0
        min_index = 0
        for current_index in range(n - 1):
            for i in range(current_index + 1, n):
                min_index = current_index
                if arr[i] < arr[min_index]:
                    min_index = i
                arr[min_index], arr[current_index] = arr[current_index], arr[min_index]

    def insert_sort(self):
        n = self.n
        arr = self.arr
        for i in range(1, n):
            j = i - 1
            temp = arr[i]
            while j >= 0:
                if temp < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = temp

    def patition(self, left, right):
        k = left
        arr = self.arr
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.patition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_heap(self, pos, len):
        """
        调整以pos为index的根节点的子树为大根堆
        :param pos: 根节点的index
        :param len:只考虑后面到len位置
        :return: 
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < len:
            if son + 1 < len and arr[son] < arr[son + 1]:
                son = son + 1
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = dad * 2 + 1
                # 继续往下层去 只需考虑一侧，因为下面的已经排好了
            else:
                break

    def build_heap(self):
        arr = self.arr
        n = self.n
        for i in range(n // 2 - 1, -1, -1):
            self.adjust_heap(i, n)
        # 先变成大根堆

    def heap_sort(self):
        arr = self.arr
        n = self.n
        self.build_heap()
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        for i in range(n - 2, 0, -1):
            self.adjust_heap(0, i + 1)
            arr[0], arr[i] = arr[i], arr[0]

    def merge_help(self, left, right):
        """
        在内部进行排序
        :param left: 
        :param right: 
        :return: 
        """
        help_arr = self.help_arr
        arr = self.arr
        help_arr[left:right + 1] = arr[left:right + 1]
        mid = (left + right) // 2
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if help_arr[i] < help_arr[j]:
                arr[k] = help_arr[i]
                i += 1
            else:
                arr[k] = help_arr[j]
                j += 1
            k += 1
        while i <= mid:
            arr[k] = help_arr[i]
            k += 1
            i += 1
        while j <= right:
            arr[k] = help_arr[j]
            k + +1
            j += 1

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge_help(left, right)

    def test_sort(self, method, *args, **kwargs):
        print("before sorted,the arr was")
        print(self.arr)
        print("after sorted,the arr is")
        method(*args, **kwargs)
        print(self.arr)

    def count_sort(self, range0):
        """
        对0到range的数进行排序
        :param range:
        :return:
        """
        count_arr = [0] * (range0 + 1)
        for i in self.arr:
            count_arr[i] += 1
        k = 0
        for i in range(range0 + 1):
            for j in range(count_arr[i]):
                self.arr[k] = i
                k += 1


if __name__ == '__main__':
    arr = [random.randint(0, 100) for i in range(2000)]
    # 左闭右闭区间
    s = sorts(arr)
    s.test_sort(s.count_sort, 100)
