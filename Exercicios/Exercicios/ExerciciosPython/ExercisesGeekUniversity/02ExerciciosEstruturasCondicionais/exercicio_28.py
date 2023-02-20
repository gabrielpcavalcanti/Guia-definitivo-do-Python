"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das 
seguintes médias de acordo com um valor numérico digitado pelo usuário: 

(a) Geométrica
(b) Ponderada
(c) Harmônica
(d) Aritmética
"""

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

media = input("Digite a média que quer calcular ((a) Geométrica (b) Ponderada (c) Harmônica (d) Aritmética)): ")

if media == "a":
    geometrica = ((a * b * c) ** (1/3))
    print(geometrica)

elif media == "b":
    ponderada = (a + 2*b + 3*c) / 6
    print(ponderada)

elif media == "c":
    harmonica = 1 / ((1/a) + (1/b) + (1/c))
    print(harmonica)

elif media == "d":
    aritimetica = (a + b + c) / 3
    print(aritimetica)

else:
    print("Valor inválido") 

