#case1
a="abc"
b="bbc"

print(a+b)

#case2
x="abc"
y=10
print(x+str(y))
#abc10
#error

#case3
print("abc"*10)

#"abc"+"abc"+"abc"

s3="abcdefgh"

if 'z' in s3:
    print(True)
else:
    print(False)

#case4
s4="abcdef"

if 'z' not in s3:
    print(True)
else:
    print(False)

#case5 -is/is not
s11="abc"
s12="abc"
print(id(s11))
print(id(s12))
print(s11 is s12)

a=10
b=10
print(id(a))
print(id(b))

print(a is b)

#why?
#In python,all almost all datatype are immutable.

















