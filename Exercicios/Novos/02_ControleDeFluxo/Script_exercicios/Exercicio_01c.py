"""c) Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar."""

number_01: int = int(input("Digite um número: "))

if number_01 % 2 == 0:
    print()
    print(f'O número {number_01} é par.')

else:
    print()
    print(f'O número {number_01} é ímpar.')
