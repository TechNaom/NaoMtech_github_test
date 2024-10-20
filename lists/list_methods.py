list1=list()

#append() ->Insert last
list1.append(10) #
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)

print(list1)

#Using itertor
for i in range(1,10):
    list1.append(i)

print(list1)

#insert method
list1.insert(5,100) # Shifted
print(list1)

#How remove or delete elements from a List.
#remove() /pop()
#Remove - Remove  an element from a list - pass a value which we want remove
list1.remove(10)
print(list1)

#pop() - remove element based on index
list1.pop(5)
print(list1)

list1.pop()
print(list1)

list1.pop()
print(list1)

#remove()  - value based removal
#pop(index) - Index based removal
#pop()  - Remove elemnet at end of list.

#count - count returns number of occurances of a value
list2=[1,2,3,4,1,2,3,4,1,2,3,4]
print("The count of value is {}".format(list2.count(1)))

#default sorting is ascending
list2.sort()
print(list2)

#default sorting is descending
list2.sort(reverse=True)
print(list2)

list3=[1,3,5,2,7]
list3.reverse()
print(list3)

print(list3.index(7))

#extend - Merging of 2 lists
list3.extend([5,6,7,8,9])
print(list3)

list4=list3.copy() #Explicit copying
print(list4)

list4[0]=100
print("list3 .......",list3)
print("List4 .......",list4)

list5=list3
print("list3 .......",list3)
print("List5 .......",list5)

list5[3]=1000
print("list3 .......",list3)
print("List5 .......",list5)

print(id(list3))
print(id(list5))

print(id(list3))
print(id(list4))

#list1.clear()
print(list1)

#Generic Methods
#len()  - returns length of string
print(len(list1))

#min()
print(min(list1))

#max()
print(max(list1))

#sum()
print(sum(list1))

#sorted()
print(sorted(list1))

#all()
print(all(list1))

list1.append(0)
print(list1)
print(all(list1))   #All non zeros - True
                    #Even if one zero in a list- False
list1.clear()
list1.append(0)
list1.append(0)
list1.append(0)
list1.append(1)

print(list1)

#any()
print(any(list1))  #All elements are zeroes(0) - False
                   #Even one elemnet is non-zero - True















































