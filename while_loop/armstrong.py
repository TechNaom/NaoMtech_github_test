'''
Sum of power of digits + Armstrong
Author : ManoRam
'''

#Reading n
n=input("Enter n")

#Finding length of n
length=len(n)

sum=0

temp=int(n) #253
temp1=temp #copying original value
while(temp>0): #condition check
    r=temp%10 # Get remainder
    sum=sum+r**length  #27+125 ->152+8
    temp=temp//10  #Get quotient

print("The sum of {} is {}".format(n,sum))

#Armstrong check
if(temp1==sum):
    print("{} is Armstrong".format(temp1))
else:
    print("{} not Armstrong".format(temp1))
