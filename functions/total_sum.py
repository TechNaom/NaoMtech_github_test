#sum of n numbers

def sum_of_numbers(n):
    result = 0
    for dummy in range(1,n+1): #range(1,2,3,...10)
        result=result+dummy
    print("Sum of ",n,"numbers is ",result)
    return result

n=int(input("Enter n"))
sum_result=sum_of_numbers(n)
print(sum_result)


def sum_of_2(x,y):
    return x+y

print(sum_of_2(1,2))

#Lambda funtion - Anonymous function - No name
#lambda arguments:expression
sum_of_2 = lambda x, y,z: x + y+z
print(sum_of_2(1,2,3))



