# Creator:justice 廖振谊
# Creat time:2022/6/4 17:58
def find_the_number_more_than_half(list):
    n=len(list)
    result=list[0]
    count=1
    for i in range(2,n):
        if list[i]==result:
            count+=1
        else:
            count-=1
            if count<0:
                result=list[i]
                count=1
    temp=0
    for i in range(n):
        if list[i]==result:
            temp+=1
    if temp>=n/2:
        print("the number appearing more than half of the list is %d"%result)
    else:
        print("there is no number appearing more than half in the list")
list1=[3,7,3,4,5,6,7,7,7,7]
find_the_number_more_than_half(list1)