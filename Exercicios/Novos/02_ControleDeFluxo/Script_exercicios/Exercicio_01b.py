"""
b) Leia um número fornecido pelo usuário. Se o número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem que o número é inválido.
"""

number_01: float = float(input(("Digite um número: ")))

if number_01 >= 0:
    print()
    print(f'A raiz quadrade de {number_01} é {number_01 ** (1/2)}.')

else:
    print()
    print("Número inválido para calcular a raiz quadrada.")
