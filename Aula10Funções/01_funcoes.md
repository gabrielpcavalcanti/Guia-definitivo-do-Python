# Funções

A medida que os códigos escritos em qualquer linguagem ficam mais complexos é necessário utilizar uma artimanha para reduzir o tamanho e melhorar
a leitura dos scripts. É ai que as funções entram. Elas servem para não ter a necessidade de repitir um certo conjunto de blocos e deixar o código
mais limpo e bem escrito.

Uma função são pequenos trechos de código que realizam tarefas específicas.

Uma função bem escrita é aquela que executa uma e somente uma tarefa. Funções que fazem mais de uma coisa precisam ser desmebradas para um melhor
funcionamento do código.

As funções seguem o princípio DRY - Don`t repete yourself. Você cria um bloco de código que pode ser utilizado em qualquer parte do seu programa ou em até
outros lugares, dando origens as bibliotecas. Por esse e outros motivos, as funções são muito importantes.

Durante o apredizado do Python, desde o início, na verdade, utilizamos funções bilt-in, como o print( ), len( ), max( ), upper( ), input( ).
Perceba que elas execultam uma única função e não mais de uma.

Não é porque uma função exuculta uma única tarefa que é precisa ser uma única linha, pelo contrário, uma funcão é um bloco de comando que tem a
função de realizar determinado objetivo. Esse bloco de comando pode ter funções bilt-in, uma outra função ou código próprio.

Para declarar uma função, usamos a palavra reservada **def** seguida do nome da função mais os ( ), que podem ter parâmetros ou não (Veramos mais
a frente).

```python
def hello_world():
    """ Imprime Hello World na tela"""
    print("Hello World")


hello_world()    
```

```python
Hello world
```

Obs: Para seguir o PEP8, nome de funções são todos em minúsculas e se for palavras compostas separa elas com _. Depois que o bloco de comando
ter terminado, da um espaço de duas linhas para continuar a escrita do código.

Obs: Definir uma função não muda em nada no andamento do código. Para que ela seja utilizada em algum lugar do código, é preciso chama-la, por isso o hello_world().
Caso a função tenha parâmetros, é preciso coloca-los quando a função é chamada.
