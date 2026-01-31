"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""

number: int = int(input("Digite um número: "))

next_number = number + 1

while True:

    if next_number % 11 == 0 or next_number % 13 == 0 or next_number % 17 == 0:
        print(f'O primeiro múltiplo encontrado é: {next_number}')
        break

    next_number += 1
