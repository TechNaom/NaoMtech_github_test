#Declaring variables.
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))

#a>b and a>c
#b>a and b>c
#c>a and c>b

#checking condition
if(a>b):
    if(a>c):
        print("{} is bigger than {} and {}".format(a,b,c))
if(b>a):
    if(b>c):
        print("{} is bigger than {} and {}".format(b,a,c))
if(c>a):
    if(c>b):
        print("{} is bigger than {} and {}".format(c,a,b))