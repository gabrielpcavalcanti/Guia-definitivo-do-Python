"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro 
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com 
a tabela abaixo: 

CONSUMO (Km/l")       MENSAGEM 
menor que 8       Venda o carro!
entre 8 e 14        Económico! 
maior que 12     Super económico! 
"""

distancia = float(input("digite a distância percorrida: "))
litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))

consumo_km = distancia / litros_consumidos

if consumo_km < 8:
    print("Venda o carro.")

elif consumo_km >= 8 and consumo_km <= 14:
    print("Econômico")

elif consumo_km > 12:
    print("Super econômmico")

