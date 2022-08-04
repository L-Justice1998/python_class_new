# Creator:justice 廖振谊
# Creat time:2022/6/4 17:51
def find(list1,list2):
    result=[]
    n1=len(list1)
    n2=len(list2)
    i=0
    j=0
    while i<n1 and j<n2:
        if list1[i]==list2[j]:
            result.append(list1[i])
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
    return result
l1=[1,4,6,7,10,11]
l2=[1,6,8,9,11,12]
result=find(l1,l2)
print(result)