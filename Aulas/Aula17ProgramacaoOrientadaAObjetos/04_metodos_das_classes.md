# Métodos das classes 

Já vimos que métodos nada mais são que funções que ficam dentro de uma classe. Elas representam o
comportamento do objeto. 

Assim como os atributos, os métodos também possuem dois grupos: métodos de instância e de classe. Como pode perceber, 
funcionam com a mesma lógica dos atributos. veremos cada um agora:

## Métodos de instância

São métodos criados dentro da classe em que se pode acessar eles quando se cria um objeto, instância da classe. 

```Python
class User:

    def __init__(self, frist_name, last_name, altura, data_aniversario):
        self.frist_name = frist_name
        self.last_name = last_name
        self.altura = altura
        self.data_aniversario = data_aniversario

    def describe_user(self):
        """ faz um relatório com as informaçãoes do usuário """
        print(f"nome: {self.frist_name} {self.last_name}\naltura: {self.altura} metros\ndata aniversário: {self.data_aniversario}")

    
    def greet_user(self):
        print(f"Olá {self.frist_name} {self.last_name}, seja bem vindo!")
    

user_01 = User("Gabriel", "Cavalcanti", 1.70, "14/05/98")

user_01.describe_user()
user_01.greet_user()

```

```Pyhton
nome: Gabriel Cavalcanti  
altura: 1.7 metros        
data aniversário: 14/05/98
Olá Gabriel Cavalcanti, seja bem vindo!
```

foi criado dois métodos, describe_user e greet_user. Para acessar eles fora da classe, primeiro é criado uma instância da classe
e depois, com a notação ponto, chama o método da classe utilizando o objeto criado, no caso user_01.

os métodos são funções, ou seja, tudo que as funções são capazes de fazer os métodos também fazem. Como estamos começando, os métodos somente "printam" algo, mas podem fazer quais quer coisas que a linguagem permita. 

## Métodos de classe

Funciona com a mesma lógica que os atributos de classe. Somente a classe tem acesso ao método e precisa colocar um decorador para 
que funcione. 

Além disso, não se utiliza a palavra self e sim cls. Não estamos mais relaciondo com o objeto da classe e sim com a classe em si, então é preciso passar como parâmetro o cls (classe) e não mais o self. Como não passamos mais o self, nenhum dos atributos do construtor podem ser utilizados dentro de um método de classe.

Ele utiliza como parâmetro obrigatório a palavra cls, que indica a própia classe. Esse tipo de método faz referencia a própia classe e não ao objeto, que nem o self faz.

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

```Python
Ele já comeu
Esta vivo
```

### Criando objetos a partir de um arquivo .csv

Muitas vezes não iremos instanciar um objeto diretamente, muitas vezes quando a quantidade de objetos é muito grande. Utilizamos um aqruivo .csv
que contém todos os objetos e utilizamos um método de classe para adcionar os obejtos e colocalos dentro de uma lista (como pode ser visto emum tópico mais a frente nesse pdf). 

Para adcionar objetos a partir de um arquivo .csv, primeiro precisamos importar a biblio teca csv e utilizar esse método de classe.

```Python
import csv

class Item:
   
   all = []

   def __init__(self, name: str, price: float, quantity: int):
      self.name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("arquivo.csv", 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity'),
            )
    
    def __repr__(self):
      return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


Item.instanciate_from_csv()
print(Item.all)
```

## Alterando valores de atributos com métodos

Agora vamos ver como aletrar o valor de atributos com os métodos. Vamos utilizar a classe dos carros, utlizadas na aula de 03_atributos_de_classe.md

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

Se quiser deixar o programa mais complexo, podemos colocar uma condição de alterar o valor do odometro. Já que pode ser um valor menor, vamos adcionair isso ao programa.

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

## Criando uma lista com todos os objetos criados

É possível adcionar uma lista com os objetos criados e a partir dai utilizar os métodos das listas a nosso favor. Primeiramente iremos criar um atributo de classe que será uma lista vazia. Em seguida, vamos utilizar o construtor para adicionar esses novos elementos. 

```Python
class Item:
   
   all = []

   def __init__(self, name: str, price: float, quantity: int):
      self.name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)

print(Item.all)

```

```Python
[<__main__.Item object at 0x000002C950B2AEF0>, <__main__.Item object at 0x000002C950B2BBE0>, <__main__.Item object at 0x000002C950B2BEB0>]
```

Perceba que os objetos foram adicionados a lista. Por enquanto o nome da instância e esse código na memória péssimo de vizualizar (vamos mudar isso daqui a pouco) e não fizemos nada com eles ainda. Vamos mudar essas duas coisas agora. Para colocar um vizual mais legal para os objetos, vamos utilizar o **__rept__** e darei uma amostra do que é possível fazer com a lista de objetos.

```Python
class Item:

   all = []

   def __init__(self, name: str, price: float, quantity: int):

      self.name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)
       

   def __repr__(self):
      return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)

print(Item.all)

for instance in Item.all:
   print(f"Item: {instance.name}, Preço: {instance.price}, quantidade: {instance.quantity}")

```

```Python
[Item('Phone', 100, 1), Item('Laptop', 1000, 3), Item('Cable', 10, 5)]
Item: Phone, Preço: 100, quantidade: 1
Item: Laptop, Preço: 1000, quantidade: 3
Item: Cable, Preço: 10, quantidade: 5

```

## Métodos estáticos 

Assim como os métodos de classe, eles tmb precisam de um decorador para funcionar. Eles servem para realizar funções que se relaciona com a
classe e não com as instâncias. É uma diferença muito sutil com relação aos métodos de classe, já que nos métodos de classe tmb são funções relacionas a classe, mas utilizamos ela para manipular diferentes tipos de estrututas para instanciar objetos, os métodos estáticos não tem nafa haver com instâncias, elas não participam do rolê. 

Para dizer que é um método estático, utilizamos o decorador @staticmethod. E como eles não tem havem com as instâncias, não utilizamos o self e muito menos o cls, apenas parâmetros normais de uma função qualquer. 

```Python
class Item:

   all = []

   def __init__(self, name: str, price: float, quantity: int):

      self.name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)
    

   @staticmethod
   def is_numeric(num):
        if isinstance(num, float):
            print("It is numeric")
        elif isinstance(num, int):
            print("It is numeric")
        else:
            print("It is not numeric")
 

Item.is_numeric(3)
Item.is_numeric("oi")
```

```Python
It is numeric
It is not numeric
```

Obs: Podemos instânciar os métodos de classe e estático a partir de objetos, mas não é recomendado, utilize apenas a partir de classes, como mostrado no exemplo anterior e em todos os outros exemplos.
