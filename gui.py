import  function
import PySimpleGUI as sg


lable=sg.Text('enter a todo:')
input_Box=sg.InputText(key="todo")
add_button=sg.Button("Add")
window=sg.Window('to do app',layout=[[lable],[input_Box,add_button]],
                 font=['tahome',20])
while True:
    event,value=window.read()
    print(type(event))
    print(value)
    match event:
        case 'Add':
            todos=function.get_todos()
            new_todo=value['todo'] +"\n"
            todos.append(new_todo)
            function.write_todos(todos)
window.close()

