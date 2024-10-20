import re

'''
number = int(input())
strings = []
for i in range(number):
    strings.append(input())

for word in strings:
    b1=bool(re.match(r'^[456]', word))
    b2=bool(re.match(r'^[0-9-]*$', word))
    #group_list=word.split("-")
    #count=0
    #for ch in word:
        #if(word.count(ch)>=4):
         #   count=word.count(ch)
    if  b1 and (len(word) == 16 or len(word) == 19) and b2:
        print("Valid")
    else:
        print("Invalid")
'''

import re

number = int(input())
strings = []
for i in range(number):
    strings.append(input())

for word in strings:
    is_special=0
    b1=bool(re.match(r'^[456]', word))
    b2=bool(re.match(r'^[0-9-]*$', word))
    group_list=word.split("-")
    if  b1 and b2 or len(word)==16 or  len(group_list) == 4:
        print("Valid")
    else:
        print("Invalid")


