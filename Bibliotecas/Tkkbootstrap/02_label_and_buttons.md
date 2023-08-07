# Label and Buttons

O esquema de criar label and buttons é bem pareceido com o tkinter tmb. Vamos ver 
cada um deles.

### Label

Para criar um label funciona da mesma forma que o tkinter.

```Python
label = tb.Label(text='', font=('', num), bootstyle='')

label.pack()
```

Temos uma opção para o bootstyle que é a "inverse", que coloca a cor escolhida como plano de fundo, não mais como cor da letra.

### Button

Para criar um botão, mesmo esquema. Uma das opções opcionais para os botõess é a outline e link, fica dentro do bootstyle; Outra opção é o
state (que indica de o botão é ativado ou desativado por padrão)

```Python
bbt = tb.Button(text='', font=('', num), bootstyle='success, outline or link', state="disabled")

bbt.pack()
```

Botões fazem ações, funciona da mesma forma que o tkinter. Define uma função e designa a um botão.

```Python
def command():
    pass

bbt = tb.Button(text='', font=('', num), bootstyle='success outline', command=command)

bbt.pack()
```
