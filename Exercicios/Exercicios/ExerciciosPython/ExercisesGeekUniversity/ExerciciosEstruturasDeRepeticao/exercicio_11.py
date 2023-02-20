"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números 
naturais de 0 até N em ordem crescente.
"""

N = int(input("Digite um número inteiro: "))

for i in range(N + 1):
    print(i, end=' ')
