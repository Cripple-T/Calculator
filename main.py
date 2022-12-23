from ast import Expression
import tkinter
from turtle import width

root = tkinter.Tk()
root.title("Calculator")

calculation = ""

# Functions
def add(value):
    global calculation 
    calculation += value
    label_awnser.config(text=calculation)

def clear():
    global calculation
    calculation = ""
    label_awnser.config(text="0")

def calculate():
    global calculation
    awnser = ""
    if calculation !="":
        try:
            awnser = eval(calculation)
        except:
            awnser = "error"
            calculation = ""
    label_awnser.config(text=awnser)


# GUI
label_awnser = tkinter.Label(root, padx=30,text="0", font=('arial', 20, 'bold'))
label_awnser.grid(row=0, column=0, columnspan=4)

button_7 = tkinter.Button(root, padx=30,text="7", font=('arial', 20, 'bold'), command=lambda: add("7"))
button_7.grid(row=1, column=0)

button_8 = tkinter.Button(root, padx=30,text="8", font=('arial', 20, 'bold'), command=lambda: add("8"))
button_8.grid(row=1, column=1)

button_9 = tkinter.Button(root, padx=30,text="9", font=('arial', 20, 'bold'), command=lambda: add("9"))
button_9.grid(row=1, column=2)

button_4 = tkinter.Button(root, padx=30,text="4", font=('arial', 20, 'bold'), command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, padx=30,text="5", font=('arial', 20, 'bold'), command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, padx=30,text="6", font=('arial', 20, 'bold'), command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_1 = tkinter.Button(root, padx=30,text="1", font=('arial', 20, 'bold'), command=lambda: add("1"))
button_1.grid(row=3, column=0)

button_2 = tkinter.Button(root, padx=30,text="2", font=('arial', 20, 'bold'), command=lambda: add("2"))
button_2.grid(row=3, column=1)

button_3 = tkinter.Button(root, padx=30,text="3", font=('arial', 20, 'bold'), command=lambda: add("3"))
button_3.grid(row=3, column=2)

button_C = tkinter.Button(root, padx=30,text="c", font=('arial', 20, 'bold'), command=lambda: clear())
button_C.grid(row=4, column=0)

button_0 = tkinter.Button(root, padx=30,text="0", font=('arial', 20, 'bold'), command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, padx=31.5,text=".", font=('arial', 20, 'bold'), command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_plus = tkinter.Button(root, padx=30,text="+", font=('arial', 20, 'bold'), command=lambda: add("+"))
button_plus.grid(row=1, column=3)

button_minus = tkinter.Button(root, padx=30,text="-", font=('arial', 20, 'bold'), command=lambda: add("-"))
button_minus.grid(row=2, column=3)

button_multiply = tkinter.Button(root, padx=30,text="*", font=('arial', 20, 'bold'), command=lambda: add("*"))
button_multiply.grid(row=3, column=3)

button_divide = tkinter.Button(root, padx=30,text="/", font=('arial', 20, 'bold'), command=lambda: add("/"))
button_divide.grid(row=4, column=3)

button_equal = tkinter.Button(root, padx=30,text="=", font=('arial', 20, 'bold'), width=19, command=lambda: calculate())
button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()