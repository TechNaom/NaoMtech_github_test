'''
Prime or Composite
Author: ManoRam
Algorithm:
Step1:
Count of factors of a number
step2:
Validate if count equals to 2 -> Prime else composite
'''

#Read n from keyboard
n=int(input("Enter n"))
count=0

#Iterarte loop 1 to n
for i in range(1,n+1):
    #condition check
    if(n%i==0):
        count=count+1

#Validating count to check if number is prime or composite
if(count==2):
    print("{} is prime number".format(n))
else:
    print("{} is composite number".format(n))




