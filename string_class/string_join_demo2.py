#this is a string
#step2
#This method splits string and concatenates with join using '-'
def split_and_join(line):
    word_list=line.split(" ")
    output_str='-'.join(word_list)
    return output_str

#Step1
line=input()
output_str1=split_and_join(line) #caller
print(output_str1)
