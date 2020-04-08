import re

message = 'My Number is 415-555-1011'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #(\d\d\d) - Group
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

message2 = 'My Number is (415)-555-1011'
phoneNumRegex2 = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d') # escape parenthesis
mo2 = phoneNumRegex2.search(message2)
print(mo2.group())

# Prefix
batRegex = re.compile(r'Bat(Man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))