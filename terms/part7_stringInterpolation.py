# STRING INTERPOLATION

name = 'Sasa'
age = 13

# String concatenation
greetings1 = 'My name is' + name + ' and I am ' + str(age) + ' years old'
print(greetings1)

# String interpolation - placeholders {} are replaced with their corresponding values
greetings2 = 'My name is {} and I am {} years old'.format(name,age)
print(greetings2)

greetings3 = 'I am {age} years old and my name is {name}'.format(name=name,age=age)
print(greetings3)
