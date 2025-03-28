"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os 
nümeros impares de 1 até N em ordem decrescente. 
"""

N = int(input("Digite um número inteiro: "))
c = -1

while c != N:
    if not N % 2 == 0:
        print(N, end=' ')
        N -= 1
        continue
    else:
        N -= 1
        continue
