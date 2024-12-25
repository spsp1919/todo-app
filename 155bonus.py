
import FreeSimpleGUI as sg
from zipfilefunction import  make_archive
label1 =sg.Text("select files to compress")
input1 =sg.Input()

choose_button1 =sg.FilesBrowse("choose",key="files")
label2 =sg.Text("select destiantion folder")
input2 =sg.Input()

choose_button2 =sg.FolderBrowse("choose",key="folder")
compress_button =sg.Button("compress")

window =sg.Window("file compressor",layout=[[label1,input1,choose_button1],
                                          [label2,input2,choose_button2 ],[compress_button]])

while True:
    event,values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder=values["folder"]
    make_archive(filepaths,folder)

window.close()