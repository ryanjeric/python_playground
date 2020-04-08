import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone = phoneRegex.search('My Phone number is 415-555-1234. Call me tomorrrow')
if(phone!=None):
    print(phone.group())
else:
    print('Nutnumber')

phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phone2 = phoneRegex2.search('My phone number is 415-444-1254')
phone3 = phoneRegex2.search('My phone number is 555-1254')
print(phone2.group())
print(phone3.group())

# * Zero or more
batRegex2 = re.compile(r'Bat(wo)*man')
bat2 = batRegex2.search('The advetures of Batwowowowowoman')
print(bat2.group())

# + 1 or more
batRegex3 = re.compile(r'Bat(wo)+man')
bat3 = batRegex3.search('The adventures of Batwoman')
print(bat3.group())

# escaping
regex = re.compile(r'\+\*\?')
reg=regex.search('I learned about +*? regex Syntax')
print(reg.group())

# Exact Match
haRegex = re.compile(r'(Ha){3}')
ha = haRegex.search('He said HaHaHa')
print(ha.group())

phoneRegex2 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
pn = phoneRegex2.search('My phone number are 415-555-1234,555-4242,212-555-0000')
print(pn)

# Range
ha2Regex = re.compile(r'(Ha){3,5}')
haz2 = ha2Regex.search('He said "HaHaHa"')
hax2 = ha2Regex.search('He said "HaHaHaHa"')
print(haz2.group())
print(hax2.group())

# greedy match
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
# non greedy match
digitRegex2 = re.compile(r'(\d){3,5}?')
print(digitRegex2.search('1234567890'))