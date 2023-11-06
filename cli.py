#this is the first commit
from functions import get_todo,write_todo
import os

if os.path.exists("todos.txt")!=True:
    with open("todos.txt","w") as file:
        pass
prompt="Enter | add {task} | show | edit {pos} | complete {pos} | clear | exit: "
while True:
    user_action=input(prompt).strip().lower()
    if  user_action.startswith("add"):
        todos=get_todo()
        todos.append((user_action[4:]).capitalize()+'\n')
        write_todo(todo_args=todos)
    elif user_action.startswith("show"):
        todos=get_todo()
        if len(todos)>=1:
                for index,task in enumerate(todos):
                    task=task.strip("\n")
                    print(f"{index+1}.{task}")
        else:
            print("There are no tasks to do!")
    elif  user_action.startswith("edit"):
        try:
            todos=get_todo()
            for index,task in enumerate(todos):
                    task=task.strip("\n")
                    print(f"{index+1}.{task}")
            index=int(user_action[5:])
            todos[index-1]=(input("Enter new todo:")+'\n').capitalize()
            write_todo(todo_args=todos)
        except ValueError:
             print("you have to pass numbers not text!")
    elif  user_action.startswith("complete"):
        try:
            todos=get_todo()
            if len(todos)>=1:
                pos=int(user_action[9:])
                todos.remove(todos[pos-1])
                write_todo(todo_args=todos)    
            else:
                print("There are no tasks to do!")     
        except IndexError:
             print(f"There is no number in the position {pos}")
    elif user_action.startswith("clear"):
                 with open("todos.txt","w")as file:
                    file.write("")
    elif  user_action.startswith("exit"):
        print("GoodBye!")
        break 
    else:
         print("Invalid command entered!")                 


            


