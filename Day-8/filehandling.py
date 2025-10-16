#______________WRITE FILE______________
# import os
# # file_path=r'C:\AIML\Day-8\FILE_PATH EXAMPLE'
# file_path=os.getcwd()
# # file_path='C:\\AIML\Day-8\\FILE_PATH EXAMPLE\\Asample.txt'  #can code this way w/o r''
# filename=input('Enter File Name to create:\t')
# fullpath=os.path.join(file_path,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file:\n')
# file.write(content)
# print(f"File {filename} create at '{fullpath}' and the content has been saved in the file")
# file.close()


#______________APPEND FILE______________
print('TOPIC:\tAPPEND FILE')
import os
# file_path=r'C:\AIML\Day-8\FILE_PATH EXAMPLE'
file_path=os.getcwd()
# file_path='C:\\AIML\Day-8\\FILE_PATH EXAMPLE\\Asample.txt'  #can code this way w/o r''
filename=input('Enter File Name to update:\t')
fullpath=os.path.join(file_path,filename)

file=open(fullpath,'a')     #here's the difference
content=input('Enter text to add in file:\n')
file.write(content)
print(f"File {filename} create at '{fullpath}' and the content has been updated in the file")
file.close()

#______________APPEND FILE + IF LOOP______________
print('TOPIC:\tAPPEND FILE IF ONLY FILE NAME EXISTED')
import os
# file_path=r'C:\AIML\Day-8\FILE_PATH EXAMPLE'
file_path=os.getcwd()
# file_path='C:\\AIML\Day-8\\FILE_PATH EXAMPLE\\Asample.txt'  #can code this way w/o r''
filename=input('Enter File Name to update:\t')
fullpath=os.path.join(file_path,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')     #here's the difference
    content=input('Enter text to add in file:\n')
    file.write(content)
    print(f"File {filename} create at '{fullpath}' and the content has been updated in the file")
    file.close()
else:
    print(f'No such file {filename} existed')