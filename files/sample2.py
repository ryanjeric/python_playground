import  os
totalsize = 0

for filename in os.listdir('c:\\'):
        if os.path.isfile(os.path.join('c:\\',filename)):
            continue
        totalsize = totalsize + os.path.getsize(os.path.join('c:\\',filename))
print(totalsize)

os.makedirs('c:\\ryan-sample')