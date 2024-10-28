import timeit
#factorial of a number

#Non Recursive Function
def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact

#Testing function
#Testcase1
ex1=timeit.timeit(factorial(5))
print(ex1)

#Recursive function
def factorial(n):
    if(n==1):
        return 1
    fact=n*factorial(n-1)
    return fact

#5*factorial(4)
#5*4*factorial(3)
#5*4*3*2*factorial(1)

#Testcase1
print(factorial(5))



