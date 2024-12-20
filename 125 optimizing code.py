def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

while True:
    user_action=input("type add ,show,edit,complete,or exit")
    user_action=user_action.strip()

    if  user_action.startswith("add"):
        todo = user_action[4:]
        todos=get_todos("todos.txt")
        todos.append(todo+'\n')

        write_todos(todos)


    elif  user_action.startswith("show"):
        todos=get_todos("todos.txt")

        for index,item in enumerate(todos):
               item=item.strip("\n")
               row=f"{index+1}.{item}"
               print(row)

    elif user_action.startswith("edit"):
        try:

             number=int(user_action[5:])
             print(number)
             number=number -1

             todos=get_todos("todos.txt")

             new_todo=input("enter the new todo")
             todos[number]=new_todo + '\n'

             write_todos( todos)

        except ValueError:
             print("your command is not valid")


    elif  user_action.startswith("complete"):
        try:
             number=int(user_action[9:])

             todos=get_todos("todos.txt")
             index=number-1
             todo_to_remove=todos[index]
             todos.pop(index)

             write_todos(todos)

             message=f"todo{todo_to_remove}was removed from the list"
             print(message)

        except IndexError:
             print("there is no item with that no")
             continue
    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")
