"""
Faça um programa que leia um número inteiro positivo de três digitos (100 a 999). Gere outro numero formado pelos dígitos invertidos do número lido.
"""

num = input("Digite um número de (100 a 999): ")

num_inv = num[::-1]

print(f'O número invertido é: {num_inv}')
