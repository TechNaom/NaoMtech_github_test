#Finding count of each element from a list
list2=[1,2,3,4,1,2,3,4,1,2,3,4,7,10,11]
print(list2)
#Create a new list without duplicates
#list3=[1,2,3,4,7,10,11]
list3=[]

for i in list2:
    if i not in list3:
        list3.append(i)

print(list3)

#finding occurances of each element in a list
for i in list3:
    print(i,list2.count(i))






