my_string = "Hello, World!"

print("The slice1 is {}".format(my_string[0:4])) # printing Hell
print("The slice2 is {}".format(my_string[0:5])) #Hello
print("The slice3 is {}".format(my_string[7:13])) #World

sentence = "The quick brown fox jumps over the lazy dog"

print("The slice4 is {}".format(sentence[0:3])) #The
print("The slice5 is {}".format(sentence[:3])) #The

start_ind=sentence.index('j')
#Usecase3 -  Extract jumps over dynamically from a string
end_ind=sentence.find('r',11+1)
print("The slice5 is {}".format(sentence[start_ind:end_ind+1])) #The

#Uscecase4 -Reversing
#Reversing a string
print("The slice6 is {}".format(my_string[::-1])) #The

#Getting alternate character in reverse order
print("The slice7 is {}".format(my_string[::-3])) #The

#Uscecase5 -Forward by using step
print("The slice8 is {}".format(my_string[::2])) #The
print("The slice8 is {}".format(my_string[::2])) #The
print("The slice9 is {}".format(my_string[::3])) #The

print("The slice10 is {}".format(my_string[0:])) #The
print("The slice11 is {}".format(my_string[my_string.index('W'):])) #The
print("The slice11 is {}".format(my_string[:my_string.index('o')+1])) #The



















