# Estrutra de repetição: For

O for funciona com o que chamamos de iteravel, isto é, um objeto que é possível repetir ações com ele.
Alguns onjetos no python são iteraveis, outros não. Exemplos de iteraveis são: as Strings, as listas (veremos em outra seção), a função range, a função enumerate.

O for funciona da seguinte maneira: definimos uma variável temporária que irá iterar sobre um iteravel e em seguida um bloco de comando que pode executar qualquer coisa enquanto a variavel estiver iterando. Assim que todos os elementos do iteravel acabarem, o programa vai para a proxima linha (fora do loop) e continua o programa.

```python
for variavel in iterador:
    pass
```

## Iterando sobre Strings

A primeira forma de iteração é com String. Podemos designar uma variável para receber cada termo da String e fazer o que quiser com ela, como por exemplo:

```Python
nome = "Gabriel"

for letra in nome:
    print(letra)

```
```Python
G
a
b
r
i
e
l
```

a variável letra vai receber, a cada vez, uma letra da variável nome (que é o interavel, neste caso) e imprimi-lo. Quando o bloco de comando acabar, a variável letra pegarar a proxima letra de nome e imprimirar novamente até que todas as letras de nome estiverem sido "cobertas". 

Obs: Podemos definir qualquer nome para a variável. É comum utilizar a letra i para essa função, mas se quiser ser mais específico
utilize o nome adequado.

perceba que cada letra da variável nome está em um linha. Caso queria colocar o nome em uma mesma linha é preciso utilizar o parâmetro opcional end da função print( ) para que isso aconteça.

```Python
nome = "Gabriel"

for letra in nome:
    print(letra, end='')

```
```Python
Gabriel
```

Caso queira transformar cada letra da String em maiúsculo, podemos fazer assim:

```Python
palavra = "AjjisdAJIJwpeW"

for i in palavra:
    print(i.title(), end='')

```
```Python
AJJISDAJIJWPEW
```

As possibilidades são inumeras, depende do que você quer alcançar. 

## Iterando com a função range( )

A função range é muito util para fazer iterações numéricas. Você define o intervalo de valores que queira trabalhar. 

Há quatro formar de trabalhar com o range: definindo o valor final; definindo o inicio e o fim; definindo o 
inicio, o fim e os saltos; e por fim, definindo o inicio, fim e saltos, mas agora decrescendo.

### Caso 1

```Python
for i in range(5):
    print(f'valor {i+1}/5)

```
```Python
valor 1/5
valor 2/5
valor 3/5
valor 4/5
valor 5/5
```

Perceba que a função range começa contanto a partir do 0 e não do 1. O python começa contando seus iteraveis a partir do 0. Por isso temosque colocar o i+1 para que apareça 1/5...

### Caso 2

```Python
for i in range(1, 10):
    print(i, end='')
    print(f' tree ' * i)

```
```Python
1 tree 
2 tree  tree 
3 tree  tree  tree 
4 tree  tree  tree  tree 
5 tree  tree  tree  tree  tree 
6 tree  tree  tree  tree  tree  tree 
7 tree  tree  tree  tree  tree  tree  tree 
8 tree  tree  tree  tree  tree  tree  tree  tree 
9 tree  tree  tree  tree  tree  tree  tree  tree  tree
```

Nesse caso, definimos um inicio (incluso) e um fim (que não é incluso). Em notação de conjunto na matemática seria assim: [1,10[ ou
)1,10).

### Caso 3

```Python
for i in range(0, 110, 10):
    print(i, end=' ')

```
```Python
0 10 20 30 40 50 60 70 80 90 100 
```

Definindo um separadoer, podemos escolher um intervalo em que os números vão aparecer e não somente listar todos os números do intervalo, como feito no caso 2. 

### Caso 4

```Python
for i in range(10, 0, -1):
    print(i)

```
```Python
10
9
8
7
6
5
4
3
2
1
```

Colocando o -1 na parte de saltos, faz com que ele conte do fim para o inicio saltando de um em um. É um caso especial, mas pode ser útil alguma vez.

### Obs

Podemos definir variáveis para o inicio, final e separador e coloca-las dentro da função range, ficando mais fácil o teste.

```Python
start = 0
stop = 10
step = 2

for i in range(start, stop, step):
    print(i, end=' ')
```
```Python
0 2 4 6 8 
```

veja que somente dei exemplos usando a função print para que pudesse vizualizar a como funciona, mas podemso colocar o que quiser dentro do bloco de comando do for, como por exemplo, uma condição, pedir dados do usuário com o input, outra estrutura de repetição, a imaginação é o limite.

```Python
for i in string:
    print(i, end=' ')
    if i == 'u':
        print('w', end=' ')
        continue

```
```Python
o i ,   t u w d o   b e m ?
```

```Python
for k in range(2):
    x = int(input("Digite um valor: "))
    print(x)

print(x)

```
```Python
# por exemplo: (pode ser quaisquer número).

5
10
10 
```

A iteração utilizando lista e o enumerate falarei quando estudarmos listas e tuplas, respectivamente. Precisa entender primeiro o que é o que para poder trabalhar o for nesses casos.
