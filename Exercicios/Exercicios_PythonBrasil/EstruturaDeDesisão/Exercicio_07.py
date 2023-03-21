"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = float(input("Digite um número:"))
num2 = float(input("Digite um número:"))
num3 = float(input("Digite um número:"))

print()

if num1 > num2 > num3:
    print(num1)
    print(num3)
elif num1 > num3 > num2:
    print(num1)
    print(num2)
elif num2 > num3 > num1:
    print(num2)
    print(num1)
elif num2 > num1 > num3:
    print(num2)
    print(num3)
elif num3 > num1 > num2:
    print(num3)
    print(num2)
elif num3 > num2 > num1:
    print(num3)
    print(num1)
else:
    print("Erro")