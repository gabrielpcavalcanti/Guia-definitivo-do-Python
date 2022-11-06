# Funções com retorno

Funções também podem retornar valores. Utilizamos a palavra reverva da **return**. É necessário passar a função print( ) para que o resultado do return apareça na tela. Retornar um valor é devolver uma valor ou um conjunto de valores ao programa. A instrução **return** toma um valor que está em uma função e o envia de volta à linha que a chamou.

```python
def soma(num1, num2):
    return num1 + num2


soma_qualquer = soma(3, 4)

print(soma_qualquer)
print(soma(1,41))

```

```python
7
42
```

Quando chamamos um valor, precisamos forncer uma variável para em que o valor de retorno possa ser armazenado.

## Funções com retorno e valores deafault

Podemos passar parâmetros opcionais com funções de retorno também. Lembrando que eles tem que estar no final e caso querira utiliza-lo sem seu valor padrão, tem que colocar ele sempre no final e na ordem que aparece no corpo da definição da função. Caso não o faça, a função pode se embralhar, cuidado!

```python
def formar_roupa(tipo, tamanho, cor, frase="Esrampa padrão"):

    return f"O tipo da roupa é {tipo}, seu tamnho é {tamanho}, com a cor {cor} e com a estampa {frase}."


roupa_01 = formar_roupa("Camisa", "M", "Preta"))

print(roupa_01)
print(formar_roupa("Camisa", "M", "Preta", "Rock in roll"))
print(formar_roupa("Camisa", "Preta", "Rock in roll", "M"))

```

```python
O tipo da roupa é Camisa, seu tamnho é M, com a cor Preta e com a estampa Esrampa padrão.
O tipo da roupa é Camisa, seu tamnho é M, com a cor Preta e com a estampa Rock in roll.
O tipo da roupa é Camisa, seu tamnho é Preta, com a cor Rock in roll e com a estampa M.
```

## Função com estruturas condicionais

A função pode devolver qualquer tipo de valor que quisermos, como listas e dicionários. Faremos um programa que utiliza disso 
e das estruturas condicionais.

```python
def construir_pessoa(nome, sobrenome, tipo=''):
    """Devolve um dicionário ou uma lista com o nome e sombrenome de uma pessoa"""

    print("Escreva 'D' para que a saida seja um dicionário e 'L' para uma lista")

    tipo1 = input("Digite o valor do tipo: ")

    if tipo1 == "D":
        pessoa = {"primeiro_nome": nome, "segundo_nome": sobrenome}
        return pessoa

    elif tipo1== "L":
        pessoa =  [nome, sobrenome]
        return pessoa

    else:
        print("Valor inválido")


eu = construir_pessoa("Gabriel", "Cavalcanti")

print(eu)

```

## Função com laço while

No exemplo passado, utilizamos estruturas condicionais para o nosso fim, também podemos utilizar estruturas de repetição dentro de funções. Na verdade, podemos colocar o que quisermos dentro de funções. 

```python
def soma(num1, num2):
    return num1 + num2


while True:
    num1 = int(input("Digite o valor do número 1: "))
    num2 = int(input("Digite o valor do número 2: "))

    soma_teste = soma(num1, num2)

    if num1==9999 or num2==9999:
        break
    
    else:
        print(soma_teste)

```

## Função com laço for

Assim como no laço while, podemos utilizar o for, como vemos no exemplo a seguir:

```python
def saudacoes(nomes):

    for name in nomes:
        msg = "Olá, " + name.title() + "!"
        print(msg)


usuarios = ["Aline", "Rebecca", "pedro"]

saudacoes(usuarios)

```

```Python
Olá, Aline!
Olá, Rebecca!
Olá, Pedro!
```

## Utilizar uma função como parâmetro de outra função

Podemos colocar como parâmetro de uma função, outra função já criada anteriormente. 

```python
def sub(num1, num2):
    return num1 - num2


def conta(num1, num2, operacao=sub):
    return operacao(num1,num2)


print(conta(1,3))
print(conta(5,6))
print(conta(9,6))

```

```Pyhton
-2
-1
3
```

## return como break

O return também possui a função do break, ou seja, caso o interpretador passe por um return, a função é encerrada naquela declaração.

```python
def e_par(num):
   
    if num % 2 == 0:
        return 'é par'
    else:
        return


print(e_par(4))
print(e_par(5))

```

```python
é par
None
```
