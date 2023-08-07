import ttkbootstrap as tb
from tkinter import *

def scaler(e):
    label.config(text=f'{int(slider.get())}%')

root = tb.Window(themename="cerculean")
root.geometry("500x350")
root.title("Sliders")

slider = tb.Scale(root, bootstyle="info",
                  length=200,
                  from_=0,
                  to=100,
                  orient="horizontal",
                  command=scaler)
slider.pack(pady=20)

label = tb.Label(font=("Helvetica", 14))
label.pack(pady=20)

root.mainloop()
