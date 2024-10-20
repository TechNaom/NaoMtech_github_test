#getattr ->retrieves a method passed as string and applies that method on input
import time


def string_validator(word,check_type):
           flag=False
           for ch in word:
               method=getattr(ch,check_type)
               if method():
                   flag=True
           return flag

start_time=time.time()
input1=input()
print(input1.isalnum())
print(string_validator(input1,'isalpha'))
print(string_validator(input1,'isdigit'))
print(string_validator(input1,'isupper'))
print(string_validator(input1,'islower'))
end_time=time.time()
execution_time=end_time-start_time
print("The execution time is {:.6f}".format(execution_time))


