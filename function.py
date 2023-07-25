def get_todos(filepath="todos.txt"):
   """read the text file and return the list of todos """
   with open(filepath,"r") as file:
      todos=file.readlines()
   return todos

def write_todos(local_todos,filepath="todos.txt"):
   """write the todo item list in the text file"""
   with open(filepath,"w") as file:
      file.writelines(local_todos)

if __name__=="__main__":
   print("this is a test from function file!")