# Frames

Frame é uma região na janela que vão ficar seus widget's. É utilizado para organização da GUI. Dentro da janela temos os frames e dentro dos frames temos os widgets.

lembrando que os frames também são widgets.

``` Python
from tkinter import *

janela = Tk()

frame_1 = Frame(janela)
frame_1.grid(row=0, column=0, pady=50)
frame_2 = Frame(janela)
frame_2.grid(row=1, column=0, pady=30)

btn_1 = Button(frame_1, text = "sair", command=janela.quit)
btn_2 = Button(frame_2, text="frame 2")

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=0)

janela. mainloop()
```

Funciona assim: Criamos quantos frames quiser e colocamos dentro da janela. Você primeiro refrencia eles em relação a janela e depois cria
os widgets e referencia eles em relação ao frame. É como tivesse diversas janelas dentro da própia janela. 

Quando usarmos o grid, a referencia será de acordo com o frame escolhido, então, por exemplo, se ja tiver um widget na possição (0,0) no 
frame 1, temos que colocar outro widget em outra posição. Mas caso queria colocar em outro frame, podemos colocar um widget na posição
(0,0) novamente, não irá sobrepor.

Outro uso muito importante dos frames é a organização para o POO. Falaremos com calma depois, mas a ideia é colocar cada página da aplicação
dentro de um frame. Cada frame uma página. Cada um desses frames vira ma função dentro da classe, que é a aplicação.

Isso fará bem mais sentiso no futuro, mas é so para dar uma ideia de como usa e de como eles são poderosos dentro do Tkinter.

## Labelframe

É um tipo especial de frame. Nele é possível definir um nome que irá aparecer dentro do frame. Tudo igual, somente com esse detalhe a mais.

``` Python
from tkinter import *

janela = Tk()

frame_1 = Frame(janela)
frame_1.grid(row=0, column=0, pady=50)
frame_2 = LabelFrame(janela, text="isso é o espaço do frame 2", pady=30)
frame_2.grid(row=1, column=1, pady=30)

btn_1 = Button(frame_1, text = "sair", command=janela.quit)
btn_2 = Button(frame_2, text="frame 2")

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=0)

janela. mainloop()
```

Esses exemplos são bem simples e um pouco inúteis. Somente mostram como o widget funciona. O objetivo é entender isso e depois usar eles em exemplos e projetos mais complexos e organizados. 
