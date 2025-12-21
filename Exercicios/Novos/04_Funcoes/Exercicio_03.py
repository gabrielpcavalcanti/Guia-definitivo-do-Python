""" 
Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

def which_weekday(number: int) -> str:

    match number:

        case 1: 
            return "Domingo."

        case 2:
            return"Segunda=feira."

        case 3:
            return "Terça-feira."

        case 4:
            return "Quarta-feira."
        
        case 5:
            return "Quinta-feira."
        
        case 6:
            return "Sexta-feira."
        
        case 7:
            return "Sábado."
        
        case _:
            return "Erro."


def main() -> None:
    
    number_week_day: int = int(input("Escolha um número de 1 a 7: "))

    print(which_weekday(number_week_day))


if __name__ == '__main__':
    main()
