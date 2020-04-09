import os, shutil, send2trash
# file
# os.unlink('bacon_renamed.txt')
# folder
# os.rmdir('testFolder') # won't delete if folder is not empty
# shutil.rmtree('testFolder') # delete folder and its content


# Dry RUN FIRST BEFORE DELETING : check what to delete..
for filename in os.listdir():
    if filename.endswith('.py'):
        print(filename)
        #os.unlink(filename)

# sendtoTrash
send2trash.send2trash('sendtotrash.txt')