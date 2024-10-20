#Creating functions
#function1 - find sum of 2 numbers - return 1 value
#function2 -sum/sub/mul  ->returns multiple values

#function returns 1 value
def addition(a,b):
      c=a+b
      return c

#function returns multiple values
def arithOperations(a,b):
      add=a+b
      diff=a-b
      prod=a*b
      return add,diff,prod  # Tuple

#calling addition
result1=addition(10,20)
result2=arithOperations(10,20)

print("The result {{}} from addition() is {}".format(result1))
print("The result from arithOperations() is {}".format(result2))








