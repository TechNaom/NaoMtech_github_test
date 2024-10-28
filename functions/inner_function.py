#Calling inner function directly from driver program

#outer
def f1():
    print("Outer")
    #inner functions
    def f2():
        print("Hi Im inner")
    return f2
#Test calling
inner_func=f1()
inner_func()
