#Finding the nth occurance of a value in a list
list1=[1,2,3,4,1,10,11,1]


count = 1
#Iterator
for i in list1:
    if count==1:
        ind = list1.index(1)
        print("index is {} and values is {}".format(ind, list1[ind]))
    if((i==1 and count>1) and list1.index(1)!=-1):
        ind = list1.index(1,ind+1)
        print("index is {} and values is {}".format(ind, list1[ind]))
    count+=1



