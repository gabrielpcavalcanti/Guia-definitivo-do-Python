# Message boxes

São aquelas mensagens de texto que aparecem na sua tela (toma até um susto). Eles podem ser de aviso, pergunta, erro e outros.

Para poder utilizar eles é preciso importar um modulo do próprio Tkinter chamado messagebox.

```Python
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message boxe")

def popup():
    messagebox.showinfo("This is my popup!", "POPUP")

Button(root, text="Popup", command=popup).pack()

mainloop()
```

Temos várias opções de message box: showinfo, showwarning, showerror, askquestion, askokcancel,askyesno. Teste cada uma para ver o que acontece.

Cada message box tem um ou mais botões. Cada um deles, quando clicados, retorna um valor diferente. Com esse valor podemos fazer qualquer coisa. Veja um exemplo simples abaixo.

```Python
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message boxe")

def popup():
    res = messagebox.showwarning("This is my popup!", "POPUP")

    if res == 1:
        Label(root, text=" You clicked Yes").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()
```