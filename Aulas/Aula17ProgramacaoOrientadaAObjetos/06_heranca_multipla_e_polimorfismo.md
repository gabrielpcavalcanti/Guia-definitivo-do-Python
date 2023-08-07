# Herança múltipla e polimosrfismo

Como o nome indica, é a possibilidade de uma classe herdar mais de 
uma classe. Pode ser quantas quiser, não a limite de herança.

Obviamente a classe filha herdará todos os atributos e métodos das classes mães.

Há duas maneiras de realizar a herança múltiplas: por multiderivação direta e por multiderivação indireta, vamos ver cada uma.

## Multiderivação direta

Quando a herança é feita de forma direta, simples assim.

```Python
class mae1:
    pass

class mae2:
    pass

class maee3:
    pass

class filha(mae1, mae2, mae3):
    pass
```

A classe filha herda todos as atributos e métodos das classes mae1, mae2 e mae3.

## Multiderivação indireta

Ocorre quando você herda de uma classe que ja está herdando de outra, ou seja, a última classe filha recebe todos os métodos da classe mãe, mas a classe mãe é filha de outra classe mãe.  

```Python
class mae1:
    pass

class mae2(mae1):
    pass

class mae3(mae2):
    pass

class filha(mae3):
    pass
```

a classe filha recebe da classe mae3, que por sua vez recebe da mae2, que por sua vez, recebe da classe mae1. A herança é feita de forma indireta e a classe filha recebe todos os atributos e métodos das mae1, mae2 e mae3.

## MRO - Method Resolution Order

É um fenômeno que ocorre quando realizamos a herança múltipla. Ele indica qual o método que será execultado primeiro.

Quando herdamos os métodos da classe mãe e utilizamos ele na classe filha, o pyhton execulta o método da classe mãe, sem problemas aqui.

```Python
class Animal:

    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def andar(self):
        return f"O animal {self.nome} anda"

class Cachorro(Animal):

    def __init__(self, nome, idade, especie, raca):
        super().__init__(nome, idade, especie)
        self.raca = raca


rex = Cachorro("rex", 4, "Canis lupus familiaris", "maltês")

print(rex.andar())
```
```Python
O animal rex anda
```

### Polimorfismo

Agora quando criamos um método na classe filha com o mesmo nome de um método da classe mãe e criamos uma instância da classe filha, o python não mais execulta o método da classe mãe e sim o da classe filha. Esse processo é chamado de polimorfismo.

```Python
class Animal:

    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def andar(self):
        return f"O animal {self.nome} anda"

class Cachorro(Animal):

    def __init__(self, nome, idade, especie, raca):
        super().__init__(nome, idade, especie)
        self.raca = raca

    def andar(self):
        return f"O cachorro {self.nome} anda"


rex = Cachorro("rex", 4, "Canis lupus familiaris", "maltês")

print(rex.andar())
```

```Python
O cachorro rex anda
```
