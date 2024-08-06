import os

def main():

    while True:

        print("0 : Soma")
        print("1 : Subtração")
        print("2 : Multiplicação")
        print("3 : Divisão")
        print("4 : Exponenciação")

        print("Escolha a opção que deseja realizar:")
        escolha = int(input())
        print()

        if escolha == 0:

            print(">>> + escolhida\n")

            print("Qual o primeiro valor?")
            num1 = float(input())

            print("Qual o segundo valor?")
            num2 = float(input())
            print()

            print(f'{num1} + {num2} = {sum(num1, num2)}')

            print()

            print("=============")

            print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
            cont = int(input())

            if cont == 0:
                clear_screen()
            
            if cont == 1:
                break
        
        if escolha == 1:

            print(">>> + escolhida\n")

            print("Qual o primeiro valor?")
            num1 = float(input())

            print("Qual o segundo valor?")
            num2 = float(input())
            print()

            print(f'{num1} + {num2} = {sub(num1, num2)}')

            print()

            print("=============")

            print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
            cont = int(input())

            if cont == 0:
                clear_screen()
            
            if cont == 1:
                break
        
        if escolha == 2:

            print(">>> + escolhida\n")

            print("Qual o primeiro valor?")
            num1 = float(input())

            print("Qual o segundo valor?")
            num2 = float(input())
            print()

            print(f'{num1} + {num2} = {multi(num1, num2)}')

            print()

            print("=============")

            print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
            cont = int(input())

            if cont == 0:
                clear_screen()
            
            if cont == 1:
                break
        
        if escolha == 3:

            print(">>> + escolhida\n")

            print("Qual o primeiro valor?")
            num1 = float(input())

            print("Qual o segundo valor?")
            num2 = float(input())
            print()

            print(f'{num1} + {num2} = {div(num1, num2)}')

            print()

            print("=============")

            print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
            cont = int(input())

            if cont == 0:
                clear_screen()
            
            if cont == 1:
                break
        
        if escolha == 4:

            print(">>> + escolhida\n")

            print("Qual o primeiro valor?")
            num1 = float(input())

            print("Qual o segundo valor?")
            num2 = float(input())
            print()

            print(f'{num1} + {num2} = {exp(num1, num2)}')

            print()

            print("=============")

            print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
            cont = int(input())

            if cont == 0:
                clear_screen()
            
            if cont == 1:
                break


def sum(num1, num2):
    
    return num1 + num2

def sub(num1, num2):
    
    return num1 - num2

def multi(num1, num2):
    
    return num1 * num2

def div(num1, num2):
    
    return num1 / num2

def exp(num1, num2):
    
    return num1 ** num2

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')


main()
