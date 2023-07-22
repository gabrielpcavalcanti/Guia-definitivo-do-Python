# Date entry

É um widget que motra um calendário onde vc pode 
escolher datas.

```Python
from tkinter import *
import ttkbootstrap as tb
from datetime import date

def clicker():
    label.config(text=f"You Picked: {date.entry.get()}")

root = tb.Window(themename="vapor")

root.title("Date entry")
root.geometry("500x350")

date =tb.DateEntry(root, bootstyle="danger", startdate=date(2023,5,14),
                   firstweekday=0)
date.pack(pady=50)

button = tb.Button(root, text="Get date", bootstyle="danger outline",
                   command=clicker)
button.pack(pady=20)

label = tb.Label(root, text="You Picked: ")
label.pack(pady=20)

root.mainloop()

```

A outro modo tmb, que em vez de aparecer o widget, vc faz ele aparecer atravez de um botão.

```Python
from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

def clicker():
    cal = Querybox()
    label.config(text=f"You Picked: {cal.get_date()}")

root = tb.Window(themename="vapor")

root.title("Date entry")
root.geometry("500x350")

button = tb.Button(root, text="Get Calendar", bootstyle="danger outline",
                   command=clicker)
button.pack(pady=20)

label = tb.Label(root, text="You Picked: ")
label.pack(pady=20)

root.mainloop()

```
