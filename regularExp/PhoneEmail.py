#! python3

import re,pyperclip
# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 414-55-0000, 555-0000, (415) 555-0000,555-0000 ext 12345,ext.12345,x12345
(
((\d\d\d)| (\(\d\d\d\)))?    #area code (optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x) #extention
(\d{2,5}))?   #extention
)
''',re.VERBOSE)
# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+     # domain part

''',re.VERBOSE)
#  Get the text off the clipboard
text = pyperclip.paste()
#  Extract the Email/Phone for the Text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNUmber in extractedPhone:
    allPhoneNumbers.append(phoneNUmber[0])

print(allPhoneNumbers)
print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)