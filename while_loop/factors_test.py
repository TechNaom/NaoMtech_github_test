#Program to find factors of a number

n=int(input("Enter n"))

i=1

while(i<=n):
    if(n%i==0):
        print("{} is a factor".format(i))
    i=i+1
