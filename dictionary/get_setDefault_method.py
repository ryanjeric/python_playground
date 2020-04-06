eggs = {'name':'Zophie','species':'cat','age':8}

# get method (key,defaultValue)
print(eggs.get('age',0))
print(eggs.get('color','black'))

# setdefault method
eggs.setdefault('color','black')
print(eggs)