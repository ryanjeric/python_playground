import os

filepath = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(filepath)

# get current working directory
print(os.getcwd())
# change current working directory
os.chdir('c:\\')
print(os.getcwd())

# Absolute file path - begins in the root folder
# Relative file path - relative to the current directory
# . this folder
# .. parent folder

# os.chdir('c:\\')
# os.path.abspath('spam.png')
# os path.abspath('..\\..\\spam.png')
# os.path.isabs('..\\..\\spam.png')
# os.path.isabs('c:\spam.png')

# os.path.relpath('C:\\folder1\\folder2\\spam.png','c:\\folder')
# ''folder2\\spam.png'

# os.path.dirname('c:\\folder1\\folder2\\spam.png')
# c:\\folder1\\folder2
# os.path.basename('c:\\folder1\\folder2\\spam.png')
# spam.png
# os.path.basename('c:\\folder1\\folder2')
# folder2

print(os.path.exists('c:\\Program Files'))
print(os.path.isdir('c:\\Program Files'))
print(os.path.isfile('c:\\Program Files'))

print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('c:\\'))