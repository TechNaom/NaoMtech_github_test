#Armstrong using for loop
#153 --> sum of cube of each digit in that number
#1**3+5**3+3**3 -->153
#111 -> 1**3+1**3+1**3 #3

#1234 -->sum of digit to the power of n
#1**4+2**4+3**4+4**4
#12345
#1**5+2**5+.....

#Reading n
n=input("Enter n")

#Find length of n
length=len(n)

#covert numeric string to integer
m=temp=int(n)

sum1=0
#Iterate for loop passing length
for i in range(length):
    r=m%10
    sum1=sum1+r**length
    m=m//10

print("The sum is {}".format(sum1))

#Armstrong check
if(temp==sum1):
    print("The {} is Armstong".format(temp))
else:
    print("The {} is not Armstong".format(temp))
