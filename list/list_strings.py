import copy

print(list('hello'))
name = 'Ryan'
print(name[0])

for letter in name:
    print(letter)

name = "ryan a cat"
newname = name[0:5] + 'the' + name[6:]
print(newname)

# Reference
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'hello'
print(cheese)
print(spam)
print()
# copy
spam1 = [0, 1, 2, 3, 4, 5]
spam2 = copy.deepcopy(spam1)
spam2[0] = 'hello'
print(spam1)
print(spam2)

# \ - slash line = new line code
print('Four score and seven' + \
      'years ago')
print('Four score and seven' + 'years ago')
