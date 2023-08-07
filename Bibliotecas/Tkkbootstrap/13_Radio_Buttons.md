# Radio Button

Tem algumas maneiras de criar Radio Buttons, veja a seguir. 

A primeira maneira é atraz de loops.

```Python
import ttkbootstrap as tb
import tkinter

def clicker():
    label.config(text=f"Vc escolheu {topp.get()}")


root = tb.Window(themename="superhero")
root.geometry("500x350")
root.title("Radio Buttons")

toppings = ["pepperoni", "frango com catupiry", "portuguesa"]

topp = tkinter.StringVar()

for topping in toppings:
    tb.Radiobutton(root, bootstyle="success", variable=topp ,text=topping, value=topping, command=clicker).pack(pady=20)

label = tb.Label()
label.pack(pady=20)

root.mainloop()

```

A segunda forma é diretamente, mais simples e rápido.

```Python
def clicker():
    label.config(text=f"Vc clicou em {topp.get()}")

root = tb.Window(themename="superhero")
root.geometry("500x350")
root.title("Radio Buttons")

topp = tkinter.StringVar()

rb1 = tb.Radiobutton(root, bootstyle="danger toolbutton", variable=topp, text="Radio Button 1", value="Radio Button 1", command=clicker)
rb1.pack(pady=20)

rb2 = tb.Radiobutton(root, bootstyle="info toolbutton outline", variable=topp, text="Radio Button 2", value="Radio Button 2", command=clicker)
rb2.pack(pady=20)

label = tb.Label(text="Selecione um botão")
label.pack(pady=20)


root.mainloop()

```
