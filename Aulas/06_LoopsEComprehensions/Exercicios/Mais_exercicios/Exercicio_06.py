"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares. 
"""

sumation: int = 0

for i in range(1,51):

    if i % 2 == 0:
        sumation += i
    else:
        continue

print(sumation)
