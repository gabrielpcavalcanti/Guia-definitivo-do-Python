# Python Good Habits

Durante meu estudo de Python, assisti vários cursos,vídeos e li muitos fóruns mostrando formas melhores de escrever em Python. Cada um tem um estil próprio, mas a comunidade prefere de uma maneira e mais importente é seguir um padrão definido por você e/ou pela empresa/projeto que está atuando. 

Separei aqui varias dessas formas de escrever melhor o código para várias áreas dentro da linguagem Python. Não se preocupe em decorar tudo porque provavemente muitas dos tópicos aqui você nem sabe do que se trata. A intenção aqui é ser um repositório de bons hábitos na programação em Python que pode ser usado por você. Não precisa ser utilizado a risca, mas neste curso, será.

Você não precisa seguir essas recomendações, mas será bom aprende-las desde o início. Ficará natural e fácil com o aprender da programação. 


Quando explicação de cada tópico for mostrada nas aulas seguintes, irei relembrar desse artigo para que vc de uma ohada e veja o que estou dizendo. Eu ireir enfatizar as formas mostrdas  aqui, mas como lá terá muito mais conteúdo, aqui fica um arquivo só com o essencial de cada bom hábito e não a explicação do que significa cada assunto. 

## 1 - Uso de Comprehension 

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

## 2 - Uso para iterações (loops)

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

## 3 - Uso de funções

Existem certas características que toda as funções deveriam ter. No dia a dia da programação, nem sempre é fácil atingir esse ideal, na verdade pode ser bastente difícil.

Uma maneira que gosto de trabalhar e escrever um reascunho de código de uma função da maneira que conseguir, sem me preocupar com os concelhos mostrados aqui. Depois que escrevi e vi que está funcionando, aplico todos os concelhos até o código ficar bem escrito. 

Fazer esse processo não é uma tarefa simples e demanda prática. Siguindo os conselhos abaixo, ficara mais simples e saberá o que deve ser feito para que seu código deixe de ser um rascunho. 

### a) Devem apenas fazer uma única tarefa

Uma função sempre deve execultar uma única tarefa. Se ela faz mais de uma coisa, ela pode ser desmembrada para tarefaz isoladas. 

Para verificar que uma função está apenas executando uma tarefa, ela so deve execultar as etapas que estão a um nível de abstração do nome declarado da função. Isso não é uma tarefa tão simples, mas tenha isso sempre em mente.

Sempre se pergunte se pode separar ela em mais partes. Se separendo elas, a tarefa atribuida some, ela já está execultando a tarefa e não precisa mais ser desmembrada. Caso contrário, desmembre.

Uma função pode fazer mais de uma coisa e, pior ainda, fazer coisas que nem sabe que está acontecendo. Isso se chama side effects. Trasnsformando as função em apenas uma tarefa, reduz muito esse problema, mas algumas vezes pode ser que não resolva. Fique atento.

Algumas vezes ocorre o contrário. Existe duas funções ou mais que fazem a mesma coisa. Isso se chama duplicatas. Elas nunca são necessária e só confundem. Remova todas até que sobre uma.

### b) Uma função tem que ser pequena

Funções muito grandes tendem a ter mais de uma tarefa, que já vimos que não é o ideal, ficam mais difícil de ler e entender. Mantendo as funções curtas evitam que isso aconteça.

Além disso, funções não devem ter neasting e muitos blocos de if/else. No máximo dois blocos de identação. 

O número máximo de linhas recomendada para uma função e de 20 linhas.

### c) Tente contar uma história com suas funções

obedeça uma hierarquia no programa, sempre coloque funções mais gerais no incício e vá descendo com funções hierequicamente abaixo delas. Isso fará sentido e aprenta como se contasse uma história no seu código, fica mais organizado e elegante.

Essa "filosofia" faz parte do que chamamos de step-down rule. Detalhando um pouco mais: A ideia principal é que o código deve ser escrito de forma que o leitor entenda primeiro os conceitos de alto nível antes de mergulhar nos detalhes de implementação.

O código deve ser estruturado de cima para baixo, seguindo uma hierarquia lógica:

Comece com funções/métodos de alto nível (métodos devem descrever o "o que" o código faz, sem muitos detalhes). Em seguida detalhe as implementações conforme o código desce (As funções chamadas no nível superior devem ser definidas logo abaixo, explicando o "como").

Por fim, cada nível responde perguntas do nível acima, ou seja, se uma função chama outra, a implementação da função chamada deve aparecer logo abaixo.

### d) Poucos argumentos nas funções

Tente ao máximo ter a menor quantidade de argumentos possíveis. Se uma função necessita de argumentos, utilize, mas não crie argumentos inúteis.

Uma forma de fazer isso é escolhendo bem o tipo de dado escolhido para que possa reduzir os argumentos. Por exemplo, ter agumentos separados podem ser unidos numa lista, caso faça sentido.

## 7 - Uso ara programação orientada a objetos

## 7 - Padrões para algumas bibliotecas

## 8 - Padrões para a estrutura de projetos

## 11 - Padrão para filter, map e zip
