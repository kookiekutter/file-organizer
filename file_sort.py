import os, shutil
import re

path = r"C:\Users\SAMHITHA\Documents\aDAs"
files=os.listdir(path)
print(files)


### CREATING A DIRECTORY
# npdfs=r"C:\Users\SAMHITHA\Documents\aDAs\pdfs"
# os.mkdir(npdfs)
# files2=os.listdir(npdfs)
# print(files2) 
#  -----
# ndocx=f'{path}\docxfile'
# os.mkdir(ndocx)

# txt="cd 1.pdf"
# k= re.split("\.",txt)
# print(k)

# print(files[0])
# cur_dir=os.getcwd()
# print(cur_dir)

# existing=f'{cur_dir}\{files[0]}'
# new_dir=f'{cur_dir}\pdfs\{files[0]}'
# print(existing)
# print(new_dir)

# shutil.move(existing,new_dir)
# print("successful")

for file in files:
    k=re.split("\.",file)
    epath=f'{path}\{file}'

    if k[len(k)-1]=="pdf":
        newpath=f'{path}\pdfs\{file}'
        shutil.move(epath,newpath)
        print(epath)
        print(newpath)

    elif k[len(k)-1]=='docx':
        newpath=f'{path}\docxfile\{file}'
        shutil.move(epath,newpath)
        print(epath)
        print(newpath)

    k=''


#CURRENT DIRECTORY
# cur_dir = os.getcwd()
# print(cur_dir)