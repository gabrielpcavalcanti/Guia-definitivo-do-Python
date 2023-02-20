"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo e o atecessor de seu dobro.
"""

num = int(input("Digite um número inteiro: "))

num_triple_suc = (num * 3) + 1
num_doble_prd = (num * 2) - 1

print(f'A soma é: {num_triple_suc + num_doble_prd}')
