import os

if not os.path.isdir('c:\\ryan-sample'):
    os.makedirs('c:\\ryan-sample')
else:
    print("Folder Already Created")

hellofile = open('c:\\ryan-sample\\hello.txt')
# readmode
content = hellofile.read()
print(content)
hellofile.close()

hellofile = open('c:\\ryan-sample\\hello.txt')
content = hellofile.readlines()
print(content)
hellofile.close()

hellofile = open('c:\\ryan-sample\\hello2.txt','w')
content = hellofile.write('Hello!!!!!!!')
hellofile.write('Hello!!!!!!!')
hellofile.write('Hello!!!!!!!')
hellofile.close()

baconfile = open('bacon.txt','w') # w - write mode
print(os.getcwd())
baconfile.write('BACON is not a vegetable!')
baconfile.close()

baconfile = open('bacon.txt','a') # a - append mode
baconfile.write('\nBACON is not a vegetable!')
baconfile.close()

