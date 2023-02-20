# Botões

Avançando um pouco mais na biblioteca. Agora pe possível definir botões na nossa janela. Vejamos o que é possível fazer com eles.

Primeiramente definir um botão. Igual definir uma janela, mas com um detalhe, tem que definir em qual janela aquele botão vai estar.

depois é preciso definir como ele vai aparecer na tela. Pelo Pack( ), grid( ) ou place( ),  como qualquer wedgit.

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "botão")

botao.pack() # ou .grid() ou .place()

janela.mainloop()
```

Na classe Button é possível definir alguns parâmetros interessantes. O primeiro é o text, que diz qual o nome do botão e o segundo e o command, que fala a função do botão.

Para definir um comando para um botão é preciso colocar no parâmetro uma função. Pode ser uma função bilt-in do Python ou uma função criada pelo usuário.

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "botão", command = lambda: print("oi"))

botao.grid() 

janela.mainloop()
```
``` Python
from tkinter import * 

def print_hello():
    print("Hello")

janela = Tk()
botao = Button(janela, text = "botão", command = print_hello)

botao.place() 

janela.mainloop()
```

Além desses dois parâmetros é possível colocar um status no botão, para deixar ele ativado ou desativado. Utilizando a parâmetro state.

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "botão", state=DISABLE) # ou ACTIVE

botao.pack() # ou .grid() ou .place()

janela.mainloop()
```

Para mudar o tamanho do botão, utiliza os parâmetros padx e pady. 

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "botão", padx=50, pady=30)

botao.pack() # ou .grid() ou .place()

janela.mainloop()
```

Podemos alterar a cor do texto do botão e cor do plano de fundo. Usamos o parâmetro fg e bg mais o nome da cor ou o cógigo RGB.

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "botão", fg="blue0, bg="#32ff40")

botao.pack() # ou .grid() ou .place()

janela.mainloop()
```

Podemos criar um botão que sai da aplicação, fecha a janela. Basta usar o método .quit().

``` Python
from tkinter import * 

janela = Tk()
botao = Button(janela, text = "sair", command=janela.quit)

botao.pack() # ou .grid() ou .place()

janela.mainloop()
```

