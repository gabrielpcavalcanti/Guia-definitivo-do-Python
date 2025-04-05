# Listas

Listas são uma estruturas de dados bastante poderosa no Python. Como o nome diz, é uma coleção de elementos de um ou vários tipos e armazenamos em uma única variável.

Em outras linguagems de programação as listas são chamadas de vetores.

Para declarar uma lista, basta colocar [ ]. Como no exemplo a seguir:

lista = [ ]

Obs: Não podemos usar a palavra **list** como nome de uma variável, pois é uma palavra reservada no Python.

Dentro de uma lista podemos colocar qualquer tipo de dado, inclusive outra lista (Chamamos isso de aninhamento) e não é preciso especificar o seu tamanho, já que listas são mutáveis, ou seja, podemos acrecentar, retirar, mudar qualquer elemento de uma lista.

```python
lista = [1, 2, 3, 4, 5]
lista_2 = [2.5, 6.8, 3.6]
lista_3 = ['João', 'Ana', 'Felipe', 'Mateus']
lista_4 = [1, 4.6, 'gato', [1, 2, 8.549]]
```

Toda lista possui índices associados. No Python, o primeiro elemento de uma objeto possui índice 0 e não 1. 

Obs: Tudo o python é um objeto, mas não se preucupe com isso agora, quando chegar em POO,
vai ficar tudo mais claro.

## Acessar elementos

Para acessar qualquer elemento de uma lista é preciso chamar o nome dela e colocar [n], onde n é o índice. E ainda podemos atribuir uma variável para determinado elemento.

obs: O Python permite acessar o último elemento de uma lista de uma maneira diferente,
utilizando n = -1. Só faz sentido utilizar isso quando a lista for muito grande e não souber
a quantidades de elementos. Essa regra extende para outros índices negaivos, -2, por exemplo,
seleciona o penúltimo item da lisa.

```python
lista = [1, 2, 3, 4, 5]
lista_2 = [2.5, 6.8, 3.6]
lista_3 = ['João', 'Ana', 'Felipe', 'Mateus']
lista_4 = [1, 4.6, 'gato', [1, 2, 8.549]]

lista[2] # 3
lista_2[0] # 2.5
lista_3[4] # Erro: IndexError: list index out of range. Mas um tipo de erro, perceba e anote. Aumente sua coleção de erros kkkk.

lista_4[-1] # [1, 2, 8.549]

item_2 = lista[1] # item_2 = 2
```

## Copiar uma lista

Talvez seja necessário copiar uma lista e coloca-la em outra variável. Podemos fazer isso de duas maneiras.

```Python
lista_1 = list(range(1,100,20))

# Maneira 1
lista_copia_1 = lista_1

# Maneira 2
lista_copia_2 = lista_1[:]

print(lista_copia_1)
print(lista_copia_2)

```
```Python
[1, 21, 41, 61, 81]
[1, 21, 41, 61, 81]
```

## índice do elemento de uma lista

Podemos saber qual é o índice do elemento de uma lista, atravez da função index(n). Onde n é
o elemento da lista.

```python
lista = [1, 2, 3, 4]
print(lista.index(2))

```

```python
1
```

## Mudar valores de uma lista

Podemos mudar elementos de uma lista simplesmente acessando o seu elemento e atribuindo outro valor de qualquer tipo que seja.

```python
lista = [1, 2, 3, 4, 5]

lista[3] = 'toquei'

print(lista)
```

```python
[1, 2, 3, 'toquei', 5]
```

## fatiar uma lista

Assim como é possivel fazer o slicing de uma String, é possível fazer de uma lista também. Funciona da mesma forma, caso não 
estiver lembrando, funciona assim:

```Python
nomes = ["Gabriel", "Sofia", "Eduardo", "Marina", "Felipe"]

print(nomes[0:3])
print(nomes[1:2])
print(nomes[2:5])
print(nomes[:2])
```
```Python
['Gabriel', 'Sofia', 'Eduardo']
['Sofia']
['Eduardo', 'Marina', 'Felipe']
['Gabriel', 'Sofia']
```

## Acrecentar elementos de uma lista

O método append acrecenta qualquer elemento ao final e o método insert, acrecenta em qualquer posição (escolhendo qual o índece que
queremos e depois o dado que queremos inserir).

```python
lista_4 = [1, 4.6, 'gato', [1, 2, 8.549]]

lista_4.append('acrecentei no final da lista')
lista_4.insert(0, 'coloquei no primeiro elemento')

print(lista_4)

```

```python
['coloquei no primeiro elemento', 1, 4.6, 'gato', [1, 2, 8.549], 'acrecentei no final da lista']
```

