spam = ['hello','hi','hi','howdy']
# index
print(spam.index('hi'))

# append - add at the end of the list
list1 = ['cat','dog','bat']
list1.append('moose')
print(list1)

# insert - add with defined index
list2 = ['cat','dog','bat']
list2.insert(2,'chicken')
print(list2)

# remove - specific value to remove
list3 = ['cat','dog','bat']
list3.remove('cat')
print(list3)

# sort
list4 = [2,4,3.14,1,-6]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
list5 = ['a','A','b','c','B','d']
list5.sort(key=str.lower)
print(list5)