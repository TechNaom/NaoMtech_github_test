#Program to find fibonacci series

a=0
b=1

n=int(input("Enter n"))

i=1
print(a,"",b,end=' ')
while(i<=n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    i=i+1
