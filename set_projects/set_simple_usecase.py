#Get first element set  	1
#Get Last element of set  True
#Get middle element of set  5
#Algorithm
#convert set to list
#Find index of element
#Get value using index - list1[ind]

set1={1,2,3,4,5,6,10.5,"True"}

#solution
#convert set to List/Tuple
list1=list(set1)
print(list1)

#Get index of each element
ind=list1.index(1) #
# 0  1 2   3 4
#[1, 2, 3, 4, 5, 6, 10.5, 'True']
print(list1[ind])

ind=list1.index("True")
print(list1[ind])

ind=list1.index(5)
print(list1[ind])

ind=list1.index(3)
print(list1[ind])

ind=list1.index(4)
print(list1[ind])





