"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números 
pares de 0 até N em ordem decrescente.
"""

N = int(input("Digite um número inteiro: "))
c = -1

while c != N:
    if N % 2 == 0:
        print(N, end=' ')
        N -= 1
        continue
    else:
        N -= 1
        continue
