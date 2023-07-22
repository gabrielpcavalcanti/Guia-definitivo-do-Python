# Label and Buttons

O esquema de criar label and buttons é bem pareceido com o tkinter tmb. Vamos ver 
cada um deles.

### Label

Para criar um label funciona da mesma forma que o tkinter.

```Python
label = tb.Label(text='', font=('', num), bootstyle='')

label.pack()
```

### Button

Para criar um botão, mesmo esquema. Uma das opções opcionai para os botõess é a outline e link, fica dentro do bootstyle;

```Python
bbt = tb.Button(text='', font=('', num), bootstyle='success, outline or link')

bbt.pack()
```

Botões fazem ações, funciona da mesma forma que o tkinter. Define uma função e designa a um botão.

```Python
def command():
    pass

bbt = tb.Button(text='', font=('', num), bootstyle='success, outline', command=command)

bbt.pack()
```
