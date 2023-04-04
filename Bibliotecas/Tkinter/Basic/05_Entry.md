# Entry

É um outro widget existente na biblioteca tkinte. Como o nome indica ele possui a função de entrada de dados do usuário, como a função input() no Python.

``` Python
from tkinter import *

janela = Tk()

entrada = Entry(janela)
entrada.grid()

janela.mainloop()
```

temos alguns parâmetros para as entradas:

* width: Muda a largura da entrada
* borderwith: Muda a largura da borda da entrada.
* bg e fg: Muda as cores do texto que está na entrada e muda a cor do plano de fundo da entrada, respectivamente. 

``` Python
from tkinter import *

janela = Tk()

entrada = Entry(janela, width=50, borderwidth=30, bg="green", fg="black")
entrada.grid()
entrada.focus()

janela.mainloop()
```

um método interessante é o focus(). Ele faz com que o teclado fica na entrada que você quiser quando inicia o app.

``` Python
from tkinter import *

janela = Tk()

entrada = Entry(janela)
entrada.grid()
entrada.focus()

janela.mainloop()
```

outro método importante é o get(). ele coloca o texto que você escreveu na entrada em qualquer lugar que queira. Geralmente fica no widget label.

``` Python
from tkinter import * 

def print_hello():
    texto = "Hello " + entrada.get()
    label = Label(janela, text=texto)
    label.pack()

janela = Tk()

entrada = Entry(janela)
botao = Button(janela, text = "botão", command = print_hello)

entrada.pack()
botao.pack()

janela.mainloop()
```

Temos também um método para que apareça um texto dentro da entrada, para você saber o que tem que digitar. É o método insert. Coloca o número correspondente a entrada, primeiro sempre o 0.

``` Python
from tkinter import *

janela = Tk()

entrada = Entry(janela)
entrada.insert(0, "digite algo aqui.")
entrada.grid()

janela.mainloop()
```

Podemos fazer com que o texto que está na entrada apague quando faça alguma ação. Usamos o método delete.

``` Python
from tkinter import *

janela = Tk()

def clearToTextInput():
   my_text.delete("1.0","end")


my_text=Text(janela, height=10)
my_text.pack()


btn=Button(janela,height=1,width=10, text="Clear",command=clearToTextInput)
btn.pack()

win.mainloop()
```
