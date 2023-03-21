"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números 
pares de 0 até N em ordem crescente.
"""

c = 0
N = int(input("Digite um número inteiro: "))

for i in range(N+1):
    if i % 2 == 0:
        print(i, end=' ')
        continue
    else:
        continue
