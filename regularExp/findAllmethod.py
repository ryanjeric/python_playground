import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

resume = '''
lorem 444-523-5555
lore 622-333-2345
lore m 631-333-1235
'''
#findall
phone = phoneRegex.findall(resume)
print(phone)
#Groups
phone2 = phoneRegex2.findall(resume)
print(phone2)

#Common Character Class (uppercase are opposites of lower)
# \d Any Numeroc digit from 0 - 9
# \D Any Character that is not a numeric digit from 0-9
# \w Any letter numeric digit, or the underscore character. (Word)
# \W Any character that is not a letter,numeric digit or the Underscore charater.
# \s Any Space tab or newline character
# \S Any Character that is not a Space,tab or newline

# 12 days of Christmas
lyrics = '''
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree
'''
# d = digit , + = 1 or more , s = space, w = word
xmaxRegex = re.compile(r'\d+\s\w+')
print(xmaxRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex2 = re.compile(r'[aeiouAEIOU]{2}')
lettersLower = re.compile(r'[a-z]')
print(vowelRegex.findall('Robocop eats baby food.'))
print(vowelRegex2.findall('Robocop eats baby food.'))

#Negative Char. Class = caret ^
isNotvowelRegex = re.compile(r'[^aeiouAEIOU]')
print(isNotvowelRegex.findall('Robocop eats baby food.'))