import re


# ^ - start , End $
begistWithHelloRegex = re.compile(r'^Hello') # String begins
hello = begistWithHelloRegex.search('Hello there!')
print(hello)

endWithWorldRegex = re.compile(r'world!$')
helloworld =endWithWorldRegex.search('Hello world!')
print(helloworld)

allDigitsRegex = re.compile(r'^\d+$')
num = allDigitsRegex.search('234234234234252')
notnum = allDigitsRegex.search('23423x4234234252')
print(num)
print(notnum)

# .  = any char except newline
atregex = re.compile(r'.{1,2}at')
print(atregex.findall('The cat in the hat sat on the flat mat.'))

# .* = any char and anything
name = 'First Name: Ryan Last Name: Sabado'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRaw = nameRegex.findall(name)
print(nameRaw)

# .* - Greedy match | .*? - Non Greedy match
serve = '<To serve humans> for dinner>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# re.DOTALL
prime = 'Serve the public.\nProtect the innocent.\nUpload the law'
dotStar = re.compile(r'.*',re.DOTALL) # including newline
print(dotStar.search(prime))

# re.I - ignorese
vowelRegex = re.compile(r'[aeiou]',re.I)
rr = vowelRegex.findall('RyAn, why does your programming book talk about RoboCop so much')
print(rr)