#Declaring 2 variables
year=int(input("Enter year"))

#checking leap or not
if(year%4==0):
    print("{} is leap year".format(year))
else:
    print("{} is not leap year".format(year))
