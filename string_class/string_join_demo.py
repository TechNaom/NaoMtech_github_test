#string concatenation using join
#input - this is a string
#output - this-is-a-string

s1="this is a string"

word_list=s1.split(" ") #Returns a list of tokens

output_str='-'.join(word_list)

print("The combined string  is {}".format(output_str))

#['this','is','a','string']
#this-is-a-string



