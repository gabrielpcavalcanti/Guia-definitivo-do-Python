"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
num_3 = float(input("Digite um número: "))

if num_1 > num_2 and num_1 > num_3 and num_2 > num_3:
    print(f"{num_3} {num_2} {num_1} ")

elif num_1 > num_2 and num_1 > num_3 and num_3 > num_2:
    print(f"{num_3} {num_1} {num_2} ")

elif num_2 > num_1 and num_2 > num_3 and num_1 > num_3:
    print(f"{num_3} {num_1} {num_2} ")

elif num_2 > num_1 and num_2 > num_3 and num_3 > num_1:
    print(f"{num_1} {num_3} {num_2} ")

elif num_3 > num_1 and num_3 > num_2 and num_2 > num_1:
    print(f"{num_1} {num_2} {num_3} ")

elif num_3 > num_1 and num_3 > num_2 and num_1 > num_2:
    print(f"{num_1} {num_3} {num_2} ")


# Maneira mais elegante, mas com conhecimentos que pode ser que não tenha ainda. Veja como é:

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um número: "))
num_3 = float(input("Digite um número: "))

lista = [num_1, num_2, num_3]

lista.sort()

print(f"{lista[0]} {lista[1]} {lista[2]}")
