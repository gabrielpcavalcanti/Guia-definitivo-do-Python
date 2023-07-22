import ttkbootstrap as tb
from tkinter import *

def checker():
    
    if var1.get() == 1:
        Label2.config(text="Checked!")
    else:
        Label2.config(text="Unchecked!")


root = tb.Window(themename="cyborg")

root.title("Checkbox")
root.geometry("500x350")

#Label
Label = tb.Label(text="Click the checkbutton below",
                 font=("Helvetica",18))

Label.pack(pady=5)

Label2 = tb.Label(text="teste",
                 font=("Helvetica",18))



#CheckButton

var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="Light",
    text="Check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

var2 = IntVar()
check2 = tb.Checkbutton(
    bootstyle="Default, toolbutton",
    text="ToolButton",
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=checker)

var3 = IntVar()
check3 = tb.Checkbutton(
    bootstyle="info, toolbutton, outline",
    text="outline toolbutton",
    variable=var3,
    onvalue=1,
    offvalue=0,
    command=checker)

var4 = IntVar()
check4 = tb.Checkbutton(
    bootstyle="success, round-toggle",
    text="round toggle",
    variable=var4,
    onvalue=1,
    offvalue=0,
    command=checker)

var5 = IntVar()
check5 = tb.Checkbutton(
    bootstyle="warning, square-toggle",
    text="square toggle",
    variable=var5,
    onvalue=1,
    offvalue=0,
    command=checker)


check.pack(pady=5)
check2.pack(pady=5)
check3.pack(pady=5)
check4.pack(pady=5)
check5.pack(pady=5)

Label2.pack(pady=5)

root.mainloop()