"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 
(basemaior + basemenor) * altura / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero. 
"""

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

if base_maior > 0 and base_menor > 0:

    area_trapazio = ((base_maior + base_menor) * altura) / 2
    print("O valor da área é " + str(area_trapazio))

else:
    print("Valores inválidos.")
