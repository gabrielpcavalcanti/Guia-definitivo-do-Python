from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="vapor")
root.title("Spinboxes")
root.geometry("500x350")

def sppiny():
    label.config(text=spin.get())


stuff = ["Monday", "Tuesday", "Wenesday", "Thursday", "Friday","Saturday", "Sunday"]

spin = tb.Spinbox(root, bootstyle="success", font=("Helvetiva", 18),
                  from_=0, to=10, values=stuff, state="readonly", command=sppiny)
spin.pack(pady=20)

spin.set(stuff[0])

button = tb.Button(root, text="click me", bootstyle="success", command=sppiny)
button.pack(pady=20)

label = tb.Label(root, text="", font=("Helvetica", 18))
label.pack(pady=20)

root.mainloop()
