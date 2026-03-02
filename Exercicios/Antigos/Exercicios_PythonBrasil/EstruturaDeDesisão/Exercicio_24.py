"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

num1 = float(input("Digite um número"))
num2 = float(input("Digite outro número"))


print("Qual operação você deseja efetuar?")
print("soma - +, diferença - -, produto - * ou divisão - /")

operacao = srt(input("Qual será a operação: ").upper())

if operacao == '+':
    soma = num1 + num2
    print(f"A soma é {soma}")
    if soma % 2 == 0:
        print("O número {} é par".format(num))
    elif soma % 2 != 0:
        print("O número {} é impar".format(num))
    elif soma > 0:
        print("Número é positivo")
    elif soma < 0:
        print("Número é negativo")

if operacao == '-':
    diferenca = num1 - num2
    print(f"A soma é {diferenca}")
    if diferenca % 2 == 0:
        print("O número {} é par".format(num))
    elif diferenca % 2 != 0:
        print("O número {} é impar".format(num))
    elif diferenca > 0:
        print("Número é positivo")
    elif diferenca < 0:
        print("Número é negativo")

if operacao == '*':
    produto = num1 * num2
    print(f"A soma é {produto}")
    if produto % 2 == 0:
        print("O número {} é par".format(num))
    elif produto % 2 != 0:
        print("O número {} é impar".format(num))
    elif produto > 0:
        print("Número é positivo")
    elif produto < 0:
        print("Número é negativo")

if operacao == '/':
    divisao = num1 / num2
    print(f"A soma é {divisao}")
    if divisao % 2 == 0:
        print("O número {} é par".format(num))
    elif divisao % 2 != 0:
        print("O número {} é impar".format(num))
    elif divisao > 0:
        print("Número é positivo")
    elif divisao < 0:
        print("Número é negativo")
