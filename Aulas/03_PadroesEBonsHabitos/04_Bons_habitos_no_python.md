# Python Good Habits

Durante meu estudo de Python, assisti vários cursos,vídeos e li muitos fóruns mostrando formas melhores de escrever em Python. Cada um tem um estil próprio, mas a comunidade prefere de uma maneira e mais importente é seguir um padrão definido por você e/ou pela empresa/projeto que está atuando. 

Separei aqui varias dessas formas de escrever melhor o código para várias áreas dentro da linguagem Python. Não se preocupe em decorar tudo porque provavemente muitas dos tópicos aqui você nem sabe do que se trata. A intenção aqui é ser um repositório de bons hábitos na programação em Python que pode ser usado por você. Não precisa ser utilizado a risca, mas neste curso, será.

Você não precisa seguir essas recomendações, mas será bom aprende-las desde o início. Ficará natural e fácil com o aprender da programação. 


Quando explicação de cada tópico for mostrada nas aulas seguintes, irei relembrar desse artigo para que vc de uma ohada e veja o que estou dizendo. Eu ireir enfatizar as formas mostrdas  aqui, mas como lá terá muito mais conteúdo, aqui fica um arquivo só com o essencial de cada bom hábito e não a explicação do que significa cada assunto. 

## - Uso de Comprehension 

Essa questão é um pouco complicada. Usar comprehensions facilita a escrita e reduz muito o código e é a forma pythonica de criar listas, dicionários, conjuntos. Podem ser usados dentro de loops também.

A questão é que dependendo da forma que é escrito, o código pode ficar não muito legível. Segui o PEP8, como é feito aqui, pode ajudar, mas nem toda hora é preciso utilizar comprehensions. 

Vai de caso a caso essa questão. O mais importante aqui é tentar deixar o comprehension mais legível possível, ainda mais que muitas linguagens de programação não possuem esse recurso e pode ficar ainda mais difícil nesses casos.

Veja exemplos de como usar comprehensions, lembrando que pode mudar dependendo do caso.

```python
# Sem comprehension.
quadrados: list[int] = []

for i in range(5):
    quadrados.append(i ** 2)

print("Sem List Comprehension:", quadrados)

# Forma boa com list comprehension
quadrados_comprehension = [i ** 2 for i in range(5)]
print("Com List Comprehension:", quadrados_comprehension)

# Forma ruim com comprehension
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4) if i % 2 == 0]
print(matriz)

# Forma ruim sem comprehension
matriz: list[int] = []

for i in range(1, 4):

    if i % 2 == 0:  
        linha = []

        for j in range(1, 4):
            linha.append(i * j)

        matriz.append(linha)

print(matriz)

```

## - Uso para iterações (loops)

### a) Não use range(len( ))

É possível e sem problemas usar o range(len( )), mas a melhor forma e mais inteligente é utilizar outras formas, mostradas abaixo.

A primeira forma é pensar que para acessar elemento de um iterador é preciso ser por indices, no python, não precisa. Basta colocar o iterador no loop.

```python
# Iterar com elementos - forma ruim.
list_num: list[int] = [1, 2, 3]

for i in range(len(list_num)):
    valor = list_num[i]

# Iterar com elementos - forma boa.

for i in list_num:
    print(i)

```

Caso queira o valor do índice para algum uso, ainda não use range(len( )), use enumerate( ), você consegueo índice e ,de brinde, o elemento.

```python
#Forma ruim
list_num: list[int] = [1, 2, 3, 4, 5]

for i in range(len(list_num)):
    print(i)

# Forma boa
list_num: list[int] = [1, 2, 3, 4, 5]

for indice, valor in enumerate(list_num):
    print(f'Indice: {indice} Valor: {valor}')
```

Caso esteja trabalhando com mais de um iterador, não use a mesma variável de interação para a iteradores diferentes, use o zip( ).

```python
#Forma ruim
list01: list[int] = [1, 2, 3]
list02: list[int] = [4, 5, 6]

for i in range(len(list01)):
    valor_list01= list01[i]
    valor_list02 = list02[i]

#Forma boa
list01: list[int] = [1, 2, 3]
list02: list[int] = [4, 5, 6]

for valor_list01, valor_list02  in zip(list01, list02):
    ...

```

Se ainda quiser ter os indices, utilize o enumerate( ) junto com o zip( )

```python
#Forma boa
list01: list[int] = [1, 2, 3]
list02: list[int] = [4, 5, 6]

for valor_list01, valor_list02  in enumerate(zip(list01, list02)):
    ...

```

### b) Bons usos de iterações com dicionários

É comum ver iterações com dicionários usando o comando .keys( ). Não é preciso, já que iterar com as chaves é o padrão.

```python
# Forma ruim
dictionary: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for key in dictionary.keys():
    ...

# Forma boa
dictionary: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for key in dictionary:
    ...

```

Não conhecer o comando items( ). Ele "salva"tando o valor das chaves quanto dos valores. Usar eles em vez de qualquer outra forma.

```python
# Forma ruim
dictionary: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for key in dictionary:
    val = d[key]

# Forma boa
dictionary: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for key, valor in dictionary.items():
    ...

```

Não precisa criar seu próprio contador de indíces e aumentá-lo ou diminuí-lo com += ou --, use enumerate( ) para isso.

```python
# Forma ruim
lista: list[int] = [1, 2, 3]

i = 0

for x in lista:
    print(i)
    i += 1

# Forma boa
lista: list[int] = [1, 2, 3]

for i, x in enumerate(lista):
    ...

```















## 7 - Uso ara programação orientada a objetos

## 7 - Padrões para algumas bibliotecas

## 8 - Padrões para a estrutura de projetos

## 11 - Padrão para filter, map e zip
