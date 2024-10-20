#Sum of First n numbers

#initialization
i=1
result=0

#Reading n
n=int(input("Enter n"))

#condition check
while(i<=n):
   result=result+i
   i+=1

print("The sum is {}".format(result))

