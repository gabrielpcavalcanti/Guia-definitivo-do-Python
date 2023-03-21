"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros 
números naturais impares.
"""

num = int(input("Digite um número inteiro: "))

for i in range(1, num + 1):
    if not i % 2 == 0:
        print(i)
        continue
    else:
        continue
