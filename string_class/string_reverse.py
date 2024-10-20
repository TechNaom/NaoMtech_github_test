s1=input("Enter n") #abcdefg

str_len=len(s1)
rev_str=''

for i in range(str_len-1,-1,-1):
    rev_str=rev_str+s1[i]    #g+f  gf+e gfe+d ...

print(rev_str)
