"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

c = 1
k = 1

num = float(input(f'Digite um número {k}/10: '))

maior = num
menor = num

while c <= 9:
    num = float(input(f'Digite um número {k+1}/10: '))
    c += 1
    k += 1

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
