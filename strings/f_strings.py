# F-Strings - tut by Corey Schafer https://www.youtube.com/watch?v=nghuHvKLhJA
from datetime import datetime
first_name = 'sasa'
last_name = 'Meow'

#sentence = 'My name is {} {}'.format(first_name,last_name)
#print(sentence)

sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)

person = {'name':'Sasa','age':12}
sentence = f'My name is {person["name"]} and I am {person["age"]}'
print(sentence)

calculation = f'4 times 11 is equal to {4*11}'
print(calculation)

for n in range (1,11):
    sentence = f'The value is {n:02}'
    print(sentence)

pi = 3.1415926535
sentence = f'Pi is equal to {pi:.5f}'
print(sentence)

bday = datetime(2001,1,1)
print(f'Sasa has a birthday on {bday:%B %d,%Y}')