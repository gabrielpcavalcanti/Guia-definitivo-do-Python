# Funções com **kwargs

Funciona quase da mesma forma que *args, com com duas diferenças: precisa ser argumentos nomeados para funcionar e ele cria um dicionário em vez de colcoar os elementos numa trupla. De resto tudo continua igual, apenas o fato que ganhamos o poder dos dicionários, não mais das tuplas.

```Python
def pessoas(**kwargs):
    print(kwargs)


pessoas(nome1="Gabriel", nome2="Júlia", nome3="José")

```

```Pyhton
{'nome1': 'Gabriel', 'nome2': 'Júlia', 'nome3': 'José'}
```

Assim como *args, o **kwargs não é obrigatório, mas precisa estar na ordem correta quando definimos uma função, para não termos problema. A ordem é a seguinte:

```Python
def ordem_parametros(parametro_posicionais, *args, parametros="default", **kwargs):
    pass


```

Assim como o *, o ** tem a função de desempacotar. Com a diferença que agora é um dicionário e não mais uma lista. 

O nome da chave em um dicionário tem que ser o mesmo nos parâmetros da função.
