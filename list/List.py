listx = ['cat', 'bat', 'rat', 'elephant']
print(listx)
print(listx[0])
print(listx[2:4])

list2 = [['cat','bat'],[10,20,30]]
print(list2[0][1])
print(list2[-1][-1])

list3 = ['cat','bat','sad']
list3[2] = 'cow'
print(list3)
list3[0:3] = ['a','b','c']
print(list3)

list4 = ['a','b','c','d']
print(list4[:2])
print(list4[1:])
del list4[2] # delete c
print(list4)

print(len('Hello'))
print(len([1,2,3]))

print('Hello' * 3)
print(list('hello'))

print('howdy' in ['hello','hi','howdy'])
print('howdy' not in ['hello','hi','howdy'])