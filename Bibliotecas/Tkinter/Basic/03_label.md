# Label 

O label é utilizado para organização e design da janela e para insersão de textos.

funciona da mesma forma que um botão, ativa a classe e define em qual janela o label vai pertencer e se quiser, muitas outras configurações. Veremos algumas delas.

lembre que sempre é preciso colocar o método de layout.

```Python
from tkinter import *

janela = Tk()

label1 = Label(janela)
label1.pack()

janela.mainloop()
```

É possível alterar o texto utilizando variáveis, para isso é preciso chamar a classe StringVar( ), definir a varivável com o método set( ) e colocar nos parâmetros do label, não mais o text, mais sim o textvariable.

```Python
from tkinter import *

janela = Tk()

texto = StringVar()
texto.set("texto teste")

label1 = Label(janela, textvariable=texto)
label1.pack()

janela.mainloop()
```

## Configuração do label

podemos definir:

* a cor do background (bg),
 
* da letra (fg), 
 
* fonte do texto (font),

A fonte tem diversas configurações. Pesquise para ver o que pode ou não fazer.

* da borda (bd) e tipo da borda (relief),

O parâmetro opcional relief possui seis tipos: solid, flat, raised, sunken, ridge e groove. 

* comprimento (width) e altura (height) do label,

O valor colocado é relatico ao tamanho da fonte do texto.

* posicionamento do texto dentro do label (anchor),

Utiliza o posicionamento da rosa dos ventos (em inglês) e caso queira colocar centralizado, usa a palavra CENTER. Não precisa colocar numa String, apenas a letra sempre capitalizada.

* justificar o texto (justify),

Igual ao anchor, mas com as opções: CENTER, LEFT, RIGHT.

Todos eles são parâmetros opcionais da classe label.

```Python
from tkinter import *

janela = Tk()

label1 = Label(janela,text='teste para ver o design', bg='#344556', fg='red', font='Times 20 bold italic', bd=5, relief='solid', width=30, height=2, anchor=S, justify=RIGHT)
label1.pack()

janela.mainloop()
```

As configurações são inúmeras, faza vários testes para ver o que funciona e o que não funciona. Lembre que existe a função help( ) para nos ajudar.

Podemos também realizar cada uma das opções do label utilizando dicionário:

```Python
from tkinter import *

janela = Tk()

label1 = Label(janela)
label1['text'] = 'texto teste'
label1['bg'] = 'orange'

label1.pack()

janela.mainloop()
```
