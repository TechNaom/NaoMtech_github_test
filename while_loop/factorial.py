#Factorial of a number n
#Loop initialization
i=1

#Reading n
n=int(input("Enter n"))
result=1
temp=n
#5 ->5*4*3*2*1
while(n>=1):
    result = result*n
    n=n-1

print("The factorial of {} is {} ".format(temp,result))