from tkinter import *  # imporat package
calculator = Tk()  # storing a packages in one variable

calculator.title("Calculator")

input1 = Entry(calculator,width = 55)
input1.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 10) #input code

def click(num):
    first_value = input1.get()
    input1.delete(0,END)
    input1.insert(0,str(first_value)+str(num))

def add():  #adding function
    firstno = input1.get()
    global sum
    sum = "addition"
    global adding1
    adding1 = int(firstno)
    input1.delete(0,END)

def subtract():  #subtract function
    firstno = input1.get()
    global sum
    sum = "subtraction"
    global adding1
    adding1 = int(firstno)
    input1.delete(0,END)

def multiply():  #multiply function
    firstno = input1.get()
    global sum
    sum = "multiplication"
    global adding1
    adding1 = int(firstno)
    input1.delete(0,END)

def divide():  #division function
    firstno = input1.get()
    global sum
    sum = "division"
    global adding1
    adding1 = int(firstno)
    input1.delete(0,END)

def clear():
    input1.delete(0,END)

def equal():    #equal function
    secondno = input1.get()
    adding2 = int(secondno)
    input1.delete(0,END)
    if sum == "addition":
        input1.insert(0,adding1+adding2)
    elif sum == "subtraction":
        input1.insert(0,adding1-adding2)
    elif sum == "multiplication":
        input1.insert(0,adding1*adding2)
    elif sum == "division":
        input1.insert(0,adding1/adding2)


value1 = Button(calculator,text = "7",padx = 40,pady = 15,command = lambda : click(7),fg = "white",bg= "black")
value1.grid(row = 1,column = 0)
value2 = Button(calculator,text = "8",padx = 40,pady = 15,command = lambda  : click(8),fg = "white",bg= "black")
value2.grid(row = 1,column = 1)
value3 = Button(calculator,text = "9",padx = 40,pady =15,command = lambda : click(9),fg = "white",bg= "black")
value3.grid(row = 1,column = 2)


value4 = Button(calculator,text = "4",padx = 40,pady = 15,command = lambda  : click(4),fg = "white",bg= "black")
value4.grid(row = 2,column = 0)
value5 = Button(calculator,text = "5",padx = 40,pady = 15,command = lambda  : click(5),fg = "white",bg= "black")
value5.grid(row = 2,column = 1)
value6 = Button(calculator,text = "6",padx = 40,pady = 15,command = lambda  : click(6),fg = "white",bg= "black")
value6.grid(row = 2,column = 2)


value7 = Button(calculator,text = "1",padx = 40,pady = 15,command = lambda  : click(1),fg = "white",bg= "black")
value7.grid(row = 3,column = 0)
value8 = Button(calculator,text = "2",padx = 40,pady = 15,command = lambda  : click(2),fg = "white",bg= "black")
value8.grid(row = 3,column = 1)
value9 = Button(calculator,text = "3",padx = 40,pady = 15,command = lambda : click(3),fg = "white",bg= "black")
value9.grid(row = 3,column = 2)


valueac = Button(calculator,text = "AC",padx = 35,pady = 15,command = clear,fg = "white",bg= "black")
valueac.grid(row = 4,column = 0)
value0 = Button(calculator,text = "0",padx = 40,pady = 15,command = lambda : click(0),fg = "white",bg= "black")
value0.grid(row = 4,column = 1)
equ = Button(calculator,text = "=",padx = 40,pady = 15,command  = equal,fg = "white",bg= "orange")
equ.grid(row = 4,column = 2)

#divide
divd = Button(calculator,text = "/",padx = 40,pady = 15,command = divide,fg = "black",bg= "white")
divd.grid(row = 1,column = 3)
#multiply
mul = Button(calculator,text = "*",padx = 40,pady = 15,command = multiply,fg = "black",bg= "white")
mul.grid(row = 2,column = 3)
#sub
sub = Button(calculator,text = "-",padx = 40,pady = 15,command = subtract,fg = "black",bg= "white")
sub.grid(row = 3,column = 3)
#add
add = Button(calculator,text = "+",padx = 40,pady = 15,command = add,fg = "black",bg= "white")
add.grid(row = 4,column = 3)

calculator.mainloop()  # creating mainloop function

#design by Abubucker