from functions import get_todo, write_todo
import PySimpleGUI as psg
import os

if os.path.exists("todos.txt")!=True:
    with open("todos.txt","w") as file:
        pass
nord_theme = {
    "BACKGROUND": "#2E3440",
    "TEXT": "#A4DCFF",
    "INPUT": "#3B4252",
    "TEXT_INPUT": "#E5E9F0",
    "SCROLL": "#3B4252",
    "BUTTON": ("#A4DCFF", "#2E3440"),
    "PROGRESS": ("#E5E9F0", "#88C0D0"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}
psg.theme_add_new("Nord", nord_theme)
psg.theme("Nord")

logo_=[
        psg.Text("", size=(24, 1)),
        psg.Text("", size=(1, 1)),  
        psg.Image("logo.png"),
        psg.Text("", size=(5, 1))
    ]
def create_intro_layout():
    return [
        [
            psg.Image("applogo.png",key="applogo"),
        ],
        [
            psg.Text("© CraftNeuron2023", font=("Segoe Print", 10), justification="center", pad=(0, 20),text_color="#FF6C22")
        ],
    ]
def create_main_layout():
    text = psg.Text("What you wanna do today?", font=("Segoe Print", 14))
    take_input = psg.InputText(key="todo", font=("Comic Sans MS", 12))
    add_button = psg.Button(key="Add", image_source="add1.png")
    list_box = psg.Listbox(values=get_todo(), key="todos", size=(50, 10), enable_events=True, font=("Comic Sans MS", 12))
    edit_button = psg.Button(key="Edit", image_source="edit.png")
    complete_button = psg.Button(key="complete", image_source="green-check.png")
    clear_button = psg.Button(key="Clear", image_source="broom.png")

    main_content_layout = [
        [logo_],
        [text],
        [take_input, add_button],
        [list_box, edit_button],
        [complete_button, clear_button]
    ]
    return main_content_layout
intro_window = psg.Window("App", layout=create_intro_layout(), finalize=True)

intro_duration = 2000

event, values = intro_window.read(timeout=intro_duration)

intro_window.close()

window = psg.Window(title="TODO APP", layout=create_main_layout(), font=("comic sans ms", 10))

while True:
    event,values=window.read()
    match event:
        case "Add":
            if values["todo"]!="":
                todos=get_todo()
                todos.append((values["todo"]+'\n').capitalize())
                write_todo(todos)
                window["todos"].Update(todos)
                window["todo"].Update("")
            else:
                psg.popup("Please enter an item!",font=("Comic Sans ms",10))

        case "Edit":
            try:                  
                todo_to_edit=values["todos"][0]
                new_todo=values["todo"]
                todos=get_todo()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo+'\n'
                write_todo(todos)
                window["todos"].Update(todos)
                window["todo"].Update("")
            except IndexError:
                psg.popup("Please select an item!",font=("Comic Sans ms",10))
        case "complete":
            try:            
                todo_to_remove=values["todos"][0]
                todos=get_todo()
                todos.remove(todo_to_remove)
                write_todo(todos)
                window["todos"].Update(todos)
                window["todo"].Update("")
            except IndexError:
                psg.popup("Please select an item!",font=("Comic Sans ms",10))
        case "Clear":
            todos=get_todo()
            todos.clear()
            write_todo(todos)
            window["todos"].Update(todos)
        case "todos":    
            window["todo"].Update((values["todos"][0]).strip('\n'))
        case psg.WIN_CLOSED:
            break
        case _:
            window["todo"].Update("")
window.close()



