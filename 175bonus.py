
import FreeSimpleGUI as sg

from zipfile_extractor import extract_archive

sg.theme("BlackMono")

label1 =sg.Text("select files to archive")
input1 =sg.Input()

choose_button1 =sg.FilesBrowse("choose",key="archive")
label2 =sg.Text("select destiantion folder")
input2 =sg.Input()

choose_button2 =sg.FolderBrowse("choose",key="folder")
extract_button = sg.Button("Extract")
output_label = sg.Text(key='output',text_color='green')

window =sg.Window("archive extractor",layout=[[label1,input1,choose_button1],
                                                  [label2,input2,choose_button2 ],
                                                   [extract_button,output_label]])

while True:
    event,values = window.read()
    print(event,values)
    archive_path = values['archive']
    des_dir = values['folder']
    extract_archive(archive_path,des_dir)

window.close()