"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math

a = float(input("Difite o valor de a:"))
b = float(input("Difite o valor de b:"))
c = float(input("Difite o valor de c:"))

delta = math.pow(b, 2) - 4*a*c
c = math.sqrt(delta)
print()

if a == 0:
    print("Não é equação de segundo grau")
elif delta < 0:
    print("Não possui raizes reais.")
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    print("A raiz da equação é: {}".format(x1))
elif delta !=0 and delta > 0:
    x1 = (-b + c) / (2 * a)
    x2 = (-b - c) / (2 * a)
    print("As raizes são: {} e {}".format(x1, x2))
else:
    print("Erro")
