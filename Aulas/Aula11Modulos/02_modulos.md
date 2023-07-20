# Módulos Python

Módulos são arquivos em python, ou seja, todo arquivo python é um módulo, mas utilizamos o termo módulo para um arquivo que contém classes, funções com um objetivo em comum e que podem ser utilizados no código via importação.

Qualquer um pode criar módulos em Python para seram utilizados no própio código ou disponibilizar para que outras pessoas utilizem.

## Módulos Padrão Python

Alguns módulos são ditos padrões do pyhton porque não necessita a sua instalação, somente a importação. Eles não fazer parte da linguagem padrão do Pyhton, mas podem ser importados facilmente.

### Exemplos

* os
* sys
* time
* math
* turtle
* tkinter
* random

## Importar módulos

Há duas formas de importar módulos ou pacotes (Veremos depois) no Python.

A primeira utiliza a palavra reservada import "nome do módulo".

```python
import os
import math
```

Dessa forma, todas as funções, classes serão importadas para o seu programa. Não é recomendado fazer dessa maneira porque ocupa muita memória desnecessáriamente.

Nesse tipo de importação, é necessário colocar o nome do módulo/pacote antes de função que ele contem.

```python
import os
import math

print(math.pi)
print(math.sqrt(4))

```

```Python
3.141592653589793
2.0
```

O segundo tipo de importação utiliza a forma:  from "nome do módulo" import "funções".
Nesse caso, importamos somente as funções que iremos utilizar no código, otimizando o espaço de memória.

Não é necessário colocar o nome do módulo/pacote antes da função. Como importamos a função, ela não precisa ser refêrenciada.

```python
from random import random, randrange
  
print(random()) 
print(randrange(0, 101, 2))

```

```Python
# Qualquer número de 0.0 a 1.0
# Qualquer número interiro de 0 a 100.
```

Caso importe muitas funções de um mesmo módulo ou pacote, é costume colocar eles dentro de uma trupla.

```python
from random import (random, randrange, randint, choice)
```

Existe a possibilidade de importar todas as funções do módulo/pacote utilizando a segunda forma, basta colocar *.

```python
from tkinter import *

root = Tk() # Com o import tkinter, seria: root = tkinter.Tk()
```

A diferença dessa forma para a primeira e que não precisamos colocar o nome do módulo/pacote antes da função, diferentemente do import.

Independente da forma que importar, podemos dar ao modulo/pacote um apelido, simplificando nomes grandes, utilizando o comando: as "nome do apelido"

```python
import random as rm
import tkinter as tk
from math import factorial as fac, degrees as deg
```

Obs: O apelido não pode ser uma palavra reservada da linguagem nem uma variável que for criada depois.
