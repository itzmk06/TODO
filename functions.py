FILEPATH="todos.txt"
def get_todo(filepath=FILEPATH):
        """gets the todo items from the todos.txt"""
        with open(filepath,"r") as file:
            tasks=file.readlines()
        return tasks
def write_todo(todo_args,filepath=FILEPATH):
     """ writes the todo items to the todos.txt """
     with open(filepath,"w") as file:
        file.writelines(todo_args)

#if some statements are written in this file and when we imported this file into another file
#that parent file will run all the statements of this file so to avoid this we can use below code
#which will gets executed only when this current file is executed directly and not by imported files

if __name__=="__main__":
     print("Hello Manoj!")
