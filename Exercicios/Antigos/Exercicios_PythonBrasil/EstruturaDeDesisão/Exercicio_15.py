"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Tamanho do lado do triângulo: "))
lado2 = float(input("Tamanho do lado do triangulo: "))
lado3 = float(input("Tamanho do lado do triangulo: "))

soma1 = lado1 + lado2
soma2 = lado1 + lado3
soma3 = lado2 + lado3

print()

if soma1 > lado3 or soma2 > lado2 or soma3 > lado1:
    if lado1 ==  lado2 == lado3:
        print("É um triângulo Equilátero.")
    elif lado1 != lado2 != lado3:
        print("É um trângulo Escaleno")
    elif lado1 ==  lado2 or lado2 == lado3 or lado1 == lado3:
        print("É um triângulo isoceles")
    else:
        print("Erro")
else:
    print("Não é um triãngulo")

