"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""

sumation: int = 0
count: int = 0

while count < 10:

    value: int = int(input("Digite um número: "))

    if value >= 0:
        sumation += value
        count += 1
    else:
        continue

print(sumation / 10)
