"""
b) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""

side_triangle_01: int = int(input("Digite o lado do triângulo: "))
side_triangle_02: int = int(input("Digite o lado do triângulo: "))
side_triangle_03: int = int(input("Digite o lado do triângulo: "))

if (side_triangle_01 + side_triangle_02 > side_triangle_03) and (side_triangle_01 + side_triangle_03 > side_triangle_02) and (side_triangle_02 + side_triangle_03 > side_triangle_01):
    print("Os valores formam um triângulo!")

    # Verificando o tipo de triângulo.
    if side_triangle_01 == side_triangle_02 == side_triangle_03:
        print("Triângulo Equilátero: todos os lados iguais.")

    elif side_triangle_01 == side_triangle_02 or side_triangle_01 == side_triangle_03 or side_triangle_02 == side_triangle_03:
        print("Triângulo Isósceles: dois lados iguais.")

    else:
        print("Triângulo Escaleno: todos os lados diferentes.")
        
else:
    print("Os valores não formam um triângulo.")
