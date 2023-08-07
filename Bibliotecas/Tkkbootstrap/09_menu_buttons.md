# Menu Buttons

É um menu de que vc escolhe várias opções e todas elas são botões. É um pouco trablhoso fazer isso, mas o código abixo é um exemplo de funcionalidade.

```python
import ttkbootstrap as tb
from tkinter import *

def stuff(x):
    menu.config(bootstyle=x, text=x)
    label.config(text=f'you chose {x}')

root = tb.Window(themename='yeti')

root.title("Menu Buttons")
root.geometry("500x350")

menu = tb.Menubutton(root, bootstyle='warning', text='Things!') # Cria o botão menu
menu.pack(pady=50)

inside_menu = tb.Menu(menu) # Cria o menu do botão menu

item_var = StringVar() # define os botões internos do botão menu.
for x in ['primary', 'secondary', 'danger', 'info', 'primary outline', 'danger outline']:
    inside_menu.add_radiobutton(label=x, variable=item_var, command= lambda x=x: stuff(x)) # insere os botões internos e define o que ele vai fazer quando selecionado.

menu['menu'] = inside_menu # associa o botão menu aos botões internos.

label = tb.Label(root, bootstyle='success')
label.pack(pady=20)

root.mainloop()
```
