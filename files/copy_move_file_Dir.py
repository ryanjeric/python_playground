import shutil,os

# copy
shutil.copy('c:\\ryan-sample\\hello.txt','c:\\ryan-sample\\test\\hellohello.txt')
if not os.path.isdir('c:\\ryan-sampleBK'):
    shutil.copytree('c:\\ryan-sample','c:\\ryan-sampleBK') # COPY ALL

# move
#shutil.move('bacon.txt','c:\\ryan-sample')
# Rename
shutil.move('bacon.txt','bacon_renamed.txt')