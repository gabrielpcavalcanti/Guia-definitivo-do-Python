from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

def clicker():
    cal = Querybox()
    label.config(text=f"You Picked: {cal.get_date()}")

root = tb.Window(themename="vapor")

root.title("Date entry")
root.geometry("500x350")

button = tb.Button(root, text="Get Calendar", bootstyle="danger outline",
                   command=clicker)
button.pack(pady=20)

label = tb.Label(root, text="You Picked: ")
label.pack(pady=20)

root.mainloop()