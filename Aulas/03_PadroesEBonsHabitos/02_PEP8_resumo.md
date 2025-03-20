# PEP8 - Style Guide for Python Code

PEP é uma sigla para Python Enhancement Proposals. Como nome diz, são Propostas de aprimoramento do Python, com o objetivo de que a linguagem cresça e evolua cada vez mais. Nem todos os PEP`s são aceitos e você não precisa ver e aprender todos, são inúmeros. Os mais importantes veremos durante o curso e a maioria deles nem serão citados. Caso queira ver todos, basta [clicar aqui](https://peps.python.org/pep-0000/).

A PEP8 foi criado com o objetivo de criar um padrão em qualquer código Python de qualquer sistema operacional. É uma forma mais elegante de se escrever e também uma forma pythonica ( forma de como os programadores gostam de escrever a linguagem python). 

O seguir o PEP8 para escrever na linguagem Python mostra profissionalismo. 

Todas as recomendações feitas pela PEP8 não precisam ser seguidas, mas é altamente recomendável que siga elas para o código ser mais legivel e bem apresentável. Não se prenda muito a ela, não fique querendo escrever códigos perfeitos, mas sempre é bom ter ela em mente e aprender o pyhton desde cedo usando ela para que torne natural e nem sinta que esteja usando. 

Durante projetos pessoais ou em uma empresa, é bom ter uma padrão definido para que todo mundo fale a mesma lingua e o código fique uniforme e seja legível. Mas o mais importante é: caso defina um padrão, siga ele por todo o códido, mesmo que esse padrão não siga o PEP8. Saiba quando ser inconsistente - algumas vezes, as regras deste guia 
simplesmente não se aplicam. Veja caso a caso.

Esse documento não tem como objetivo mostrar todas as recomendações da PEP8 e sim as mais importantes e mais corriqueiras.

Para acessar o documento oficial (em inglês), basta [clicar aqui](https://www.python.org/dev/peps/pep-0008/).

obs: Se estiver vendo esse arquivo sem saber nada sobre a linguagem, não fique assustado. Todas os termos e a sintaxe serão vistas posteriormente. O importante aqui é saber como funciona a PEP8 e como escrever código python de forma mais limpa e clara possível, para quando for escrever por conta própria, já saber a forma correta. 

obs: Sempre volte nesse arquivo para rever os principais pontos e toda vez que aprender algo novo na linguagem, veja se tem algo a repeito dela no PEP8. 

obs: Não precisa e nem deve decorar tudo descrito aqui, o guia de estilo será aplicado no decorrer do curso e será explicado também.


## 1 - Número de caracteres por linha

Existem moniores e monitores pelo mundo e muitos deles se limitam a linhas de 80 colunas, então o PEP8 segere que limite todas as linhas a um máximo de 79 caracteres.

Para longos blocos de texto (docstrings ou comentários), limitar o comprimento a 72 colunas é recomendado.

Usar esse limite também permite o uso de várias janelas abertas em um mesmo monitor.

## 2 - Identação

Utilize 4 espaços por nível de indentação. 

De preferencia, use espaço ao invés de tabulações. Pode dar problema e o espaço sempre é padrão para todos os computadores, o tab, não. 

Caso queira usar o tab, configure seu computador para que ele sempre dê 4 espaços e não 2 ou 5, por exemplo.

Se você estiver se perguntando o que é indentação. É uma forma de deixar o código mas legivel e definir a hierarquia entre os blocos de comando. Utilize sempre multiplos de 4 para isso.

Em outras linguagens de programação como C ou java utilizam o bloco de código por meio de { }. Em Python, um bloco de código é iniciado por : e na próxima linha (onde o bloco inicia), possui quatro espaços de indentação.  

É utlizado para criação de classes, funções, estruturas de controle (if e else) e estruturas de repetição (while e for) e mais.

O padrão é utilizar quatro espaços, mas se o TAB do seu computador estiver configurado para dar quatro espaços, pode utilizar o TAB. Não é recomendado. Sempre use os espaços para evitar problemas.

```python
if x>0:
    if x>3:
        print(x)
    else:
        print(x-1)
