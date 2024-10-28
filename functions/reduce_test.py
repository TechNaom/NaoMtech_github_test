#Redcuce function testing
from functools import reduce

#Create a list of values
list1=[1,2,3,4,5]

#creating a customized function
def add(x,y):
    return x+y

#Tescase1
#creating reduce finction
output=reduce(add,list1) #reduce object
print(output)

#Tescase2
output=reduce(lambda x,y:x+y,list1) #reduce object
print(output)
