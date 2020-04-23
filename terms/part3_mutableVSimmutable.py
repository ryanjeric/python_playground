# Mutable vs Immutable

#Immutable int, float, bool, string, unicode, tuple.
a = 'sasa'
print(a)
print(id(a)) # id() memory address

#a[0] = 'S' # TypeError: 'str' object does not support item assignment
#print(a)
#print(id(a))

a = 'chamsey' # re-assign
print(a)
print(id(a)) # diff memory address
print()
# Mutable  list, dict, set
b = [1,2,3,4,5]
print(b)
print(id(b))

b[0] = 6
print(b)
print(id(b)) # same memory address