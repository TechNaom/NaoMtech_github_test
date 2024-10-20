#Creating a list of 10 digits
list1=[1,2,3,4,5,5,6,7,8,10]

even_list=[]
#Checking even
for i in list1:
    if(i%2==0):
        even_list.append(i)

print(even_list)

#Printing even values using List comprehension
even_list2=[i for i in list1 if i%2==0]
print(even_list2)

#Add even in place of even value and odd in place of odd
new_even_list=["Even" if i%2==0 else "odd" for i in list1]
print(new_even_list)