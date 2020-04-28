person = {'name': 'Sasa', 'age': 50, 'job': 'Programmer'}
#person = {'name':'Sasa','age':50}

# LBYL (NONPYTHONIC)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print('Missing some keys')

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))
