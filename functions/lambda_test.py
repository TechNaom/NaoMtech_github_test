#Hello world
x=lambda : print("Hello world")
x()

#Finding sum of 2 numbers
sum_of_numbers=lambda  x,y:x+y
sum_val=sum_of_numbers(10,20)
print("The sum of 2 numbers is {}".format(sum_val))

#Sorting a dataset using lambda function
data = [(1, 'apple'), (2, 'orange'), (3, 'banana')]
asc_sorted_data=sorted(data,key=lambda  t:t[1])
print("Ascending sort :",asc_sorted_data)
dsc_sorted_data=sorted(data,key=lambda  t:t[1],reverse=True)
print("Descending sort :",dsc_sorted_data)

#Finding squares of numbers from 1-10
squares=[i*i  for i in range(1,11)]
print(squares)










