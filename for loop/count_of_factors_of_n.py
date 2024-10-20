'''
Count of factors
'''

#Read n from keyboard
n=int(input("Enter n"))

count=0
#Iterate n from 1 to n
for i in range(1,n+1):
    #condition check - validate
    if(n%i==0):
        count=count+1

print("The count of factors of {} is {}".format(n,count))