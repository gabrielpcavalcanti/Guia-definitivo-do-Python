# Dropdown Menus

Como o própio nome diz, é um menu de seleção. Utilizamos a classe OptionMenu( ) para fazer isso, veja abaixo.

```Python
from tkinter import *

root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

clicked = StringVar()
clicked.set("Make a choice")

drop = OptionMenu(root, clicked, "op1", "op2", "op3", "op4", "op5", "op6")
drop.pack()

root.mainloop()
```

Agora podemos fazer alguams alterações para deixa o código melhor e definir o que acontece caso uma opção seja escolhida, veja abaixo.

```Python
from tkinter import *

def show():
    my_label = Label(root, text=clicked.get()).pack()

root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

list_opt  =["op1", "op2", "op3", "op4", "op5", "op6"]

clicked = StringVar()
clicked.set("Make a choice")

drop = OptionMenu(root, clicked, *list_opt)
drop.pack()

btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
```