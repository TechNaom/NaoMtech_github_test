s1={1,2,3,4,5,6,7,8}
s2={1,2,3,4}
print(s1)
print(s2)

print(s1.difference(s2)) #Remove common elements and keep uncommon elemnts
print(s1)
print(s2)

print(s1.intersection(s2)) # common elements are returned.
print(s1)
print(s2)

s1.difference_update(s2) #Remove common elements and keep uncommon elements
print(s1)
print(s2)

s1={1,2,3,4,5,6,7,8}
s2={1,2,3,4}
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

print(s1.symmetric_difference(s2))
print(s1.union(s2))



