# Primeiros passos

Para podermos iniciar o Tkinter no Python é preciso fazer três coisas:

1 - importar a biblioteca

2 - iniciar o Tkinter com a função Tk( )

3 - Definir o loop para que a janela rode infinitamente. Utilizar o método mainloop( ).

``` Python
from tkinter import * # importa a biblioteca.

janela = Tk() # inicializa.
janela.mainloop() # loop.
```

Geralmente o nome utilizado para janela principal é root, mas para fins didaticos, decidir colocar o nome "janela". Pode utilizar o nome que quiser, fique a vontade.

## Alguns métodos iniciais

Como você deve saber o interpretador do python ler linha por linhas, de cima para baixo, a menos que haja alguma estrutura condicional ou de repetição. 

O que quero dixer com isso é que todos os métodos utilizados ficarão entre a função Tk( ) e o método mainloop( ). Veremos cada um com calma.

* title: Define o nome da janela.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")

janela.mainloop()
```

* icon: Define um icone para a janela. Utilize pelo método iconbitmap( ). É preciso que o icone esteja na pasta do arquivo .py.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.iconbitmap("Tkinter/potatos.ico")

janela.mainloop()
```

* geometry: Define a geometria inicial da janela.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.iconbitmap("Tkinter/potatos.ico")

janela.geometry("500x250+200+200")

janela.mainloop()
```

O parâmetro do método é uma String na forma "cxl+x+y". Onde:

c é o comprimeto da janela.

l é a largura da janela.

x é a posição na direção x da janela.

y é a posição na direção y da janela.

Perceba que antes a janela abria com um tamanho padrão e em qualquer lugar, definindo a gemotria é possível definir qualquer outro padrão para as dimenções e posicionamento da janela.

* resizable: Permite a escolha de modificar o tamanho da janela manualmente. Pode configurar tanto para o comprimento como para a largura.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.iconbitmap("Tkinter/potatos.ico")

janela.geometry("500x250+200+200")
janela.resizable(False, False) # comprimento, largura.

janela.mainloop()
```

Perceba que antes a janela podiamos alterar o tamanho quanto quisermos, com esse método podemos escolher o que fazer com essa função.

* Size: Define o tamanho mínimo e máximo que a janela pode ter. Método minsize( ) para o mínimo e maxsize( ) para o máximo.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.iconbitmap("Tkinter/potatos.ico")

janela.geometry("500x250+200+200")
janela.minsize(width = 500, height = 250)
janela.maxsize(width = 700, height = 400)

janela.mainloop()
```

Para ficar algo mais claro é possivel escrever o nome dos parâmetros dos métodos. Se não quiser, basta colocar assim, por exemplo: janela.maxsize(700, 400)

* state: Define se quer começar com a janela maximizada ou minimizada.

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.iconbitmap("Tkinter/potatos.ico")

janela.geometry("500x250+200+200")

janela.state("zoomed") # podemos utilizar também o "iconic" para iniciar com a janela minimizada.

janela.mainloop()
```

### Algumas configurações visuais

É possível fazer algumas configurações visuais na janela. 

Alguns códigos de cores:

"#000000" -> Cógido hexadecimal, RGB. 

"blue"

"black"

"yellow"

"red"

"white"

"orange"

"brown"

"green"

* Mudar a cor do background da janela

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela['bg'] = "orange"

janela.mainloop()
```

outra forma de mudar a cor do background é com o método .configure(background='#282828')

``` Python
from tkinter import * 

janela = Tk()

janela.title("Janela")
janela.configure(background='#282828')

janela.mainloop()
```