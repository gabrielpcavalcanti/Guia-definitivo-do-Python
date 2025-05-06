"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, 
assim como a diferença existente entre ambos.
"""

num_01: float = float(input("Digite um número: "))
num_02: float = float(input("Digite um número: "))

print()

if num_01 > num_02:
    print(f'O maior número é {num_01}')
    print(f'A diferença entre eles é {num_01 - num_02}')

else:
    print(f'O maior número é {num_02}')
    print(f'A diferença entre eles é {num_01 - num_02}')
    