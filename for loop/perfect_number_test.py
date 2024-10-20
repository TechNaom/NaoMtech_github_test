#Perfect number - sum of factors of a number equal to actual number excluding factor of itself
#Example ->6 ->1,2,3,6 ->1+2+3 -> 6 ->

#Reading n
n=int(input("Enter n"))
result=0

#Iterate loop from 1 to n
for i in range(1,n):
    #condition check
    if(n%i==0):
        result=result+i

#checking perfect or not
if(result==n):
    print(" {} is perfect number".format(n))
else:
    print(" {} is not a perfect number".format(n))

