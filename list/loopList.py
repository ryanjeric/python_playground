list1 = ['cat','bat','cow']
for i in list1:
    print(i)

list2 = list(range(0,100,2))
for x in list2:
    print(x)

supplies = ['pens','staples','flame-throwers','binder']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
supplies = ['pens','pens','pens','pens','pens','pens','pens','pens',]
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat','orange','loud']
size,color,disposition = cat
print(size)
print(color)
print(disposition)

#swapping variables
a = 'AAA'
b = 'BBB'
a,b = b,a
print(a + b)


