# Comentários

Os comentários são uma parte importantíssima de qualquer código. Um código não comentado tem a possibilidade de não ser compreendido por outra pessoa que não fez parte da criação do código.

Sempre comente o que faz determinado bloco ou funçao criada por você para que a pessoa que for ler, entenda do que se trata e consiga modificar ou ler seu código mais facilmente.

Os comentário não serão lidos pelo interpretador do Python. Eles estão lá para explicar o código e somente isso.

Comentários no python podem ser feitos de duas formas:

* A primeira é utilizando #. Esse tipo de comentário é de apenas uma linha. Se quisermos ter um comentário numa linha abaixo, é preciso utilizar outra #;

* O segundo tipo e utilizando três aspas dupas """ e fechando com mais três aspas duplas """ ou três aspas simples no começo e no final . Nesse caso, tudo que estiver dentro das aspas. será um comentário, ou seja, não será lido pelo interpretador.

Utiliza-se o segundo tipo de comentário para explicar funções. Chamamos nesse caso de docStrings (documentação da função). Falaremos de docString quando estudarmos funções.

```python
# Esse é um comentário de uma única linha. Ele não será lido pelo interpretador.

"""
Esse é um comentário de varias linhas.
Tudo que estiver dentro das aspas, será um comentário

"""

'''
Essa é outra forma de fazer comentários de várias linhas
Não é uma forma usual de fazer isso, mas é possível.

'''

```

```python
from obspy import read
import numpy as np


file = input("Digite o nome do arquivo: ")
sismograma = read(file)

dt = 1/sismograma[0].stats.sampling_rate

def filtro_passa_baixa(freq):

    for i in range(len(sismograma)): 
        a = sismograma[i].data

        F = np.fft.fft(a)
        w = np.fft.fftfreq(a.size, dt)

        F[abs(w) >= freq] = 0 

    return filtro_passa_baixa

```

Pergunte para você mesmo, entendeu o código acima?. Independendo do seu nível com a linguagem, qualquer código pode ser tornar complicado de entender, para isso que serve os comentário.

A seguir vc vai ver o mesmo exemplo com os comentários. Você verá que mesmo não entendendo a sintaxe do código ou o que está sendo tratado, vai entender para que ele serve.

```python
"""
Esse é um código que abre um arquivo .seg2, da sismologia, e aplica o filtro passa baixa no dado.
"""

# Essas são as bibliotecas necessárias para o código funcionar.
from obspy import read
import numpy as np

# lê o nome do arquivo e armazena numa variável.
file = input("Digite o nome do arquivo: ")
sismograma = read(file)

# calclua o tempo.
dt = 1/sismograma[0].stats.sampling_rate


def filtro_passa_baixa(freq):
    """
    Aplica o filtro passa baixa no dado aberto pelo usuário.

    :parâmetro: freq: define a frequência que será utilizada no filtro.

    :return: retorna a própia função.
    """
    for i in range(len(sismograma)): 
        a = sismograma[i].data

        F = np.fft.fft(a) # Calcula a transformada de Fourier.
        w = np.fft.fftfreq(a.size, dt) # Calcula as frequências.

        F[abs(w) >= freq] = 0 # aplica o filtro.

    return filtro_passa_baixa

```

Percebeu que ficou mais claro do que se trata esse código? Essa é a função dos comentários. Sempre utilize comentário nos seus códigos, para que outra pessoa ou você mesmo entenda do que ele se trata.
