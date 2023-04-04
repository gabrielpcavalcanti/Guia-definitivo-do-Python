# Imagens

O tkinter possui um sistema própio para criação e utilização de imagens, mas, infelizmente, os tipos de arquivos que ele 
suporta são datados, ninguém utiliza mais. Então é necessário utilizar uma biblioteca extra para utilizar imagnes no Tkinter.

A biblioteca é a pillow, uma biblioteca para imagens no Python. Ela possui uma classe que funciona dentro do Tkinter. Para importa-lá, utilizamos o seguinte comando:

``` Python
from PIL import Image, ImageTk
```

Pode pensar que seria "import pillow", mas por algum motivo (que desconheço), importamos ela da maneira acima.

## Importando a imagem

É uma linha de comando um pouco complexa, mas uma vez feita, a sua imagem estará importada. Siga esse padrão para qualquer imagem
que quiser.

``` Python
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = ImageTk.PhotoImage(Image.open("Tkinter/dk3.jpg"))

root.mainloop()
```

## Colocando a imagem na tela

Após importar a imagem, temos que fazer mais dois passos para que ela apareça na tela. O primeiro é definir o widget label, colocando 
como parâmetro a imagem e em seguida, utilizar alguma forma de layout para que o label apareça na tela.

``` Python
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = ImageTk.PhotoImage(Image.open("Tkinter/dk3.jpg"))
label = Label(image=img)
label.pack()

root.mainloop()
```

Em resumo, para utilizar imagens no Tkinter, é preciso fazer três coisas:

1 - Importar a imagem
2 - Colocar a imagem dentro de um widget
3 - colocar o widget dentro no root ou do frame
