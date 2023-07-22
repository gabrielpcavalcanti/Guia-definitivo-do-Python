import ttkbootstrap as tb
from ttkbootstrap.constants import *

counter = 0
def changer():
    global counter
    counter += 1

    if counter % 2 == 0:
        label.config(text="Hello World!")
    else:
        label.config(text="Goodbye World!")



root = tb.Window(themename="cyborg")
root.title("TTK Bootstrap!")
root.iconbitmap("Bibliotecas\Tkinter\potatos.ico")
root.geometry("500x350")

label = tb.Label(text='Pão tostado', font=('Helvectica',28), bootstyle='info')
bbt = tb.Button(text='Click me', bootstyle='Light, outline', command=changer)

label.pack(pady=50)
bbt.pack(pady=20)

root.mainloop()