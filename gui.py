import  function
import PySimpleGUI as sg
import  time
clock=sg.Text(time.strftime("%d-%m-%Y  %H:%M:%S"),key="clock")
lable=sg.Text('enter a todo:')
input_Box=sg.InputText(key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
delete_button=sg.Button("Delete")
exit_button=sg.Button("Exit")
list_box=sg.Listbox(values=function.get_todos(),key="todos",
                    enable_events=True,
                    size=[45,10])
window=sg.Window('to do app',layout=[[clock],[lable],
               [input_Box,add_button],
               [list_box,edit_button,delete_button],
                                     [exit_button]],
               font=['tahome',20])
while True:
    event,value=window.read(timeout=1000)
    window['clock'].update(time.strftime("%d-%m-%Y  %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case 'Add':
            todo_to_add=value['todo']
            if todo_to_add == '':
                sg.popup('please enter a todo first!!')
            else:
                todos=function.get_todos()
                new_todo=value['todo'] +"\n"
                todos.append(new_todo)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

        case "Edit":
            try:
                new_todo=value['todo'] +'\n'
                todo_to_edit=value['todos'][0]
                todos=function.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select an item first!!")
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Delete":
            try:
                todo_to_delete=value['todos'][0]
                todos=function.get_todos()
                todos.remove(todo_to_delete)
                function.write_todos(todos)
                window["todos"].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("please select an item first")
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()

