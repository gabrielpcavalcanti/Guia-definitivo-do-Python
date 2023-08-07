# Notebooks

É um widget que delimita um espaço na tela ond vc pode colocar outros widgets. Vc pode mudar o notebook atravez de abas. Vamos ver mais algumas coisas que da para fazer com ele. 

```Python
from tkinter import *
import ttkbootstrap as tb

def clicker():
    string = text.get("1.0","end-1c")
    label3.config(text=f'you wrote {string}')


root = tb.Window(themename="cerculean")
root.title("Notebooks")
root.geometry("700x550")

note = tb.Notebook(root, bootstyle='dark')
note.pack(pady=20)

tab1 = tb.Frame(note)
tab2 = tb.Frame(note)

label = tb.Label(tab1, text="label teste", font=("ariel", 18))
label.pack(pady=20)

label2 = tb.Label(tab2, text="label teste 2", font=("ariel", 12))
label2.pack(pady=20)

text = Text(tab1, width=70, height=10)
text.pack(pady=10, padx=10)

button = tb.Button(tab1, text="teste", bootstyle='warning', command=clicker)
button.pack(pady=20)

label3 = tb.Label(tab1, text="", font=("ariel", 12))
label3.pack(pady=20)

note.add(tab1, text="Tab 1")
note.add(tab2, text="Tab 2")

root.mainloop()
```
