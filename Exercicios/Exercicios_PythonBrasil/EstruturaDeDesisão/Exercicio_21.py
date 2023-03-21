"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

money = int(input("Digite o valor que você quer sacar: "))

nota_100 = money / 100
resto_nota100 = money % 100

nota_50 = resto_nota100 / 50
resto_nota50 = resto_nota100 % 50

nota_5 = resto_nota50 / 5
resto_nota5 = resto_nota50 % 5

nota_1 = resto_nota5 / 1
resto_nota1 = resto_nota5 % 1

print()

if 10 <= money <= 600:
    print(f"Diheiro sacado {money}.")
    print(f"São {int(nota_100)} notas de 100, {int(nota_50)} notas de 50, {int(nota_5)} notas de 5 e {int(nota_1)} de 1")

else:
    print("Valor inválido")
