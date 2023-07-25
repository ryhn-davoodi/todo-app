import function
import time
now=time.strftime("%d-%m-%Y  %H:%M:%S")
print("now:",now)
while True:
   user_action = input("type add,show,edit,delete or exit: ")
   user_action = user_action.strip()

   if user_action.startswith("add"):
      todos = function.get_todos()
      todo = user_action[4:]+"\n"
      todos.append(todo)
      function.write_todos(todos)


   elif user_action.startswith("show"):
      todos = function.get_todos()
      todos = [todoo.strip("\n") for todoo in todos]
      for index,item in enumerate(todos):
         print(f"{index+1}-{item}")


   elif user_action.startswith("edit"):
      try:
         todos = function.get_todos()
         number = user_action[5:]
         todo = input("enter your new todo") +"\n"
         number = int(number)-1
         item_to_remove = todos[number]
         item_to_remove = item_to_remove.strip("\n")
         todos[number] = todo
         function.write_todos(todos)
         print(f"{item_to_remove} has been changed successfuly!")
      except ValueError:
         print("unknown string!")
         continue

   elif user_action.startswith("delete"):
      try:
         todos = function.get_todos()

         num = int(user_action[7:])
         num = num-1
         removed_item = todos[num]
         removed_item = removed_item.strip("\n")
         todos.pop(num)
         function.write_todos(todos)
         print(f"{removed_item} has been removed successfully")
      except ValueError:
         print("after delete enter number of todo you want to delete")
         continue

   elif "exit" in user_action:
      break
print("bye!")