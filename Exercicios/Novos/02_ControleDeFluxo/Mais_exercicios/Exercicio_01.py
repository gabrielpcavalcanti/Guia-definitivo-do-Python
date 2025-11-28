"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.
"""

num: float = float(input("Digite um número: "))

print()

if num >= 0:
    print(f'A raiz quadrada é {num ** (1/2):.2f}')

else:
    print(f'O número ao quadrado é {num ** 2}')