else:
    print(x * -1)

for i in range(5):
    int(input("Digite um número: "))

```

## 3- Linhas em branco

 Na hora de declarar uma classe ou função é recomendado que dê dois espaços em branco após o bloco de comando terminar. 

 Dentro das classes é recomandado que de um espaço em branco para separar os métodos, inclusive no construtor.  

 Entre os métodos da classe, utiliza somente um espaço para separa-los.

```python
class Classe:

    def__init__(self, teste):
        self.teste = teste

    def test_test(self):
        pass


class ClasseMath:
    pass


def sub():
    pass

```

Todo script deve ser finalizado com uma linha em branco. Perceba que todo final de código tem uma e somente uma linha em branco, inclusive no final desse arquivo.


## 4 - Comentários

Comentários devem sempre ser frases completas e sua primeira letra deve ser maiúscula, a menos que ele comece com um identificador que começa com uma letra minúscula.

```python
# Retorna o valor da soma dos números especificados na função.
def function(num_1, num_2):

    return num_1 + num_2

```

Se um comentário for curto, o ponto final deve ser omitido. Comentários grandes normalmente consistem de um ou mais parágrafos e sentenças completas, estas sim devem terminar com ponto.

```python
# Comentário curto
def function(num_1, num_2):

    return num_1 + num_2

```

Comentários em bloco devem ser indentados no mesmo nível do código a que se referem. Cada linha deve começar com # e um espaço (a menos que o texto dentro do comentário seja indentado). O bloco inteiro deve ser separado por uma linha em branco no topo e embaixo.

```python
import os

# Comentário em bloco
# exemplo de como o um comentário em bloco funciona.
# Veja se vale a pena usar ou não utilizar.

itens = os.listdir(".")

print("Arquivos e diretórios no diretório atual:")

for item in itens:
    print(item)

```

Comentários na mesma linha devem ser separados do comando por pelo menos dois espaços. Como outros comentários, devem começar com uma tralha e um espaço.


```python

print("Hello World!")  # Mostra a frase "Hello World!" no terminal.

```

## 5 - Imports

Eles devem ser colocados no inicio do código, sendo os primeiros comandos ou depois de comentários iniciais / docstrings que possam haver. Eles vem antes de constantes e variáveis globais, caso haja.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)

y = np.sin(x)

plt.figure(figsize=(8, 5))  
plt.plot(x, y, label="y = sin(x)", color="b")  

plt.show()

```

```python
"""
This script performs operations with files and directories using the os library.

Features:
- Lists files and directories in the current directory.
- Shows the current working directory.

Author: Your Name
Date: 03/15/2025
"""

import os  # Library for file and directory manipulation.

# Get and display the current working directory.
current_directory = os.getcwd()

print("Current directory:", current_directory)

# List files and directories in the current directory.
items = os.listdir(".")

print("\nFiles and directories:")

for item in items:
    print("-", item)

```

Cada pacote deve ser declarada em uma linha. Mas podemos fazer um tipo diferente de import, na qual não importamos todo o pacote e sim algumas classes do pacote. Nesse caso, podemos importar várias classes numa mesma linha.

```python
from obsby import read
from numpy import fft, arange

```

Caso tenha muitos importes de uma mesma bliblioteca, use esse padrão.

```python
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

```

Sempre use essa ordem na hora de importar bibliotecas: Primeiro as bibliotecas padrões, depois as externas e por fim as locais.

```python
import os  # Standart
import math  # Standart
import numpy as np  # external
from my_packege import module_01, module_02  # Local
    
```

E, por fim, evite usar "from bliblioteca import *", seja específico nos módulos e classes que queira importar.

## 6 - Nomes e identificadores  

Para cada objeto no Python existe uma maneira mais adequada de declaração. Podemos usar tando PascalCase como snake_case.

### Classes e exceções

As classes e exceções utilizam o padrão PascalCase, ou seja, a primeira letra de cada palavra é maiúscula e não são separadas por virgula ou _ , são 'coladas'.