## Retirar elementos de uma lista

O método pop deleta o último elemento da lista, se nunhum parâmetro for especificado e o del deleta o elemento que quisermos, desde que ele exista na lista. Também podemos usar o método remove para retirar um elemento em específico.

```python
lista_4 = ['coloquei no primeiro elemento', 1, 4.6, 'gato', [1, 2, 8.549], 'acrecentei no final da lista']

lista_4.pop()
lista_4.pop(0)

print(lista_4)

```
```Python
[1, 4.6, 'gato', [1, 2, 8.549]]
```

O pop ainda nos permite guardar o valor do elemento excluido numa variável, mas lembre-se: o elemento sai da lista.

```Python
lista_4 = [1, 4.6, [1, 2, 8.549]]

elemento_pop = lista_4.pop(2)
print(elemento_pop)
print(lista_4)

```

```python
[1, 2, 8.549]
[1, 4.6]
```
A Funçao del deleta um elemento.

```python
lista_4 = [1, 4.6, [1, 2, 8.549]]

del lista_4[2]
print(lista_4)
```

```python
[1, 4.6]
```

Função remove remove um elemento em específico.

```python
lista_4.remove(4.6)
print(lista_4)

```

```python
[1]
```

Se quisermos eleminar todos os elementos de uma lista, basta usar o método clear( ).

```python
lista = [1, 2, 3, 4, 5]
lista.clear()

print(lista)

```

```python
[ ]
```

## Acessando elementos de um lista aninhada

Como visto acima, uma lista pode conter listas dentro dela. Como uma lista contem vários elementos, para acessar um elemento de uma lista que está dentro de outra, basta usar [n][m]. O n será o índice da lista principal e o m será o índice da lista que está dentro da lista principal. Com um exemplo fica mais claro.

```python
lista_aninhada = [[1,2,3], [3.6, 7.89, 45], ['string', 'inteiro', 'float']]

elemento_2_1 = lista_aninhada[2][1]

print(elemento_2_1)
```

```python
inteiro
```

## Contatenamento de listas

Para concatenar lista é só utilizao o sinal de adição: +.

```python
lista = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_3 = lista + lista_2

print(lista_3)
```

```python
[1, 2, 3, 4, 5, 6]
```

## Tamanho, máximo, mínimo e soma de uma lista

O tamanho de uma lista pode ser determinado usando a função len( ).

```pyton
lista = [1 ,2 ,3 , 4, 5, 6]
print(len(lista))

```

```python
6
```

O maior e menor valor da lista é detrminado usando as funções max( ) e min( ).

```python
lista = [1 ,2 ,3 ,4 ,5 ,6]

print(max(lista))
print(min(lista))

```

```python
6
1
```

a soma de elementos de uma lista é dado pela função sum( ). Lembrando que precisa ser números e não strings ou boolens.

```python
lista_num = [1, 2, 3, 4, 5, 7]

print(sum(lista_num))

```

```python
22
```

## Alguns outros métodos

Para ver todos os métodos das listas, basta usar a função dir( ). Veremos alguns deles abaixo mais
algumas outras funções que podem ser usadas com listas, mas tamém com outros objetos.

```python
dir_list = dir([])
print(dir_list)

```

```phython
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
* A palavra in pode ser usada para verificar se um elemento está ou não numa lista. Ele retorna um valor booleano.

```python
lista = ['oi', 'tchau', 42, 22]

print('oi' in lista)
print(3 in lista)

```

```python
True
False
```

* O método sort( ) organiza os elementos da lista em por ordem crescente ou em ordem alfabética.

```python
lista_num = [4, 6, 2, 8, 1, 6, 9, 20]
lista_str = ['a', 'c', 't', 'r']

lista_num.sort()
lista_str.sort()

print(lista_num)
print(lista_str)

```

```python
[1, 2, 4, 6, 6, 8, 9, 20]
['a', 'c', 'r', 't']
```

* O método count( ), conta a quantidade de vez que o elemento está presente na lista.

```python
lista = [1 ,1 ,1 ,1 ,1 , 3, 4, 3]

print(lista.count(1))
print(lista.count(3))
print(lista.count(5))

```

```python
5
2
0
```

* O método split( ) transforma uma string em uma lista. ele pega os separador do espaço para separar os elementos da lista.

```python
str_1 = "vou virar uma lista"

print(str_1.split())

```

```python
['vou', 'virar', 'uma', 'lista']
```

* O método reverse( ), inverte a ordem da lista.

```Pyhton
num = [1, 2, 3, 4, 5]

num.reverse()

print(num)

```

```Python
[5, 4, 3, 2, 1]
```
