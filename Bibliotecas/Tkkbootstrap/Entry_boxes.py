from tkinter import *
import ttkbootstrap as tb

def speak():

    label.config(text=f"You Typed: {entry.get()}")

root = tb.Window(themename="solar")

root.title("Entry boxes")
root.geometry("500x350")

entry = tb.Entry(root, bootstyle="success", font=("Helvetica", 18), foreground="blue",
            width=15, show="*")
entry.pack(pady=50)

button = tb.Button(root, text="Click me", bootstyle=" dange outline", command=speak)
button.pack(pady=20)

label = tb.Label(root, text="")
label.pack(pady=20)

root.mainloop()
