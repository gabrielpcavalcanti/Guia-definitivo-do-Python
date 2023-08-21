# Separators and sizegrips

Separators é uma linha que divide duas partes dentro da tela e o sizegrips é 
um negocinho no canto inferior que vc puxa e empurra para aumentar ou diminuir a tela. 

```Python
from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="darkly")
root.title("Separators and sizegrips")
root.geometry("500x350")

label1 = tb.Label(root, text="Label 1", bootstyle="light")
label1.pack(pady=40)

sep = tb.Separator(root, bootstyle="danger", orient="horizontal")
sep.pack(fill="x", padx=100)

label2 = tb.Label(root, text="Label 2", bootstyle="light")
label2.pack(pady=40)

sizegrip = tb.Sizegrip(root, bootstyle="info")
sizegrip.pack(anchor="se", fill="both", expand=True)

root.mainloop()

```
