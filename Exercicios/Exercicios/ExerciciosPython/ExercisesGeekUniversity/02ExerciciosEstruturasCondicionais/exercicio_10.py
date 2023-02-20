"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu 
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura): 
• Homens: (72.7 * h) — 58 
• Mulheres: (62.1 * h) — 44.7
"""

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M - masculino, F - feminino):")

if sexo == 'M' or 'm':
    peso = (72.7 * altura) - 58
    print()
    print(f'Seu peso ideal é: {peso}')

elif sexo == 'F' or 'f':
     peso = (62.1 * altura) - 44.7
     print()
     print(f'Seu peso ideal é: {peso}')

else:
    print("Digite M ou F")

