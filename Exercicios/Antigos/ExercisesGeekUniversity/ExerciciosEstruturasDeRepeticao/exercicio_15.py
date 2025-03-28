"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os 
nümeros impares de 1 até N em ordem crescente.
"""

c = 0
N = int(input("Digite um número inteiro: "))

for i in range(N+1):
    if not i % 2 == 0:
        print(i, end=' ')
        continue
    else:
        continue
