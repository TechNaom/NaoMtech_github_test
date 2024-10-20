#Sum of factors of a number.

#Read a n from keyboard
n=int(input("Enter n"))

#Variable to result
result=0
#Iterate for loop 1 to n
for i in range(1,n+1):
    #condition check - if i divides n or not
    if(n%i==0):
        result=result+i

print("The sum of factors of {} is {}".format(n,result))