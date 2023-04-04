# Creat new Windows

Podemos abrir mais de uma janela com o Tkinter, ou abir uma nova janela atravez
de um comando. Utilizamos o método Toplevel( ) para executar essas tarefas.

```Python
from tkinter import *

root = Tk()
root.title("New Window")

new_win = Toplevel()
new_win.title("new New Window")

mainloop()
```

Lembrando que podemos abrir quantas janelas quisermos, apenas indique ao programa que faça isso.

```Python
from tkinter import *

root = Tk()
root.title("New Window")

def open():
    new_win = Toplevel()
    new_win.title("Second Window")

btn = Button(root, text="Open Second window", command=open).pack()

mainloop()
```
