

import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass

sg.theme("BlackMono")
clock=sg.Text(' ',key='clock')

label=sg.Text("Type in a todo")
input_box =sg.InputText(tooltip="Enter Todo",key="todo")
add_button=sg.Button("add",tooltip="add todo")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True,
                      size=(45,10))
edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")
window=sg.Window("My Todo App",
                 layout=[[clock],
                         [label],
                         [input_box,add_button],
                         [list_box,edit_button,complete_button],
                         [exit_button]],
                font=('Helvetica',20))
while True:
    event,values =window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case"add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case"edit":
            try:
                todo_edit=values['todos'][0]
                new_todo = values['todo'].strip()
                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo +"\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("please select the item first")
        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError:
                sg.popup("please select the item first")

        case "exit":
              break
        case'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()