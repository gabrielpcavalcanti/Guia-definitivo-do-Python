"""
Faça um programa que leia um número inteiro positivo n e calculea soma dos n primeiros 
números naturais.
"""

n = int(input("Digite um número inteiro: "))
soma = 0

for i in range(n + 1):
    soma += i

print(f'A soma dos {n} primeiros números é: {soma}')
