'''
*
**
***
****
*****
'''
#Reading n
n=int(input("Enter n"))

#Outer loop initialization
i=1

#Outer loop
while(i<=n):
    ##inner loop initialization
    j=1
    while (j <= i):
        print('*',end='')
        j+=1
    i+=1
    print()
