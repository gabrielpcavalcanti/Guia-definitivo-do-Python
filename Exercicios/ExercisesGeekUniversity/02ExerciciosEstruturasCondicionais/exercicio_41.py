"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de 
acordo com a tabela abaixo: 

IMC                      Classificação 
< 18,5                   Abaixo do Peso
18,6 - 24,9              Saudável
25,0 - 29,9              Peso em excesso 
30,0 -34,9               Obesidade Grau I 
35,0 - 39,9              Obesidade Grau II(severa)
40,0                     Obesidade Grau III(mórbida)
"""

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo do peso")

elif IMC > 18.6 and IMC < 24.9:
    print("Saudável")

elif IMC > 25 and IMC < 29.9:
    print("Peso em excesso")

elif IMC > 30 and IMC < 34.9:
    print("Obesidade Grau I")

elif IMC > 35 and IMC < 39.9:
    print("Obesidade Grau II(severa)")

elif IMC > 40:
    print("Obesidade Grau III(mórbida)")
