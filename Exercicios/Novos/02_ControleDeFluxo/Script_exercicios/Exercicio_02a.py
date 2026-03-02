"""
a) Faça um programa que receba dois números e mostre o maior. Se por acaso os dois números forem iguais, imprima a mensagem: Números iguais."""

number_01: float = float(input("Digite um número: "))
number_02: float = float(input("Digite um número: "))

if number_01 > number_02:
    print()
    print(f'O maior número é {number_01}.')

elif number_02 > number_01:
    print()
    print(f'O maior número é {number_02}.')

else:
    print()
    print("Números iguais.")
