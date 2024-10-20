'''
Palindrome check
#123 -->321 ->Not Palindrome
#121 --> 121 ->Palindrome
#Phase1 -->Reverse a number
#Validate Palindrome
'''

n=int(input("Enter n"))
temp=n

sum=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10

print("The reverse of a {} is {}".format(temp,sum))

#Palindrome check
if(temp==sum):
    print("{} is Palindrome".format(temp))
else:
    print("{} is not Palindrome".format(temp))
