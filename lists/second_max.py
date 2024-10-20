'''
Finding second max
'''
#solution1
#creating a list
list1=[10,7,11,16,6,8]
print(list1)
#Second max
max_val=max(list1)
#16
#Remove it from the list
list1.remove(max_val)
max_val2=max(list1)
print("The second max is {}".format(max_val2))
print(list1)

#solution2
#sort list in desceding order
list1.sort(reverse=True)
print(list1)

#[16,11,10,8,7,6]
n=2
print("The second max element is {}".format(list1[n-1]))

#finding nth max of a list
n=int(input())
print("The {} max element is {}".format(n,list1[n-1]))









