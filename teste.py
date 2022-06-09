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