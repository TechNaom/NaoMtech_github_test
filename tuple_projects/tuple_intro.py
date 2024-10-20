#Declaring tuple

#1 st way
   #0  1   2   3  4
t1=(1 ,2 , 3 , 4 ,5,1,2,3,1,2,3)
  #-5  -4 -3  -2  -1
print(t1)

#2nd way
t2=tuple([10,20,30,40])
print(t2)

#Extracting element from a tuple using index
print("Output using index")
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])

#Extracting  element by element from a tuple using iterator
print("Output from Iterator")

for i in t1:
    print(i)


#I would like to check if tuple is really immutable
#t1[0]=100 #error -TypeError:
#print(t1)

#Tuple class
#count
#index

print("The count is {}".format(t1.count(2)))
print("The count is {}".format(t1.index(2,7)))
print("The length of tuple is {}".format(len(t1)))
print("The min of tuple is {}".format(min(t1)))
print("The max of tuple is {}".format(max(t1)))
print("The sorted tuple is {}".format(sorted(t1))) #sorting cannot on tuple

li1=sorted(t1)
t1=tuple(li1)
print(t1)

#sorted(t1)
list1=list(t1)
list2=sorted(list1)
print(list2)



