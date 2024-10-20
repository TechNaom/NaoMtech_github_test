#Sum of first n natural numbers
#Author : ManoRam Shiv Prabhu

n=int(input("Enter n"))

result=0
for i in range(1,n+1):
    result=result+i

print("The result is {}".format(result))


