# Checkbox

Não tem muito o que dizer aqui, é um checkbox. Temos várias opções de checkbuttons que podemos trabalhar, vamos ver uma por uma.

### Checkbutton

Abaixo vemos o código de criação de um checkbox e com algumas configurações. 

```Python
var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info",
    text="Check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

check.pack()
```

### Toolbutton

```Python
var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info, toolbutton",
    text="Check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

check.pack()
```

O toolbutton tambem possui a opção de outline

```Python
var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info, toolbutton, outline",
    text="Check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

check.pack()
```

### Round toogle buttons

Esse é aquele que fica uma barra verde dizendo que esta selcionado ou não.

```Python
var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info, round-toggle",
    text="round toggle",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

check.pack()
```

### square toggle Button

Mesma coisa do anterior, mas quadrado.

```Python
var1 = IntVar()
check = tb.Checkbutton(
    bootstyle="info, square-toggle",
    text="square toggle",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)

check.pack()
```
