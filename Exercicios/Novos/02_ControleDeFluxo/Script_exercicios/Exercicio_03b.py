"""
b) Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""

math_operation: str = input("Digite uma dessas quatro operaçãoes (+, -, * ou /): ")
number_01: float = float(input("Digite o primeiro número: "))
number_02: float = float(input("Digite o segundo número: "))

match math_operation:

    case "+":
        print(f'{number_01} + {number_02} = {number_01 + number_02}.')
    
    case "-":
        print(f'{number_01} - {number_02} = {number_01 - number_02}.')
    
    case "*":
        print(f'{number_01} * {number_02} = {number_01 * number_02}.')
    
    case "/":
        print(f'{number_01} / {number_02} = {number_01 / number_02}.')

    case _:
        print("Valor inválido.")
