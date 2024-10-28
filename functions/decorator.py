#decorator function
def make_pretty(func): #func is a parameter which accepts function as parameter
    def inner():
        print("I got decorated")
        #call to actual function
        func()
    return inner

#Actual function
@make_pretty
def ordinary():
    print("I am ordinary")

#Function call
ordinary()