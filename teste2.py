class Animal:

    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def andar(self):
        return f"O animal {self.nome} anda"


class Terrestre(Animal):

    def __init__(nome, idade, especie, anda=True):
        super().__init__(nome, idade, especie)
    
    def andar(self):
        return f"O animal terrestre {self.nome} anda"

class Cachorro(Terrestre, Animal):

    def __init__(self, nome, idade, especie, raca):
        super().__init__(nome, idade, especie)
        self.raca = raca

    def andar(self):
        return f"O cachorro {self.nome} anda"


rex = Cachorro("rex", 4, "Canis lupus familiaris", "maltês")
print(rex.andar())

#```Python

#```