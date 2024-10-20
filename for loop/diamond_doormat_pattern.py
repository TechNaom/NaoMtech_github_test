import sys
value=input()
val_list=value.split(" ")
n=int(val_list[0])
m=int(val_list[1])
#message=input("Enter message").upper()
r1=r2=(m-3)//2
temp=0
for i in range(1,n+1):
     if(i%2==1 and r1!=0):
        for k in range(1,(r1-i)+(i+1)):
            print("-", end='')
        for j in range(1,i+1):
            temp=j
            print(".|.",end='')
        for k in range((r1-i)+(i+1),1,-1):
            print("-", end='')
        r1 -= 3
        print()

#msg_len=len(message)
#width=m-msg_len
print("{}".format("WELCOME".center(m,'-')))

l=r2-3
for val in range(0,temp+1):
    if (val % 2 == 1):
        for k in range(1,r2-l+1):
             print("-", end='')
        for j in range(0,(temp+1)-val):
            print(".|.",end='')
        for k in range(1, r2 - l+1):
            print("-", end='')
        l=l-3
        print()






