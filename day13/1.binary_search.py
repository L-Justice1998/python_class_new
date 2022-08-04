# Creator:justice 廖振谊
# Creat time:2022/6/13 17:27
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else:
            left = mid + 1
    print("the target is not in the arr")

arr=[1,3,5,7,9,11,13,15]
print(binary_search(arr,6))