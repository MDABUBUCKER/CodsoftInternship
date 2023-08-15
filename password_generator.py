from tkinter import *
import random  #importing random

generator = Tk()
generator.title("Password Generator")
generator.geometry("400x350")

def code():
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small =  "abcdefghijklmnopqrstuvwxyz"
    number = "1234567890"
    symbols = "@#$%&*+-!"

    #password generator code
    all = capital + small + number + symbols
    first_value = input1.get()
    input2.insert(0, random.sample(all, int(first_value)))

def clear():
    input1.delete(0,END)
    input2.delete(0,END)

title_one = Label(generator, text="Password Generator", font=("times", 14, "bold")).pack()

title_two = Label(generator, text="Enter Length Of Password", font=("times", 12, "bold")).pack(pady=20)

input1 = Entry(generator, width=30)
input1.pack()

title_three = Label(generator, text="Your password", font=("times", 12, "bold")).pack(pady=20)

input2 = Entry(generator, width=30)
input2.pack()

button1 = Button(generator, text="Generate", command=code, font=("times", 12, "bold")).pack(pady=20)
button2 = Button(generator, text="Clear", command=clear, font=("times", 12, "bold")).pack(padx=90)

generator.mainloop() #mainloop

#design by Abubucker