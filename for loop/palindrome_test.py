'''
Palindrome ->121 ->121 252
Author:ManoRam

Step1:
123 -> if number n ->number of digits in n -> 3 digited -> 3 times
    ->4 digited -> 4 times
n
123 -> 3 ->12
n
12 -> 2 ->1
n
1 -> 1 -> 0

Tip of the program: divide number by 10 and get reminder
'''

#Reading n from keyboard
n=int(input("Enter n")) #123
temp=n
reverse=0
while(n>0):
    r=n%10
    reverse=reverse*10+r
    n=n//10

#validating palindrome
if(reverse==temp):
    print("{} is palindrome".format(temp))
else:
    print("{} is not palindrome".format(temp))






