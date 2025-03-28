"""
Leia um número inteiro e imprima o seu antecessor e sucessor.
"""

num = int(input("Digite um número inteiro: "))

num_pre = num - 1
num_suc = num + 1

print(f'O número é: {num}, seu antecessor é: {num_pre} e seu sucessor é: {num_suc}')
