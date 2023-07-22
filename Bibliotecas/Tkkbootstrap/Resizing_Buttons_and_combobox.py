from tkinter import *
import ttkbootstrap as tb

def clicker():

    label.config(text=f"You clicked on {combo_box.get()}!")

def click_bind(e):

    label.config(text=f"You clicked on {combo_box.get()}!")

    if combo_box.get() == "Select the option":
        label.config(text="Hello World!")


root = tb.Window(themename='cosmo')

root.title("Resizing Buttons and combo box")
root.geometry("500x350")

label = tb.Label(root, text="Hello World", font=("Helvetica", 18))
label.pack(pady=30)

days = ["Select the option", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

combo_box = tb.Combobox(root, bootstyle="default", values=days)
combo_box.pack(pady=20)

combo_box.current(0)

button = tb.Button(root, text="Click me", command=clicker, bootstyle="danger")
button.pack(pady=20)

combo_box.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
