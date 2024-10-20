#string class
#isalnum,isalpha,isdigit,isupper,islower
#decision making elif
#for loop
import time

start_time=time.time()
input1=input()

#if string has any alphanumeric character
#if string has any alphabetical characters
flag=False
for ch in input1:
    if(ch.isalnum()):
        flag=True
print(flag)

#if string has any alphabetical characters
flag=False
for ch in input1:
    if(ch.isalpha()):
        flag=True
print(flag)

#if string has any digits
flag=False
for ch in input1:
    if(ch.isdigit()):
        flag=True
print(flag)

#if string has any lower case
flag=False
for ch in input1:
    if(ch.islower()):
        flag=True
print(flag)

#if string has any upper case
flag=False
for ch in input1:
    if(ch.isupper()):
        flag=True
print(flag)
end_time=time.time()
execution_time=end_time-start_time
print("The execution time is {:.6f}".format(execution_time))








