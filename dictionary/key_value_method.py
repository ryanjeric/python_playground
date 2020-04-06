# keys,values,items methods
eggs = {'name':'Zophie','species':'cat','age':8}
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)
for v in eggs.values():
    print(v)
for k,v in eggs.items():
    print(k, v)

print('cat' in eggs.values())
