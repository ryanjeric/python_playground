import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret doc. to Agent Bob.'))
# Sub - substitute
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret doc. to Agent Bob.'))

namesRegex2 = re.compile(r'Agent (\w)\w*')
print(namesRegex2.findall('Agent Alice gave the secret doc. to Agent Bob.'))
# Sub - substitute
print(namesRegex2.sub(r'Agent \1****', 'Agent Alice gave the secret doc. to Agent Bob.'))

# Verbose
phoneRegex = re.compile(r'''
(\d\d\d-)| # area code w/o parens,with dash
(\(d\d\d\) ) # or area code wi parens and no dash
\d\d\d # first 3 digits
-     # second dash
\d\d\d\d # last 4 digits
\sx\d{2,4} # extension, like x1234
''',re.I | re.VERBOSE | re.DOTALL) # Bit wise operator
