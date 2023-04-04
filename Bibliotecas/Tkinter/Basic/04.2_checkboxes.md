# Checkboxes

São aquelas caixinhas de selação. Vamos ver do que elas são capazes.

```Python
from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

def show():
    mylabel = Label(root, text=var.get()).pack()


var = StringVar()

check = Checkbutton(root, text="Checkboxes", variable=var, onvalue="check", offvalue="Offcheck")
check.deselect()
check.pack()

btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
```
