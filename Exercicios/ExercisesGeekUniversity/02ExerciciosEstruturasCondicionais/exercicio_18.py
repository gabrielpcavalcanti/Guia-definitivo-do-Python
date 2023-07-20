"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações ma- 
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro- 
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e 
saindo. 
"""

print("Escolha uma das quatro operações básicas: \n+ \n- \n* \n/ \nDigite um desses símbolos para proseguir.")
operacao = input("->")

if operacao == "+":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    print(num1 + num2)

elif operacao == "-":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    print(num1 - num2)

elif operacao == "*":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    print(num1 * num2)

elif operacao == "/":
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    print(num1 / num2)

else:
    print("Operação inválida")

