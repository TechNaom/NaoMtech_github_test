#map()  - itera
#doing sum of elemnts of a list using map

#Input

list1=[1,2,3,4,5]

#Add each value by 100,again i want to replace it into list
#output
#[101,102,103,104,105]
#[
  #1,  ->  1+100
  #2,  ->  2+100
  #3,  ->  3+100
  #4,  ->  4+100
  #5   ->  5+100
#]

def add(list_val):
   return list_val+100

#map_object(101,102,....)
#list(....)
#[101,102,103,104,....]

#Testcase1-Generates a map output and we should iterate
output_list=map(add,list1)
print(output_list)

for val in output_list:
    print(val)

#Testcase2 - converting into a list adn itering it
output_list=list(map(add,list1))
print(output_list)

for val in output_list:
    print(val)
