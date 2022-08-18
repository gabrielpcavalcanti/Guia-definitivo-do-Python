# Iterações com listas

Já vimos as estruturas de repetição e as listas. Agora o que vamos fazer é unir elas para adquirir um dos
maiores recursos que podemos ter no Python. 

O objetivo é fazer iterações em cima de uma lista. Esse processo facilita muitas operações e é até um pouco vicioso. Quero
dizer que muitos dos problemas que poderiam ser resolvidos de outra forma, você so resolve dessa maneira. É importante aber a 
maior uantidade de formas possíveis e essa é uma muito boa.

É uma forma bem simples de se trabalhar com listas, mas muito eficiente, por isso muito boa.

Normalmente utilizamos o laço for para iterar sobre listas. 

### Percorrendo elementos de uma lista

A variável do for percorre cada um dos elementos da lista (é o iteravel) e realiza o que quiser (contanto que esteja no bloco de comando). Assim que todos os elementos da lista terminarem, o loop se encerra e o programa vai para a próxima linha de comando 

```Python
lista_num = [1,2,3,4,5,6,7,8,9,10]

for num in lista_num:
    print(num, end=' ')

print()
print("O loop for acabou")

```
```Python
1 2 3 4 5 6 7 8 9 10 
"O loop for acabou"
```

### Inserindo elementos em uma lista pelo laço for

Caso queira preencher uma lista com novos elementos, podemos utilizar o método append( ), nada novo. Mas caso estivermos 
percorrendo uma lista ou utilizando o range( ) com o loop for, podemos inserir novos elementos em uma nova lista ou na mesma, se quiser.

```Python
new_lista = []

for i in range(10):
    x = i + 1
    new_lista.append(x)

print(new_lista)
```
```Python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

podemos ainda criar uma lista a partir do range. Basta fazer o casting com a função list( ) que isso é feito.

```Python
lista = list(range(5))

print(lista)
```
```Python
[0, 1, 2, 3, 4]
```

### Percorrer elementos em uma lista fatiada

Em vez de percorrer a lista como um todo, podemos somente percorrer um pedaço dela, utilizando o slicing.

```Python
palavras = ["oi", "ola", "como vai", "hello"]

for i in palavras[1:3]:
    print(i)

```
```Python
ola
como vai
```
