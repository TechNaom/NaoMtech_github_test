
s1="apple"

#TestCase1:
#Index method return of a character present in a string
print("The index is {}".format(s1.index('a')))
print("The index is {}".format(s1.find('a')))

#TestCase2:
#Index method return of a character present in a string
#print("The index is {}".format(s1.find('A')))
#print("The index is {}".format(s1.index('A')))

print("The values are {} and {} ".format(10,20))
print(s1.upper())
print(s1.lower())

sentence = "The quick brown fox jumps over the lazy dog" #space
word_list=sentence.split(" ")

#split method splits string into words and stored into List and returns that list
#['The','quick',.....]

print(word_list)
#Print these word by word
for word in word_list:
    print(word)

s2="NaoMtech"

#ljust
#Takes 2 parameters - width,"character"
print(s2.ljust(20,"@"))
print(s2.rjust(20,"@"))
print(s2.center(20,"@"))

s3="abcbbcabcbcbc"
#count - returns number of occurances of a character or substring
print(s3.count("b"))
print(s3.count("ab"))

#UseCase ->Find max searches of some celebrity
#Who is Ranbir
#Is Ranbir Handsome
#What is caste of Ranbir
#Who is Deepika
#Is Deepika married
#What is caste of Ranbir
#Find the count of all celebrities and give ranking
#Ranbir - 100 -1
#Deepika - 99 - 2

s4="banaNa"
#Makes first character in a string as Capital letter and other characters to lower case
print(s4.capitalize())

s5="Liaom Neason"
print(s5.endswith("Neason"))
print(s5.startswith("Neason"))

s6="abc123"

print(s6.isalnum()) #True
print(s6.isdigit()) #False
print(s6.isalpha()) #False
print(s6.islower()) #True
print(s6.isupper()) #False


s7="abcdefgh" #a-b-c-d-e-g-h
#join method
#It iteratively or repeatedly combines a characater or string wth each character or a letter present into input string
print("-".join(s7))
print("abc".join(s7))



















































