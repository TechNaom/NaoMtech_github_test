#Program to find count of factors of a number

n=int(input("Enter n"))

i=1
count=0
#count of factors
while(i<=n):
    if(n%i==0):
       count=count+1
    i=i+1

print("The count of factors of {} is {}".format(n,count))
#Checking whether a number is prime or composite
if(count==2):
    print("The number {} is prime".format(n))
else:
    print("The number {} is composite".format(n))


