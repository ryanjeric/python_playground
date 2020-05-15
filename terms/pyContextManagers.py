"""
Context Managers are great for when we need to setup or
teardown some resources during use. So these can be used for:
open and closing files, opening and closing database connections,
acquiring and releasing locks, and much much more
"""
import os
from contextlib import contextmanager

class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'w') as f:  # f = __enter__
    f.write('Testing')
# __exit__
print(f.closed)


## 2nd sample
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample2.txt', 'w') as f:
    f.write('Testing 2')

print(f.closed)

## 3rd sample
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
