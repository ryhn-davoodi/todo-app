import  function
import PySimpleGUI as sg


lable=sg.Text('enter a todo:')
input_Box=sg.InputText()
button=sg.Button("Add")
window=sg.Window('to do app',layout=[[lable],[input_Box,button]])
window.read()
window.close()