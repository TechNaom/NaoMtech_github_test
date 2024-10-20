#keywed parameters
#giving names to actual parameters/values - keywed parameters
#Always a keyed parameter should follow positional parameter
def person_details(name,age):
        print("The name is {} and age is {}".format(name,age))

#testing funtion
#testcase1
person_details("Peter",40) #passed
#testcase2
person_details(40,'Peter')
#tescase3
person_details(age=40,name="John")