```python
class MathError(Exception):
    pass


class DivisionByZeroError(MathError):
    pass


class Calculator:
    """Class for basic mathematical operations."""

    @staticmethod
    def divide(a, b):
        try:
            if b == 0:
                raise DivisionByZeroError("Error: division by zero is not allowed.")
            return a / b
        except DivisionByZeroError as e:
            print(e)
            return None  # Returns None in case of an error.

```

### Funções, variáveis e modulos

As funções e variáveis seguem o padrão snake_case. Nesse caso, as palavras são todas em minúsculo, separdas por '_' .

```python
import os

def function():
    pass


def multliplicacation_nums(num1, num2):
    return num1 * num2


fruit = 'maça'
checking_account = 1400

```

### Constantes

Todas em letras maiúsculas e separadas por _.

```python
PI = 3.141592
MAX_NUMBER_OF_CLOTHES = 10

```
## 7 - Espaços em expressões e instruções

Use algun desses padroões caso a linha tenha muito texto e sempre respeita a identação, como já vimos.

```python
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

Evite colocar espaço em determinadas situações vistas abaixo. Siga o que está escrito abaixo, que estara utilizando o PEP8.

```python
spam(ham[1], {eggs: 2})

if x == 4: 
    print x, y; x, y = y, x

spam(1)

dict['key'] = list[index]

x = 1
y = 2
long_variable = 3

# Outros exemplos

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

Sempre circunde os seguintes operadores binários com um único espaço de cada 
lado: =, ==, <, >, !=, <>, <=, >=, in, not in, is, and, or, not.

Não use espaços ao redor do sinal de igual (=) quando usado para indicar um valor padrão de um argumento. Faça assim, por exemplo: 

```python
def complexe(real, imag=0.0):
    return magic(r=real, i=imag)

```

Múltiplos comandos na mesma linha são desencorajados. Faça assim: 

```python
if foo == 'blah':
    do_blah_thing()

```

## 8 - Aspas duplas ou simples

Use aspas duplas para docstrigs. De resto, escolha um padrão e fique com ele.

```python
"""
This script shows the uses of quotation marks.

Features:
- shows double and single quotes in use.

Authorr: Seu Nome
Date: 15/03/2025
"""

# Para Strings, uso sempre aspas duplas.

nanem = "Gabriel"
surname = "Cavalcanti"
complete_name = "Gabriel Cavalcanti"

# Para f strigas, uso aspas simples.

name = "Alice"
age = 25

print(f'Olá, meu nome é {name} e eu tenho {age} anos.')

# Caso dentro de uma string tenha a necessidade do uso de aspas, use aspas dupas para a string e aspas simples dentro dela.

string_longa = "Uso das 'aspas simples' dentro de uma string"

# Se dentro de uma f string tenha o uso de aspas, use aspas duplas.

print(f'Olá, meu nome é "{name}" e eu tenho {age} anos.')

```

## Outras recomendações

### Uso de self e cls

O primeiro parâmetro dentro de um método dentro de uma classe é sempre self, e para @classmethod é sempre cls.

```python
class Teste:

    def __init__(self, parametro_1):
        pass


@classmethod
def method(cls):
    pass

```

### Comparações com singletons

Para None, True e False, use "is" ou "is not". ou invés de usar ==. Use "variável is not" em vez de "is variável not".

```python
idade = None

if idade is None:

if idade is not 14:


```

### Classes são sempre preferidas à strings, como em exceptions

Módulos ou pacotes devem definir sua própria classe-exception base, que deve ser uma subclasse da classe Exception. Sempre inclua uma docstring.

```python
class MessageError(Exception):
    """Base class for errors in the email package."""

```

### Use startswith( ) e endswith( )

```python
 
if foo.startswith('bar')  # Ao invés de if foo[:3] == 'bar':.

if foo.endswith('bar')  # Ao invés de if foo[3:] == 'bar':.
```

### Comparações de tipo de objetos 

Devem sempre usar isinstance() ao invés de comparar tipos diretamente. 

```python

if isinstance(obj, int):  # E não if type(obj) is type(1):

```

### Não compare valores booleanos com True e False usando ==

```python
greating = True

if greeting:
    
```

---
