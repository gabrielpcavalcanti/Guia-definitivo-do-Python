"""
Faça um Programa que leia três números e mostre-os em ordem decrescente
"""

num1 = float(input("Digite um número:"))
num2 = float(input("Digite um número:"))
num3 = float(input("Digite um número:"))

print()

if num1 > num2 > num3:
    print("{}, {}, {}".format(num1,num2,num3))
elif num1 > num3 > num2:
    print("{}, {}, {}".format(num1, num3, num2))
elif num2 > num3 > num1:
    print("{}, {}, {}".format(num2, num3, num1))
elif num2 > num1 > num3:
    print("{}, {}, {}".format(num2, num1, num3))
elif num3 > num1 > num2:
    print("{}, {}, {}".format(num3, num1, num2))
elif num3 > num2 > num1:
    print("{}, {}, {}".format(num3, num2, num1))
else:
    print("Erro")