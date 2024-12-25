import glob
import FreeSimpleGUI
myfiles=glob.glob("filess/*.txt")

for filepath in myfiles:
    with open(filepath,'r') as file:

       print(file.read())
       print("hello")