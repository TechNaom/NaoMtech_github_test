#Creating a list of 10 digits
list1=[1,2,3,4,5,5,6,7,8,10]

square_list=[]
#Logic
#Iterate list and do square of each value
for i in list1:
    square_list.append(i*i)

#Print squares
print(list1)
print(square_list)

#Refining with List comprehension
square_list2=[i*i for i in list1]
print(square_list2)







