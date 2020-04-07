spam = 'Hello World!'

spam = spam.upper()
print(spam.isupper())
print(spam)

spam = spam.lower()
print(spam.islower())
print(spam)
print()

# isalpha
print('isalpha')
print('hello'.isalpha())
print('hello123'.isalpha())
print()
# isalnum
print('isalnum')
print('hello123'.isalnum())
print()
# isdecimal - numbers only
print('isdecimal')
print('123'.isdecimal())
print()
# isspace
print('isspace')
print('   '.isspace())
print('hello world'[5].isspace())
print()
# istitle
print('istitle')
print('Hello World'.istitle())
print()

#title
print('title')
print('hello world'.title())
print()
#startswith
print('startswith')
print('hello world'.startswith('hel'))
print('hello world'.startswith('Hel'))
print()
#endswith
print('endswith')
print('hello world'.endswith('world'))
print('hello world'.endswith('ld'))
print()
# join
print('join')
print(','.join(['cat','rat','bat']))
print(' '.join(['cat','rat','bat']))
print('\n'.join(['cat','rat','bat']))
print()
# split
print('split')
print('My name is Simon'.split())
print('My name is Simon'.split('m'))
print()
# ljust ,rjust,center
print('ljust ,rjust,center')
print('Hello'.rjust(10,'-'))
print('Hello'.ljust(10,'*'))
print('Hello'.center(10,'*'))
print()

# strip
print('strip,lstrip,rstrip')
str = 'Hello'.center(10,'*')
print(str.strip('*'))
print(str.lstrip('*'))
print(str.rstrip('*'))
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))
print()

# replace
str2 = 'Hello there!'
str2.replace('e','XYZ')
print(str2)
