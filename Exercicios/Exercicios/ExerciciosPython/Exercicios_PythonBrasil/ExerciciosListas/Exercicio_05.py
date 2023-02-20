"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

lista_nums = []
lista_nums_pares = []
lista_nums_impares = []

for i in range(20):
    num = int(input("Digite um número inteiro : "))
    lista_nums.append(num)

    if num % 2 == 0:
        lista_nums_pares.append(num)
    else:
        lista_nums_impares.append(num)
    
print(f"Lista números: {lista_nums}")
print(f"Lista números pares: {lista_nums_pares}")
print(f"Lista números ímpares: {lista_nums_impares}")
