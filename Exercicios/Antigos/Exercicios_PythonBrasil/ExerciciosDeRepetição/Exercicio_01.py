"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

while True:
    num = int(input("Digite um número: "))
    if 0 <= num <= 10:
        print(num)
        break
    else:
        print("Escreva outro número.")
        print()
        continue


