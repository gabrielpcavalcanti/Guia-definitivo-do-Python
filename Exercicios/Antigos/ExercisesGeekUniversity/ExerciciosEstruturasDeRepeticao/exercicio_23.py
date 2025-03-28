"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

num = int(input("Digite um número: "))

for i in range(1, num +1):
    if num % i == 0:
        print(i)
        continue
    else:
        continue
