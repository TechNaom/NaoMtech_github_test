#Declaring variables
a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))
d=int(input("Enter d "))

#a>b a>c a>d
#b>a b>c b>d
#c>a c>b c>d
#d>a d>b d>c

#Checking greatest
if(a>b and a>c and a>d):
    print("{} is big".format(a))
elif(b>c and b>d):
    print("{} is big".format(b))
elif(c>d):
    print("{} is big".format(c))
else:
    print("{} is big".format(d))
