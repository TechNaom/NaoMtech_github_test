#Declared integer list
l1=[1,2,3,4,5,5,6,7,8,9,10]

#Declared empty list
even_list=[]
odd_list=[]

#Iterating
for i in l1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("The even list {}".format(even_list))
print("The odd` list {}".format(odd_list))



