"""
a) Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

number_week_day: int = int(input("Escolha um número de 1 a 7: "))

print()

match number_week_day:

    case 1: 
        print("Domingo.")

    case 2:
        print("Segunda=feira.")

    case 3:
        print("Terça-feira.")

    case 4:
        print("Quarta-feira.")
    
    case 5:
        print("Quinta-feira.")
    
    case 6:
        print("Sexta-feira.")
    
    case 7:
        print("Sábado.")
    
    case _:
        print("Erro.")
