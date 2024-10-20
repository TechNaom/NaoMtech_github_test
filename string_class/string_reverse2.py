#Reversing a string character by character - No len function
s1=input("Enetr n")
#012345
#abcdef
#-6..-2-1
str_len=len(s1)
for i in range(-1,-str_len-1,-1):  #abcd
     print(s1[i])

#abcd
#-4-3-2-1
#-4-1 ->-5

