# Introdução

TTKbootstrap é uma biblioteca que deixa o tkinter mais bonito, com uma cara mais moderna. Temos diversos temas que podemos utilizar e vários widgets tmb.

A primeira coisa como sempre é fazer o download (com o método pip padrão do Pyhton) e importar a biblioteca. Sempre temos que importar a trkbootstrap, geralmente com o apelido tb, mas pode colocar qualquer um e podemos também, além de outros, importar um módulo da biblioteca, 
.constants, que poderá ser útil depois. 

```Python
import ttkbootstrap as tb
from ttkbootstrap.constants import *
```

Muitos dos métodos aqui são muito parecidos com o tkinter, alguns identicos.

Então para criar uma instância do ttkbootstrap, fazemos isso:

```Python
root = tb.Window(themename="superhero")

root.mainloop()
```

Escolhemos um dos temas disponíveis e colocamos no parâmetro themename. O link para o site onde é possível ver os temas é: https://ttkbootstrap.readthedocs.io/en/latest/themes/

Entre essas duas linhas de comando, colocamos todo o nosso código. Alguns parâmetros iniciais identicos ao tkinter:

```Python
root = tb.Window(themename="superhero")

root.title("TTK Bootstrap!")
root.iconbitmap("Bibliotecas\Tkinter\potatos.ico")
root.geometry("500x350")

root.mainloop()
```

Essa biblioteca possui algumas cores padrão que tem ums nomes diferentes, são eles:

Default, primary, secondary, success, info, warning, danger, linght and dark.

Iremos utilizar essas cores com os widgets.
 