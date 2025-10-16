#___________________________________CHECK CURRENT DIRECTORY
# import os
# import inspect

# print('Current Directory',os.getcwd())

# functions=inspect.getmembers(os,inspect.isbuiltin)
# print('All function in OS Module')
# for n,func in functions:
#     print(n)


#_______________________________CREATE FOLDER INSIDE CURRENT DIRECTORY USING PYTHON
import os
cdir=os.getcwd()
folder_name=input('Enter Folder Name to create:\t')
folder_path=os.path.join(cdir,folder_name)
if(os.path.exists(folder_path)):
    print('Folder already exist')

else:
    os.makedirs(folder_path,exist_ok=True)
    print(f'{folder_name} created at {folder_path}')

#_______________________TASK_____________________________________________
#RENAME A FOLDER
#   os.rename(folder_name,'renamed_folder')
# write code to rename a folder
# you will take folderName from user
# if it is exist, you will ask new name and rename it

import os
cdir=os.getcwd()
oldFolder=input('Enter the folder name to rename:\t')
renameFolder=input('Rename the folder:\t')
oldfolder_path=os.path.join(cdir,oldFolder)
newfolder_path=os.path.join(cdir,renameFolder)

if(os.path.exists(oldfolder_path)):
    os.rename(oldfolder_path, newfolder_path)
    print(f'{oldFolder} Folder renamed to {renameFolder}')
else:
    print(f'{oldFolder} folder does not exist!')
#___uphere: first you create the folder, then you rename the same folder