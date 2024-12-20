

todos=[]

while True:
    user=input("type add ,show,edit,or exit")
    user=user.strip()
    match user:
        case'add':
            todo=input("enter a todo")
            todos.append(todo)
        case 'show':
               for index,item in enumerate(todos):
                   row=f"{index}.{item}"
                   print(row)
        case 'edit':
            number=int(input("number of todo you want to edit"))
            number=number -1
            newtodo=input("enter the new todo")
            todos[number]=newtodo

        case 'exit':
            break
