"""
Usando match, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês 
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. 
"""

num_year: int = int(input("Digite um número de 1 a 12: "))

print()

match num_year:

    case 1:
        print("Janeiro")

    case 2:
        print("Fevereiro")

    case 3:
        print("Março")

    case 4:
        print("Abril")

    case 5:
        print("Maio")

    case 6:
        print("Junho")

    case 7:
        print("Julho")

    case 8:
        print("Agosto")

    case 9:
        print("Setembro")

    case 10:
        print("Outubro")

    case 11:
        print("Novembro")

    case 12:
        print("Dezembro")

    case _:
        print("Número inválido! Digite um valor entre 1 e 12.")
