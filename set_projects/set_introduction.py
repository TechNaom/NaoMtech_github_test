#Creating set

#Approach1:-{}
set1={1,2,3,4,5,6}
print(type(set1))
print(set1)

#Approach2:-set()
set2=set([1,2,3,4,5])
print(set2)

set3={1,2,3,4,5,1,2,3,4,5}
print(set3)

#Scenario
list1=[1,2,3,4,1,2,4,4]
set4=set(list1)
print(set4)

#Iterating set
#No indexing
for i in set1:
    print(i)

#Sum of elements of set
#Approach1
result=0
for i in set1:
    result=result+i

print("The result is {}".format(result))

#Approach2
sum2=sum(set1)
print("The result is {}".format(sum2))

#Methods of set Class:
#add() - add ane element to a set
#remove() - remove an element from a set
#copy()  - create another copy of a set
#update()  -
#clear()

marks_set=set()
print(marks_set)

#Lets add some data set
marks_set.add(90)
marks_set.add(80)
marks_set.add(70)
marks_set.add(85)
marks_set.add(60)
marks_set.add(40)
marks_set.add(68)
marks_set.add(69)


print(marks_set)

#find length of a set
set_len=len(marks_set)
print(set_len)

total_sum=sum(marks_set)
avg_marks=total_sum/len(marks_set)

print("The total is ",total_sum)
print("The avg is ",avg_marks)

#Remove min element from a set
#remove
min_marks=min(marks_set)
marks_set.remove(min_marks)
print("The marks_set is",marks_set)

marks_set2=marks_set.copy()
print("The marks_set2is",marks_set2)

marks_set.update({100,200,3000,400,500})
print(marks_set)

marks_set.clear()
print(marks_set)



















