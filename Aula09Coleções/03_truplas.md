# Truplas

Truplas são uma estrutura de dado muito parecido com as listas, com duas grandes diferenças. A primira que podemos declarar elas usanso ( ) ou só colocando os dados separados com vírgula. Como visto abaixo:

```python
trupla = (1, 2, 3, 4, 5)
trpla_2 = 1, 2, 3, 4, 5
```

A segundo é principal diferença é que elas são imutáveis, ou seja,, não é possivel adicinor,remoner ou trocar elementos de uma trupla.

Pode-se estar perguntando para que usar truplas em vez de lista, já que é bem mais versátil trabalhar com listas. A resposta é que se determinado dado não muda ou não queremos que ele mude durante o processo, truplas são uma boa solução. Como por exemplo, dias da semana, meses ou coordenadas.

Obs: Truplas com um único elemento não são consideradas truplas e sim o tipo da dado escrito.
Para virar uma trupla, adicione uma vírgula no fim.

```python
trupla = (1)
trupla_2 = (2,)

print(type(trupla))
print(type(trupla_2))

```

```python
<class 'int'>
<class 'tuple'>
```

Outra obersrvação é que não é possível usar a palavre **tuple** como varíavel. Ela é uma palavra reservada do Python.

Todas as operações que não envolve mudança que estão presentes nas listas, também podem ser usadas nas truplas.

## Imprimir o elemento da trupla

```python
trupla = (1,2,4,'oi', True)

print(trupla[2])
print(trupla[0])
print(trupla[4])
print(trupla[10])

```

```python
4
1
True
IndexError: tuple index out of range
```

## fatiar uma trupla

Assim como é possivel fazer o slicing de uma String e numa lista, é possível fazer de uma trupla também. Funciona da mesma forma, mas se não estiver lembrando, funciona assim:

```Python
nomes = ("Gabriel", "Sofia", "Eduardo", "Marina", "Felipe")

print(nomes[0:3])
print(nomes[1:2])
print(nomes[2:5])
print(nomes[:2])

```
```Python
('Gabriel', 'Sofia', 'Eduardo')
('Sofia')
('Eduardo', 'Marina', 'Felipe')
('Gabriel', 'Sofia')
```

## Determinar o indice

```python
trupla = (1,2,4,'oi', True)

print(trupla.index(4))
```

```python
2
```

## Verificar se um elemento está na trupla ou não

```Python
trupla = (43, 67, 43.5, "a")

print( 43 in trupla)
print( 8 in trupla)

```

```Python
True
False
```


## Criando uma trupla com o range

```Python
trupla = tuple(range(11))

print(trupla)

```

```Python
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

## Deletar a trupla

Basta usar o comando del + nome da trupla.

```Python
trupla = (1, 2, 3, 4)

print(trupla)

del trupla

```
```Python
(1, 2, 3, 4)
```

## Reescrever e cocatenar truplas

Truplas são imutaveis, mas podemos alterar seu valor reescrevendo as truplas ou cocatenar e escrever uma nova trupla como a união das outras truplas.

```Python
trupla_01 = (1, 2, 3)
trupla_02 = (4, 5, 6)

trupla_03 = trupla_01 + trupla_02

print(trupla_03)

trupla_01 = trupla_02

print(trupla_01)

```

```Python
(1, 2, 3, 4, 5, 6)
(4, 5, 6)
```

## Converter trupla em lista

Podemos usar o cast numa trupla para transforma-la numa lista.

```python
trupla = (1,2,4,'oi', True)

lista = list(trupla)

print(lista)

```

```python
[1, 2, 4, 'oi', True]
```

## determinar o tamanho, máximo, mínimo e a soma

```python
trupla_3 = tuple((1,2,3,4,5))

print(trupla_3)
print(len(trupla_3))
print(max(trupla_3))
print(min(trupla_3))
print(sum(trupla_3))

```

```python
(1,2,3,4,5)
5
5
1
15
```

## Contar os elementos de uma trupla

```python
trupla = 1,2,2,2,2,3,4,5,5,5,2

print(trupla.count(2))
```

```python
5
```
