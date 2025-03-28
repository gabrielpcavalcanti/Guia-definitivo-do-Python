"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números 
naturais de 0 até N em ordem decrescente.
"""

N = int(input("Digite um número inteiro: "))
c = -1

while c != N:
    print(N, end=' ')
    N -= 1
    