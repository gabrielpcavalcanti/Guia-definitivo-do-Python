""" 
Faça um programa que leia um número inteiro positivo n e calculea soma dos n primeiros 
números naturais.
"""

num: int = int(input("Digite um número inteiro: "))
sumation: int = 0

for i in range(num + 1):
    sumation += i

print(f'A soma dos {num} primeiros números é: {sumation}')
