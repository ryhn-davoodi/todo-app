import  function
import PySimpleGUI as sg


lable=sg.Text('enter a todo:')
input_Box=sg.InputText(key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=function.get_todos(),key="todos",
                    enable_events=True,
                    size=[45,10])
window=sg.Window('to do app',layout=[[lable],
               [input_Box,add_button],
               [list_box,edit_button]],
               font=['tahome',20])
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos=function.get_todos()
            new_todo=value['todo'] +"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            new_todo=value['todo'] +'\n'
            todo_to_edit=value['todos'][0]
            todos=function.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()

