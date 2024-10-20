#Program to find count of factors of a number

n=int(input("Enter n"))

i=1
count=0
while(i<=n):
    if(n%i==0):
       count=count+1
    i=i+1

print("The count of factors of {} is {}".format(n,count))