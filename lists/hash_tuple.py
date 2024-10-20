
n=int(input())
list1=input().split(" ")
list2=[]
for i in list1:
    list2.append(int(i))
t=tuple(list2)
print(hash(t))
