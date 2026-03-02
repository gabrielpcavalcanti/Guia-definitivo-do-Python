"""
Faça um programa que receba dois números e mostre o maior. Se por acaso os dois 
números forem iguais, imprima a mensagem: Números iguais.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite um número inteiro: "))

if num_1 > num_2:
    print()
    print(f'O maior número é: {num_1}')

elif num_2 > num_1:
    print()
    print(f'O maior número é: {num_2}')

elif num_1 == num_2:
    print()
    print("Números iguais.")

else:
    print()
    print("Número inválida.")

