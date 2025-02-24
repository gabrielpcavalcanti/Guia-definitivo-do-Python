# Arquivos - abertura, leitura e fechamento 

Entramos numa parte da programação em Python bastante interessante, pelo menos na minha opinião. Ela abre muitas possibilidades dentro desse universo. Podemos fazer diversas coisas com arquivos, como a leitura, escrita, criação e de manipulação de dados dentro de arquivos. Vamos ver cada uma por partes. 

## Abertura de arquivos 

A primiera coisa que é preciso saber é como abrir um arquivo. Utilizamos a função integrada open( ). Ela possui diversos parâmetros
opcionais e apenas um parâmetro obrigatório, que é o nome ou caminho do arquivo. Lembre-se que o arquivo precisa existir para poder 
ser aberto e/ou o caminho tem que ser correto. Caso utilize o nome do aquivo, ele tem que estar na mesma pasta do arquivo .py, caso contrário, é preciso utilizar o caminho para poder ser aberto.

```Python
arquivo = open("texto_teste.txt")
```

```Python
arquivo = open("C:\\Users\\gabri\\OneDrive\\Documentos\\GitHub\\Python_teoria\\Aula14Arquivos\\texto_teste.txt")
```

A função open( ) possui diversos parâmetros opcionais, mas os mais importantes são o name, que é o nome do arquivo; o modo dele, que o que escolhemos fazer com arquivos (veremos mais a frente); e o encoding, que é a formatação do texto. Sempre utilize UTF-8, vai facilitar a sua vida.

o tipo do arquivo resultante da função open( ) é o <class '_io.TextIOWrapper'>, so para saber que a única coisa que fizemos até agora foi abrir e mais nada, veremos agora diversas coisas que podemos fazer com os arquivos.

## Leitura de arquivos 

Assim que abrimos um arquivo, escolhemos o que queremos fazer com ele. Por padão, o modo será de leitura: 'r'. Mas para ler, é preciso utilizar o método read( ). Ele lerá tudo que estiver dentro do arquivo. 

```Python
arquivo = open("texto_teste.txt", mode='r')

print(arquivo.read())
```

```Python
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

A leitura de arquivos no Pyhton funciona da seguinte maneira: O cursos do teclado começa a ler o arquivo, linha por linha. Assim que ele terminar de ler, o cursor para e fica lá. Caso tente ler o arquivo novamente dentro da mesma execução do programa, não 
irá acontecer nada, já que o cursor está numa linha vazia e começa a ler a partir dalí. 
 
Caso queiramos ler o arquivo diversas vezes, uma possibilidade é a colocar o .read( ) dentro de uma variável. Assim é possível ler várias vezes.

O tipo da váriável que será criada é uma String. Como é uma string, podemos utilizar todos os métodos que ela suporta, lembre-se disso.

```Python
arquivo = open("texto_teste.txt") 

ler_arquivo = arquivo.read()

print(ler_arquivo)
print(ler_arquivo)

```

```Python
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

Caso queira ler uma certa quantidade de caracteres, coloque o número dentro do argumento do método read( ).

```Python
arquivo = open("texto_teste.txt") 

print(arquivo.read(50))
```

```Pyhton
Lorem ipsum dolor sit amet, consectetur adipisci e
```

### Movimentar o cursos com o método seek

Caso não queira utilizar uma variável para ficar lendo o arquivo, uma outra opção é utilizar o método .seek( ). Ele vai colocar o cursorna posição que quiser e assim que o arquivo for lido novamente, começará a partir daquele ponto. O número 0 representa a primeira posição.

```Python
arquivo = open("texto_teste.txt") 

print(arquivo.read())

arquivo.seek(0)

print(arquivo.read())

```

```Python
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

### Ler uma ou várias linhas 

Temos uma maneira de ler uma linha por completo dentro, utilizando o método readline( ). ele lê uma linha é coloca o cursor na 
linha de baixo.

```Python
arquivo = open("texto_teste.txt") 

print(arquivo.readline())

```
```Python
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. 
```

Caso queira adicionais mais linhas, lendo elas por inteiro, basta colocar mais .readline( ) no programa. Utilize um laço for para 
ficar mais elegante.

```Python
arquivo = open("texto_teste.txt") 

for i in range(2)
    print(arquivo.readline())


```

```Pyhton
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. 

Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
```

Caso queira saber a quantidade de linhas do aquivo, utilize a função len( ) junto com o método .readlines( ).

```Python
arquivo = open("texto_teste.txt") 

print(len(arquivo.readlines()))

```

```Python
4
```

## Contar a quantidade de carcateres no texo

Se o arquivo lido for do tipo .txt, é possível utilizar uma função para saber quantos caracters o texto possui.

```Python
arquivo = open("texto_teste.txt")

arquivo.read()

print(arquivo.tell())
```

```Python
458
```

## Fechar o arquivo

Assim que terminamos de fazer todo o trabalho dentro de um arquivo, é preciso fecha-lo para que não haja erros. Usamos o método close( ) para isso. 

```Python
arquivo = open("texto_teste.txt") 

print(len(arquivo.readlines()))

arquivo.close()

```

```Python
4
```

Caso queira verificar se o arquivo está fechado ou não, basta usar o método closed. Ele retorna um valor booleano (use isso ao seu favor também).

```Python
arquivo = open("texto_teste.txt") 

print(len(arquivo.readlines()))

print(arquivo.closed)

arquivo.close()

print(arquivo.closed)

```

```Python
4
False
True
```

Assim que você fechar um arquivo, é preciso abri-lo novamente, caso queira mexer nele, caso contrário, dará erro.

## Abertura de arquivos com o bloco with

Até agora estamos utilizando a seguinte maneira para trabalhar com arquivos:

1 - Abrimos eles
2 - Trabalhamos com eles
3 - Fechamos eles

Nenhum problema em relação a isso, mas existe uma meneira pythônica de fazer esse processo. Utilizando o bloco with.
Ele abre o arquivo, dentro do bloco de comando, os processos são execultados e assim que sair do bloco, o arquivo é fechado automaticamente.

```Python
with open(texto_teste.txt) as arquivo:
    print(arquivo.read())

print(arquivo.closed) # Coloquei aqui so para que verifique que o arquivo realmente está fechado.

```

```Python
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur.
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
True
```
