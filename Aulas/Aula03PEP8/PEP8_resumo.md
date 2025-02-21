# PEP8 - Style Guide for Python Code

PEP é uma sigla para Python Enhancement Proposals. Como nome diz são propostas para que a linguagem Python, com o objetivo de que a linguagem cresça e evolua cada vez mais.

A PEP8 foi criado com o objetivo de criar um padrão em qualquer código Python de qualquer sistema operacional. Todas as recomendações feitas pela PEP8 não precisam ser seguidas, mas é altamente recomendável que siga elas para o código ser mais legivel e bem apresentável.

Esse documento não tem como objetivo mostrar todas as recomendações da PEP8 e sim as mais importantes e mais corriqueiras.

Para acessar o documento oficial (em inglês), basta [clicar aqui](https://www.python.org/dev/peps/pep-0008/).

obs: Se estiver vendo esse arquivo sem saber nada sobre a linguagem, não fique assustado. Todas os termos e a sintaxe serão vistas posteriormente. O importante aqui é saber como funciona a PEP8 e como escrever código python de forma mais limpa e clara possível, para quando for escrever por conta própia, já saber a forma correta.

## Formatação do código

### indentação

Você pode estar ser perguntando o que é indentação. É uma forma de deixar o código mais legivel e definir a hierarquia entre os blocos de comando. Utilize sempre multiplos de 4 para isso.

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

### Linhas em branco

· Na hora de declarar uma classe ou função é recomendado que dê dois espaços em branco após o bloco de comando terminar.  
· Dentro das classes é recomandado que de um espaço em branco para separar os métodos, inclusive no construtor.  
· Entre os métodos da classe, utiliza somente um espaço para separa-los.

```python
class Classe:

    def__init__(self, teste):
        self.teste = teste

    def teste_teste(self):
        pass


def sub():
    pass



```

Todo script deve ser finalizado com uma linha em branco. Perceba que todo final de código tem uma e somente uma linha em branco, inclusive no final desse arquivo.

### Imports

O python possui um vasto conjunto de pacotes que podem ser importados para o seu programa (Alguns pacotes são necessário fazer a instalação outros já vem com a linguagem por deafault). Eles devem ser colocados no inicio do código, sendo os primeiros comandos ou depois de comentários iniciais que possam haver.

```python
import numpy as np
import matplotlib.pyplot as plt

```

Cada pacote deve ser declarada em uma linha. Mas podemos fazer um tipo diferente de import, na qual não importamos todo o pacote e sim algumas classes do pacote. Nesse caso, podemos importar várias classes numa mesma linha.

```python
from obsby import read
from numpy import fft, arange

```

## Nomes e identificadores  

Para cada objeto no Python existe uma maneira mais adequada de declaração. Podemos usar tando PascalCase como snake_case.

### Classes

As classes utilizam o padrão PascalCase, ou seja, a primeira letra de cada palavra é maiúscula e não são separadas por virgula ou _ , são 'coladas'.

```python
class Pessoa:
    pass


class SomaDeDoisNumeros:
    pass



```

### Funções e variáveis

As funções e variáveis seguem o padrão snake_case. Nesse caso, as palavras são todas em minúsculo, separdas por '_' .

```python
def funcao():
    pass


def multliplicacao_nums(num1, num2):
    return num1 * num2


fruta = 'maça'
conta_corrente = 1400

```
