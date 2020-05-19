# https://www.youtube.com/watch?v=tJxcKyFMTGo - Corey Schafer
import os
from datetime import datetime
# print(dir(os))

# GET Current Working Directory
print(os.getcwd())

# Change Working Directory
# os.chdir('/Users/user/Desktop')
# print(os.getcwd())

# List Files/Folders
# print(os.listdir())

# Create directory
os.mkdir('os-demo')
os.makedirs('os-demo2/sub-dir')
print(os.listdir())
# Remove directory
os.rmdir('os-demo')
os.removedirs('os-demo2/sub-dir')

# Renaming file
# os.rename('test.txt','demo.txt')

print(os.stat('os-sample.py'))
print(os.stat('os-sample.py').st_size)
mod_time = os.stat('os-sample.py').st_mtime
print(datetime.fromtimestamp(mod_time))

# Tree Directory
"""
for dirpath,dirnames,filenames in os.walk('/Users/user/Desktop/Projects/PY'):
    print('Current Path:',dirpath)
    print('Dirs :', dirnames)
    print('Files',filenames)
    print()
"""
# print(os.environ)
print(os.environ.get('ALLUSERSPROFILE'))
file_path = os.path.join(os.environ.get('ALLUSERSPROFILE'),'text.txt')
print(file_path)

print(os.path.basename('tmp/test.txt'))
print(os.path.dirname('tmp/test.txt'))
print(os.path.split('tmp/test.txt'))
print(os.path.exists('tmp/test.txt'))
print(os.path.isdir('tmp/test.txt'))
print(os.path.isfile('tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))