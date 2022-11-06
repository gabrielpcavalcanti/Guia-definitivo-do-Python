# List compreheinsions

É uma forma mais sucinta de escrever código, mais inteligente e elegante. 
É uma das formas que alguns chamam de Pythonicas (Uma maneira de escrever código típica da linguagem Python). 

Podemos utilizar compreheinsions em listas e dicionários, vamos ver as listas nessa aula.
Criar uma lista a partir de um dado interavel. A sintaxe é a seguinte:

```Python
[dado for dado in iteravel]
```

Vamos ver um exemplo:

```Python
numeros = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]

res = [numero * 10 for numero in numeros]
print(res)

print([numero / 5 for numero in numeros])

```

```Python
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
```
No exemplo acima, escolhi um nome para ser a variável iteravel e iterei sobre o interval lista já criado, gerendo uma nova lista (atribui o valor dela na varivável res).

### List compreheinsions versus loop

O list compreheinsions mistura listas com estrutura de repetição, uma forma mais compacta de fazer as tarefas.

Fazendo o mesmo código acima, mas com loop for apenas, para verifiar a diferença entre ele o list compreheinsions.

```Python
numeros = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
num_10 = []
num_5 = []

for num in numeros:
    num_2 = num * 10
    num_10.append(num_2)

print(num_10)

for num in numeros:
    num_3 = num / 5
    num_5.append(num_3)

print(num_5)

```

```Python
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
[0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
```

perceba a diferença no tamanho do código. Concorda que é mais simples e elegante o list compreheinsions.

### List compreheinsions com Strings

Podemos utilizar Strings como iteraveis também, assim como fizemos com as listas. 

```Python
stri = "oi, tudo bem?"

print([letra.upper() for letra in stri])

```

```Python
['O', 'I', ',', ' ', 'T', 'U', 'D', 'O', ' ', 'B', 'E', 'M', '?']
```

Podemos colocar a string dentro de listas e utlizar o list compreheinsions.

```Python
nomes = ["maria", "joao", "gabriel"]

print([letra.capitalize() for letra in nomes])

```

```Python
['Maria', 'Joao', 'Gabriel']
```

### List compreheinsions com funções 

A variável iteravel pode ser uma função, como no exemplo abaixo.

```python
def quadrado(num):
    return num * num


numeros = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]

res3 = [quadrado(numero) for numero in numeros]
print(res3)

```

```Python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Adicionar estruturas condicionais dentro do list compreheinsions 

Podemos deixar as list compreheinsions ainda mais poderosas, adicionando condições ao código, como podemos ver abaixo:

```Python
numeros = range(1,51)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(f"Número pares de 1 a 51: {pares}")
print(f"Número impares de 1 a 51: {impares}")

```

```python
Número pares de 1 a 51: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
Número impares de 1 a 51: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
```
