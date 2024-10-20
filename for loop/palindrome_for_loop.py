# Palindrome using for loop

n=input("Enter n")
length=len(n)

m=temp=int(n) #chained initialization 123
rev=0

#Iterating length of n
for i in range(length):
     r=m%10
     rev=rev*10+r
     m=m//10

print("The reverse of {} is {}".format(temp,rev))

#Palindrome check
if(temp==rev):
    print("{} is palindrome".format(temp))
else:
    print("{} is not palindrome".format(temp))


