#variable-length arguments **kwargs
#Dynamic variable - Implictly a dict(key/value)

def f1(**kwargs):
    print(type(kwargs))
    print(kwargs)

    if(len(kwargs)>1):
        for name,flower in kwargs.items():
             print(name ," " ,flower)


#testing
#Testcase1
f1()

#Testcase2
f1(x="rose")

#Testcase3
f1(x="rose",y="lilly")

#Testcase4
f1(x="rose",y="lilly",z='hibiscus')






