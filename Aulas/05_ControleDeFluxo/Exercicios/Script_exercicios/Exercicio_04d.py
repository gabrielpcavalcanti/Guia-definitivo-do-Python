"""
d) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

a_coefficient: int = int(input("Digite o valor do coeficiente a: "))

if a_coefficient == 0:
    print()
    print("equação não é do segundo grau.")

else:
    b_coefficient: int = int(input("Digite o valor do coeficiente b: "))
    c_coefficient: int = int(input("Digite o valor do coeficiente c: "))

    delta: int = (b_coefficient ** 2) - 4 * a_coefficient * c_coefficient
    square_delta: int = delta ** (1/2)

    if delta < 0:
        print()
        print("A equação não possui valores reais.")

    elif delta == 0:
        print()
        print(f'A equação só possui uma raiz real e é igual a: {-b_coefficient / (2 * a_coefficient)}.')

    elif delta > 0:
        root_01: int = (-b_coefficient + square_delta) / (2 * a_coefficient)
        root_02: int = (-b_coefficient - square_delta) / (2 * a_coefficient)

        print()
        print(f'A equação tem duas raizes reais e são iguais a {root_01} e {root_02}')
