# Atributos das classes 

Já vimos o que é classe e entendemos de início o que são atributos. Relembrando: atributos são caracerístcas do objeto.  

existem três grupos de atributos: O de instância, de classe e os dinâmicos. 

## Atributos de instância

Esse tipo de atributos fica dentro de um método especial chamado de "construtor". Para definir o construtor é necessário utilizar a palavra reservada \__init( )__. 

Toda classe terá esse método, invariavelmente. E como o construtor é uma função, precisamos definir ela da mesma forma que fazemos em uma função normal.

```Python
class Cachorro:
    
    def __init()__():
```

os atributos que desejamos colocar na classe ficam dentro dos parâmetros da função \__init( )__. 

Só que antes disso, precismoas entender uma coisa, todo método dentro de uma classe possui como primeiro parâmetro uma palavra que vai ser utilizada para se auto referenciar dentro do classe. Utilizamos a palavra "self" para esse fim. Podemos utilizar qualquer outra, mas é uma convensão entre todos os programadores que utilizam Python.

Então o primeiro parâmetro será o self e em seguida todos os outro atributos da classe.

```Python
class Cachorro:
    
    def __init__(self, nome, cor, tamanho, raca):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.raca = raca
```

Entenda: quando utilizamos o self.atributo estamos dizendo o seguinte, o atributo x da classe y recebe x. Percebe que ele está se auto referenciado, ou seja, utilizando um atributo (self) para representar outros atributos dele mesmo. 

O self da acesso aos atributos da classe a um objeto/instância individual. Ele faz isso de forma automática. 

todos as variáveis prefixadas com o self estarão disponíveis em todos os outros métodos da classe. 

É algo confuso de se entender no início, mas com o tempo e prática você verá que faz sentido.

### Declarando um objeto/ instâncias

Quando a classe possuir um contrutor, é necessário colocar todos os parâmetros desse método na objeto, com exessão do self. Caso coloque um a mais ou um a menos, dará erro.

```Python
class Cachorro:
    
    def __init__(self, nome, cor, tamanho, raca):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.raca = raca
    

doguinho_01 = Cachorro("toto", "preto", 0.48, "pitbull")
doguinho_02 = Cachorro("lala", "branco", 0.25, "maltês")
```

O Python executa o construtor automaticamente sempre que criamos um novo objeto de uma classe.

para acessar os atributos de uma determinada instância, utilizamos da mesma forma que para acessar o método de uma função (que no fundo é uma classe), ou seja, utilizando a notação ponto. 

Após acessar um atributo, podemos fazer qualquer coisa que a tipo da variável permita, ou seja, podemos acessar qualquer método que o tipo da variável suporta. Fazemos isso, novemente, pela notação ponto. 

```Python
class Cachorro:
    
    def __init__(self, nome, cor, tamanho, raca):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.raca = raca
    

doguinho_01 = Cachorro("toto", "preto", 0.48, "pitbull")
doguinho_02 = Cachorro("lala", "branco", 0.25, "maltês")

print(doguinho_01.nome)
print(doguinho_02.tamanho)

print("A raça do meu cachorro é " + doguinho_02.raca.title())

```
```Python
toto
0.25
A raça do meu cachorro é Maltês
```

### Atributos públicos e privados

No pyhton todos os atributos de uma classe são públicos, mas caso queria avisar que um determinado atributo é privado, uiizamos __ antes de qualquer nome do atributo.

Ainda sim é possível acessar o atributo privado fora da classe, mas para isso funcionar é preciso utilixar esse "truque": _NomeDaClasse__nome_do_atributo_privado. Caso não faça isso, dará erro. 

Em outras linguagens de programação e impossíve acessar um atributo privado fora da classe, o Pyhton não faz isso.

```Python
class Carro:

    def __init__(self, cor, marca, tamanho):
        self.cor = cor #público
        self.__marca = marca # Privado
        self.__tamanho = tamanho # Privado

carro_01 = Carro("vermelho", "BMW", 2.3)

print(carro_01.cor)
print(carro_01._Carro__marca)
print(carro_01._tamanho) # Dará erro

```

## atributos de Classe

São atributos declarados fora do construtor. Nada mais são variáveis que podemos utilizar em qualquer método da classe. 

Colocamos eles antes do construtor e para chamar ele dentro de um método, incluindo o construtor, chamamos o NomeDaClasse.nome_do_atributo.

```Python

Class Produto:

    imposto = 1.5 # Atributo de classe.

    def __init__(self, nome, marca, funcao, valor):
        self.nome = nome
        self.marca = marca
        self.funcao = funcao
        self.valor = valor + (Produto.imposto * valor)
```

Utilizamos o atributo imposto dentro do construtor e não precisamos declarar ele dentro dos parâmetros. Ele pode ser usado dentro de qualquer método, basta chamar ele pelo nome_da_classe.atributo_de_classe.

## Alterando valores de atributos

Há três maneiras de alterar um valor de atributos: uma diretamente e as outras duas através de métodos. Vamos ver a primeira maneira aqui.

primeira vamos definair uma classe que representa um carro (nossa entidade, nesse caso).

em seguida é criado um valor default. Ele é o atributo que será alterado durante o programa. Podemos definir ele dentro do construtor ou fora dele, atributo de instância e de classe, respectivamente. Caso defina no construtor, não é preciso colocar nos parâmetros do construtor. 

```Python

class Car:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

carro = Car("BMW", "X6", 2021)

print(carro.odometro)

```
```Python
0
```

Agora para alterar o valor diretamente basta definir o novo valor fora da classe, da mesma forma que fazemos com variáveis. No fundo o parâmetro é uma variável, então funciona da mesma forma.

```Python

class Car:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

carro = Car("BMW", "X6", 2021)

carro.odometro = 50
print(carro.odometro)
```
```Python
50
```
