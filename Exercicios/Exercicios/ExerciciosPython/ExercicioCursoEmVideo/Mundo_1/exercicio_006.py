"""
Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""

num = int(input("Digite um número: "))

print(f'O dobro de {num} vale {num * 2}.')
print(f'O triplo de {num} vale {num * 3}.')
print('A raiz quadrada de {} é {:.2f}.'.format(num, num ** (1/2)))
