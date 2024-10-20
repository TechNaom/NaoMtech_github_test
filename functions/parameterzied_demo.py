'''
#Take 2 strings and combine 2 strings while printing
def combine_strings(str1,str2):
    print("{}{} ".format(str1,str2))

#function call
combine_strings("Hello","World")
This is test
'''
#import textwrap

def wrap(string, max_width):
    count=0
    str1=''''''
    for i in string:
         str1+=i
         count=count+1
         if(max_width==count):
             str1+='\n'
             count=0
    return  str1
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
