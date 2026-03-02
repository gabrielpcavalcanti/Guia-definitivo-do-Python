""" 
Faça um programa que leia um número inteiro positivo N e imprima todos os números 
naturais pares de 0 até N em ordem decrescente.
"""

num = int(input("Digite um número inteiro: "))
list_num: list[int] = list(range(num))

for i in list_num[::-1]:

    if i % 2 == 0:
        print(i, end=' ')
