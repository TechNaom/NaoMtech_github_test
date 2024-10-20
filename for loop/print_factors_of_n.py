#Printing factors of a number

#Read n from keyboard
n=int(input("Enter n"))

#Iterate for loop from 1 to n
for i in range(1,n+1):
    #condition - we should see if i is a factor of n
    if(n%i==0):
        print("{} is a factor of {}".format(i,n))

