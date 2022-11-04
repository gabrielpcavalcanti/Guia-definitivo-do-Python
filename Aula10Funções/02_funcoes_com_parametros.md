# Funções com parâmetros

Algumas funções podem possuir parâmetros. Colocamos eles dentro dos ( ). As funções podem possuir quantos parâmetros necessitarem, 
mas é preciso colocar todos e na quantidade correta quando for declarar, caso contrário, terá erro.

```python
def soma( num1, num2):
    s = num1 + num2
    print(s)


soma(2,2)
```

```python
4
```

## Parâmetros posicionais

Os parânetros podem ser qualquer tipo de dado e devem ser colocados na ordem correta quando foram declarados. Caso a ordem for trocada e os tipos de
dados continuaem corretos, a função vai execultar sem nenhum erro, mas com parâmetros trocados.

```python
def nome(nome, sobrenome):
    """ Imprime o nome e sobrenome"""
    print(f'{nome} {sobrenome}')


nome('Rafael','nadal')
nome('Williams','Serena')
```

```python
Rafael nadal
Williams Serena
```

## Argumentos nomeados

Mesmo que o nome seja Serena e o sobrenome Williams, o python não sabe disso e executa na ordem em que os argumentos aparecem. Para evitar isso é
possível colocar o nome do argumento seguido de = no momento em for declarado.

```python
def nome(nome, sobrenome):
    print(f'{nome} {sobrenome}')


nome(nome='Rafael',sobrenome='nadal')
nome(sobrenome='Williams',nome='Serena')
```

```Python
Rafael nadal
Serena Williams
```

## Parâmetros com valores default 

Podemos criar funções com parâmetros padrão, default, eles recebem um valor inicial e não precisam ser colocados no momento da declaração. Caso queira mudar 
o valor, coloque ele no argumento e na ordem correta em que eles foram estabelecidos na função, ira embaralha, caso mude a ordem, cuidado!

```python
def meu_nome(nome='Gabriel', sobrenome='Cavalcanti'):
    print(f'{nome} {sobrenome}')


meu_nome()
meu_nome(nome='Rafael')
```

```python
Gabriel Cavalcanti
Rafael Cavalcanti
```

Caso a função tenha parâmetros padrão e parâmetros obrigatórios, eles sempre são colocados primeiros na construção da função, depois os
opcionais.

```python
def func(var1, var2, var3, var4=3, var=6);
    pass


```

Obs: Utilizmaos a palavra reservada **pass** para quando quisermos declarar a função ou classe, mas não mexer com ela no momento. Quando 
for trabalhar na função novamente é necessário retirar a palavra pass.

Obs: Caso não tenha notado, foi utilizado o nome parâmetro e argumento. Eles significam a mesma coisa, ou seja, são as variáveis que ficam dentro dos ( ). A diferença é que o nome parâmetro é usado na criação da função e o argumento, na declaração. É somente nomeclarura, mas significam a mesma coisa.