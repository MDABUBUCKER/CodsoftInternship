from tkinter import *
from tkinter import messagebox  #importing messagebox package

def addtask():
    task_values = input1.get()
    if task_values != "":
        tasks.insert(END,task_values)
        input1.delete(0,"end")
    else:
        messagebox.showwarning("Reminding","Enter Some Task")

def deletetask():
    tasks.delete(ANCHOR)


todo = Tk()
todo.geometry("400x450")
todo.title("Todo List")
todo.resizable(width = False,height=False)
perfect_frame = Frame(todo)
perfect_frame.pack(pady = 10)

input1 = Entry(todo,width = 28,font=("times",15))
input1.pack(pady = 20)

tasks = Listbox(perfect_frame,width = 25,height = 8,font = ("times",20))
tasks.pack(side = LEFT,fill = BOTH)

task_list = []  #storing tasks in list

for value in task_list:
    tasks.insert(END,value)


button1 = Button(todo,text = "Add Task",font = ("times",14),bg = "green",fg = "white",command = addtask)
button1.pack()

button2 = Button(todo,text = "Delete Task",font = ("times",14),bg = "red",fg = "white",command = deletetask)
button2.pack(pady = 17)

todo.mainloop()

#design by Abubucker