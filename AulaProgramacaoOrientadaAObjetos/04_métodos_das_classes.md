# Métodos das classes 

Já vimos que métodos nada mais são que funções que ficam dentro de uma classe. Elas representam o
comportamento do objeto. 

Assim como os atributos, os métodos também possuem dois grupos: métodos de instância e de classe. Como pode perceber, 
funcionam com a mesma lógica dos atributos. veremos cada um agora:

## Métodos de instância

São métodos criados dentro da classe em que se pode acessar eles quando se cria um objeto, instância da classe. 

```Python
class User:

    def __init__(self, frist_name, last_name, altura, dataaniversario):
        self.frist_name = frist_name
        self.last_name = last_name
        self.altura = altura
        self.dataaniversario = dataaniversario

    def describe_user(self):
        """ faz um relatório com as informaçãoes do usuário """
        print(f"nome: {self.frist_name} {self.last_name}\naltura: {self.altura} metros\ndata aniversário: {self.dataaniversario}")

    
    def greet_user(self):
        print(f"Olá {self.frist_name} {self.last_name}, seja bem vindo!")
    


user_01 = User("Gabriel", "Cavalcanti", 1.70, "14/05/98")

user_01.describe_user()
user_01.greet_user()
```

foi criado dois métodos, describe_user e greet_user. Para acessar eles fora da classe, primeiro é criado uma instância da classe
e depois, com a notação ponto, chama o método da classe utilizando o objeto criado, no caso user_01.

os métodos são funções, ou seja, tudo que as funções são capazes de fazer os métodos também fazem. Como estamos começando, os métodos somente "printam" algo, mas podem fazer quais quer coisas que a linguagem permita. 

## Métodos de classe

Funciona com a mesma lógica que os atributos de classe. Somente a classe tem acesso ao método e precisa colocar um decorador para 
que funcione. 

Além disso, não se utiliza a palavra self e sim cls. Não estamos mais relaciondo com o objeto da classe e sim com a classe em si, então
é preciso passar como parâmetro o cls (classe) e não mais o self. Como não passamos mais o self, nenhum dos atributos do construtor podem ser utilizados dentro de um método de classe.

Ele utiliza como parâmetro obrigatório a palavra cls, que indica a própia classe. Esse tipo de método faz referencia a própia classe e não ao 
objeto, que nem o self faz.

```Python
class Pessoa:

    @classmethod # Decorador
    def vivo(cls, viver):
        if viver == True:
            print('Esta vivo')
        else:
            print('Esta morto')

    def __init__(self, nome, sobrenome, idade, comendo = True):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.comendo = comendo
    
    def esta_comendo(self):
        if self.comendo:
            print('Ele já comeu')
        else:
            print('Ele não comeu ')


pessoa_01 = Pessoa("Gabriel", "Cavalcanti", 230)

pessoa_01.esta_comendo() # Método de instância
Pessoa.vivo(True) # Método de classe
```

## Alterando valores de atributos com métodos

Agora vamos ver como aletrar o valor de atributos com os métodos. Vamos utilizar a classe dos carros, utlizadas na aula de 04_atributos_de_classe.md

É possível mudar de duas formas: definir o valor com um método ou incrementa-lo.

### por meio de métodos

criamos um método para alterar o valor do parâmetro. Há diversas formas de fazer isso, mas a mais simples é escolher um valor novo dentro do parâmetro do método e definir o valor do odometro como o valor do parâmetro. 

```Python

class Car:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0


    def ler_odometro(self):
        print(f"Odometro do carro: {self.odometro}")
    

    def atualizar_odometro(self, kmrodados):
        self.odometro = kmrodados


carro = Car("BMW", "X6", 2021)

carro.atualizar_odometro(50)
carro.ler_odometro()
```
```Python
Odometro do carro: 50
```

Se quiser deixar o programa mais complexo, podemos colocar uma condição de alterar o valor do odometro. Já que pode ser um valor menor, vamos adcionais isso ao programa.

```Python

class Car:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0


    def ler_odometro(self):
        print(f"Odometro do carro: {self.odometro}")
    

    def atualizar_odometro(self, kmrodados):
        if kmrodados >= self.odometro:
            self.odometro = kmrodados
        else:
            print("Não pode colocar um valor menor.")

carro = Car("BMW", "X6", 2021)

carro.atualizar_odometro(50)
carro.ler_odometro()

carro.atualizar_odometro(30)
```
```Python
Odometro do carro: 50
Não pode colocar um valor menor.
```

### por incremento 

Em vez de definir o valor do atributo, agora iremos incrementar o valor. Também existe diversas formas de fazer isso, mostrarei uma aqui.

```Python

class Car:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0


    def ler_odometro(self):
        print(f"Odometro do carro: {self.odometro}")
    

    def atualizar_odometro(self, kmrodados):
        if kmrodados >= self.odometro:
            self.odometro = kmrodados
        else:
            print("Não pode colocar um valor menor.")
    
    def incrementar_odometro(self, kmnovos):
        self.odometro += kmnovos

carro = Car("BMW", "X6", 2021)

carro.atualizar_odometro(24900)
carro.ler_odometro()

carro.incrementar_odometro(100)
carro.ler_odometro()
```
```Python
Odometro do carro: 24900
Odometro do carro: 25000
```

outra maneira de fazer é criando um atributo de classe como default e fazer o incremento dentro do construtor.

```Python
class Car:

    odometro = 0

    def __init__(self, marca, modelo, ano):
        self.incremento_odometro = Car.odometro + 1
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Car.odometro = self.incremento_odometro

carro = Car("BMW", "X6", 2021)

print(Car.odometro)

carro_2 = Car("BMW", "X6", 2021)

print(Car.odometro)
```
```Python
1
2
```
