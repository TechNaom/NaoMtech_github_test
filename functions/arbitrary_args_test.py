#variable-length arguments *args
#A variable length arguments accepts variable size of input


def f1(*args): #* (Asterik) is need only while declaring parameter
    sum_val=0
    #print(type(args))
    print(args)

    if len(args)>1:
        for val in args:
            sum_val=sum_val+val

    print("The sum is {}".format(sum_val))


#Testing
#testcase0
f1()
#testcase1
f1(1)
#testcase2
f1(1,2)
#testcase3
f1(1,2,3)
#testcase4
f1(1,2,3,4)



