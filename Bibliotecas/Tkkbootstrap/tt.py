import ttkbootstrap as tb
from tkinter import *

root = tb.Window(themename="superhero")

root.title("Testes")
root.geometry("500x350")

btn1 = tb.Button(text="click here", bootstyle="success", state="disable")
btn1.pack(pady=20)

style2 = tb.Style()
style2.configure('success.Outline.TButton', font=("Helvetica, 6"), bootstyle="success outline")

button = tb.Button(text="Hello World",  
                bootstyle='success',
                style="success.Outline.TButton",
                width=20)
button.pack(pady=40)

var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info, round-toggle",
    text="round toggle",
    variable=var1,
    onvalue=1,
    offvalue=0,
    )

check.pack()

root.mainloop()