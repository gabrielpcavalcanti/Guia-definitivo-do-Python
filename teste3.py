"""
lista = [1, 1, 2, 4, 5, 5, 6]

print(lista)

print(set(lista))

print(list(set(lista)))

def function(input: str | int):
    print(input.capitalize())

function("teste")
function(1)
function(10.2)

lista: list[any] = [1, '20', True]

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