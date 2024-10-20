#Create a tuple containing numbers greater than 5 from the given tuple below using a for loop.
#Create a tuple number>5 ->(6,7,8....)
#Create an empty list -> Put all numbers > 5 into list
#Convert that list into tuple

myTuple = (3, 6, 2, 1.89, 1, 9, 5.5, 5, 7, 8, 1, -3, -5, 10.3)

#Follow 2 Solutions
#Solution1  - Standard Solution
#Iterarte tuple

myList=[]

for val in myTuple:
    #conditional appending
    if(val>5):
        myList.append(val)

print(myList)

#converting list to tuple
myTuple2=tuple(myList)

print(myTuple)
print(myTuple2)

#Solution2:
myTuple3=(val  for val in myTuple if val>5)
print(myTuple3)














