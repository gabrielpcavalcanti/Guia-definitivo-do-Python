# Função com *args

O *args é um parâmetro como qualquer outro. Podemos colocar o nome que quiser, mas como convenção, utiliza-se o nome args. 
O que importa, na verdade, e o *. 

ele tem o poder de colocar todos os valores extras em um função dentro de uma trupla, portanto tudo que sabemos sobre truplas pode ser utilizado aqui.
Normalmente as função vem somente com o *args ou com todos os outros parâmetros posicionais, o *args e por fim, os default. 

Ele não é um argumento obrigatório, então a utilização dele é opicional.

So colocamos o *args no corpo da função. Caso queira utilizar os valores da trupla dentro da função, apenas utilize o nome args, sem o *.

```python
def sabor_pizza(*args):

    print("Igredientes Pizza:")
    for i in args:
        print(i)

    print()

sabor_pizza("pepperoni")
sabor_pizza("pepperoni", "cheese")
sabor_pizza("cebola", "alho", "milho")
```

```python
Igredientes Pizza:
pepperoni

Igredientes Pizza:
pepperoni
cheese

Igredientes Pizza:
cebola
alho
milho
```

Esse é só um exemplo, podemos fazer muito, mas muito mais coisa. A criatividade é o limite.

Um outro exemplo com o *args no final, após ter colocado parâmetros.

```python
def sabor_pizza(tamanho, *args, bom=True):

    print(f"Igredientes Pizza de tamanho {tamanho}:")
    for i in args:
        print(i)

    print()

sabor_pizza("M", "pepperoni")
sabor_pizza("G","pepperoni", "cheese")
sabor_pizza("P", "cebola", "alho", "milho")
```

```Pyhton
Igredientes Pizza de tamanho M:
pepperoni

Igredientes Pizza de tamanho G:
pepperoni
cheese

Igredientes Pizza de tamanho P:
cebola
alho
milho
```

Outra função bem interessante do * é que ele pode desempacotar uma lista de forma bem mais simples e facil.

```python
def somar_numeros(*args):

    return sum(args)


numeros = [4, 3.7, 2, 87, 5]

soma_teste = somar_numeros(*numeros)

print(soma_teste)
```

```Pyhton
101.7
```
