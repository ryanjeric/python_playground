import os,shelve
# Shelve module can store python values in binary file
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Sasa','Prosasa','Chumsey']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.values()))
print(list(shelfFile.keys()))