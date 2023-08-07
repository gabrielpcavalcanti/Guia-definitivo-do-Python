import ttkbootstrap as tb
from tkinter import *

def stuff(x):
    menu.config(bootstyle=x)
    label.config(text=f'you chose {x}')

root = tb.Window(themename='yeti')

root.title("Menu Buttons")
root.geometry("500x350")

menu = tb.Menubutton(root, bootstyle='warning', text='Things!')
menu.pack(pady=50)

inside_menu = tb.Menu(menu)

item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'primary outline', 'danger outline']:
    inside_menu.add_radiobutton(label=x, variable=item_var, command= lambda x=x: stuff(x))

menu['menu'] = inside_menu

label = tb.Label(root, bootstyle='success')
label.pack(pady=20)

root.mainloop()