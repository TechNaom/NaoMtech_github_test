#Applying filter() on list of values

#list of integers
list1=[10,15,20,19,55]

#Testing even or not
def number_check(value):
    return value%2==0

#Applying a filter
#Testcase1
output_result=filter(number_check,list1)
print(output_result)

for val in output_result:
    print(val)

#Testcase2
output_result=list(filter(lambda x: x%2==0,list1))
print(output_result)

for val in output_result:
    print(val)