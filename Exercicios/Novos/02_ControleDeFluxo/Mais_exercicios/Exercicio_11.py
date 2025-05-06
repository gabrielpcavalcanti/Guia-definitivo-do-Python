"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro 
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com 
a tabela abaixo: 

CONSUMO (Km/l")       MENSAGEM 
menor que 8       Venda o carro!
entre 8 e 14        Económico! 
maior que 12     Super económico! 
"""

distance: float = float(input("Digite a distância percorrida: "))
litros: float = float(input("Digite a quantidade de litros consumidos pelo carro: "))

fuel_consumption: float = distance / litros

if fuel_consumption < 8:
    print("Venda o carro.")

elif fuel_consumption >= 8 and fuel_consumption < 14:
    print("Econômico.")

elif fuel_consumption > 12:
    print("Super econômico.")
