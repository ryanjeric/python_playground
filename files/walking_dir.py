import os,shutil

for folderName,subfolders,filenames in os.walk('c:\\ryan-sample'):
    print('The Folder is '+ folderName)
    print('The Subfolders in ' + folderName + ' are ' + str(subfolders))
    print('The Filenames in ' + folderName + ' are ' + str(filenames))
    print()

    for subfolder in subfolders:
        #os.unlink(subfolder)
        if 'deleteDir'==subfolder:
            print('RMDIR On: '+ subfolder)
            #os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.txtz'):
            shutil.copy(os.path.join(folderName,file),os.path.join(folderName,file+'.backup'))