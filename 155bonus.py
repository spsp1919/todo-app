

import FreeSimpleGUI as sg
label1 =sg.Text("select files to compress")
input1 =sg.Input()
choose_button1 =sg.FilesBrowse("choose")
label2 =sg.Text("select destiantion folder")
input2 =sg.Input()
choose_button2 =sg.FolderBrowse("choose")
compress_button =sg.Button("compress")

window =sg.Window("file compressor",layout=[[label1,input1,choose_button1],
                                          [label2,input2,choose_button2 ],[compress_button]])
window.read()
window.close()