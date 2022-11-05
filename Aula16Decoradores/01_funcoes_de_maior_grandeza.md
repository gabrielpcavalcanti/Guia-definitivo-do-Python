# Funções de maior grandeza

É a possibilidade de ter funções dentro de outras funções, funções que retornam outras funções,
passar uma função como argumento de outra função. 

Esse recurso no Python se chamam Higher Order Functions - HOF e são Cidadões de Primeira Classe, First Class Citizen. 

Esse conhecimento vai ajudar a entender os decoradores, que por sua vez, serão muito úteis no estudo da programação orientada
a objetos - POO.

## Funções aninhadas

são funções dentro de outras funções. Vejamos alguns exemplos:

```Python
from random import choice


def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lolololololo', 'kkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir('Fernanda')

print(rindo())
print(rindo())
print(rindo())
```

```Python
# Exemplo de saída
hahahahaha Fernanda
lolololololo Fernanda
lolololololo Fernanda
```

Está acontecendo o seguinte: Definimos uma função faz_me_rir que recebe um parâmetro, pessoa. Dentro dela, temos uma outra
função, dando_risada que retorna uma string. A função faz_me_rir retorna a função dando_risada que por sua vez retorna a String. 
Então quando definimos uma variável "rindo" e mandamos imprimir ela, recebemos a String.

É um pouco confuso, mas com o tempo vai ficando mais claro. Vejamos outro exemplo com a mesma lógica.

```Python
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Angelina'))
print(cumprimento('Felicity'))
```

```Python
# Exemplo
Gosto muito de você Angelina
Suma daqui Felicity
```

# Usanso funções como argumento

Criamos várias funções e uma ou mais recebe como parâmetro as outras funções. Dentro dela a função retorna a função que colocamos
como parâmetro. confuso?, veja o exemplo a seguir. 

```Python
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))
```

```Python
7
1
12
1.3333333333333333
```

Criamos as funções somar, diminuir, multiplicar e dividir e calcular. A última recebe uma função como parâmetro e dentro dela
retorna essa mesma função, que vai ser uma das outras que criamos, retornando, neste caso, o valor da operação matemática.
