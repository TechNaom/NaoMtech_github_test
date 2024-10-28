#Replace normal function with lambda function as parameter to map()

list_integers=[100,200,300,400,500]

#Testcase1
output_list=map(lambda x:x+1000 ,list_integers)
print(output_list)

#Testcase2
output_tuple=tuple(map(lambda x:x+1000 ,list_integers))
print(output_tuple)