"""
Faça um programa que peqa ao usuårio para digitar 10 valores e some-os. 
"""

c = 1
k = 1
soma = 0

while c <= 10:
    num = float(input(f'Digite um número {k}/10: '))
    soma += num
    c += 1
    k += 1

print(f'A soma dos números digitados é {soma}')
