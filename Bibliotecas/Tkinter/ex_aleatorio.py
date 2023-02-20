from tkinter import *

janela = Tk()

def clicked(value):
    label = Label(janela, text=f"você escolheu a pizza: {value}")
    label.pack()

opcoes = [
    ("pepperone", "pepperone"),
    ("frango com catupiry", "frango com catupiry"),
    ("mista", "mista"),
    ("margherita", "margherita")
]

pizza = StringVar()
pizza.set(None)

for tipo_pizza, sabor_pizza in opcoes:
    Radiobutton(janela, text=tipo_pizza, variable=pizza, value=sabor_pizza).pack(anchor=W)


btn = Button(janela, text='aceitar', command= lambda: clicked(pizza.get())).pack()

janela. mainloop()