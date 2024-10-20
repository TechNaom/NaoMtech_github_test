#Methods dict class
fruits = {"banana": "yellow", "strawberry": "red", "grapes": "purple",'apple':'red'}

print(fruits)
print(type(fruits))

#Methods of dict class
#Items
print(fruits.items())

#I want to iterate - what happens let us see
for fruit in fruits:
    print(fruit)

#Approcha1
print("Reading data from dict using key")
for fruit in fruits:
    print(fruit,fruits[fruit])

#Approch2
print("Reading data from dict applying items method")
for fruit,color in fruits.items():
    print(fruit,color)

#keys() - return list of keys - ['banana',''straw..',......]
for fruit in fruits.keys():
    print(fruit)

#Values - returns list of values
for fruit in fruits.values():
    print(fruit)

#get() - return value of of a key
print(fruits.get('banana')) #'Yellow'

#Aprroach3
for fruit in fruits:
    print(fruit,fruits.get(fruit))

#pop() - removes a key - value pair based on key
print(fruits.pop('banana'))
print(fruits)

#popitem() - remove last item(key- value) from a dict
print(fruits.popitem())
print(fruits)

#popitem
print(fruits.popitem())
print(fruits)

#copy() - create another copy of existing dict
fruits2=fruits.copy()
print(fruits2)

#fromkeys() - It is used to perform group initialization of all keys to a default value
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
print(dishes)
dishes2=fruits.fromkeys(dishes.keys(),100)
print(dishes2)

#setdefault - if key is present then returns value of that key else return None.
person = {'name': 'Phill', 'age': 22}
age=person.setdefault('age')
print(age)

#update -
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
dishes.update({"icecream":20,"kulfi":30})
print(dishes)

dishes.clear()
print(dishes)


















