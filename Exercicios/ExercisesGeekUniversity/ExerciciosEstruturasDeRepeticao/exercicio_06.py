"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

c = 1
k = 1
soma = 0

while c <= 10:
    num = float(input(f'Digite um número {k}/10: '))
    soma += num
    c += 1
    k += 1

print(f'A média dos números digitados é {soma / 10}')
