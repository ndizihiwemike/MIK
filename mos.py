import os
import shutil

current = os.getcwd()
print(current)
# craetion of path
new_path = os.path.join(current,"newfolder")
print(new_path)


#check whether the specified
#specify path
path = '/usr/local/bin/'
#path exist or not
isExist = os.path.exists(path)
print(isExist)
#creation of folders

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(e)

try:
#second method
 directory = "movies"
 parent_dir = current
 path = os.path.join(parent_dir, directory)
 os.makedirs(path)
 os.makedirs("audio")
 print("directory '%s'{directory}' created"  )
except FileExistsError as e:
        print(e)

#change directory
os.chdir("newfolder")
print(os.getcwd())
os.chdir("..")
#listing directory contents
directory_content = os.listdir()
print(directory_content)
#checking whether a given path is a folder or a file
pa = os.path.join(os.getcwd(), "classes.py")
print(os.path.isfile(pa))
#check dir
print(os.path.isdir(pa))
#file size
print(os.path.getsize(pa))
#return size
destination = os.path.join(current, "newfolder")

shutil.copy2(pa, destination)
os.chdir("newfolder")
#os.remove("classes.py")
#os.unlink(os.path.join(destination, "classes.py"))

shutil.rmtree("newfolder")

