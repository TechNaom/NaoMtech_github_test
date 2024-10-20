#Create a tuple containing numbers greater than 5 from the given tuple below using a for loop.
myTuple = (3, 6, 2, 1.89, 'h', 1, 9, 5.5, 5, 7, 8, True, 1, -3, -5, 'USA', 10.3, 'France')

#We create 2 solutions

#Soultion1 - Standard Solution
myList=[]

for val in myTuple:
    if(type(val) == int or type(val)== float ):
        if(val>5):
            myList.append(val)

print(myList)

#solution2 - tuple comprehension
myTuple2 = tuple(val for val in myTuple if (type(val) == int or type(val) == float) and val > 5)
print(myTuple2)


