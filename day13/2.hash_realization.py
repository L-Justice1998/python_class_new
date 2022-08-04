# Creator:justice 廖振谊
# Creat time:2022/6/13 17:37
import random
MAXKEY=2000
def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY

def bitmap(list1):
    bitnum=0
    list2=[]
    for i in list1:
        if not bitnum>>i&1:
            list2.append(i)
            bitnum|=1<<i
    print(bin(bitnum))
    return list2

word_list=["Shanghai","Beijing","New York","Chicago","Shenzhen","London",
           "Beijing1","Beijing2","Beijing3","Beijing4","Beijing5"]
hash_table=[None]*MAXKEY
for word in word_list:
    hash_table[elf_hash(word)]=word
    print("the hash value of %8s is %8d"%(word,elf_hash(word)))

list1=[random.randint(1,100) for i in range(1000)]
list1.sort()
print("the length of list1 is %d"%len(list1))
list2=bitmap(list1)
print("the length of list1 is %d"%len(list2))
print(list1)
print(list2)