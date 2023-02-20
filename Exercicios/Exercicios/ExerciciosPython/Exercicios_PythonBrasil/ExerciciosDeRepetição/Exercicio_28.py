"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

while True:

    quant_cd = int(input("Digite a quantidade de cd`s que vc tem: "))

    lista_valor_cd = []

    for i in range(quant_cd):
        valor_cd = float(input(f"Digite quanto vc gastou pelo cd {i + 1}: "))
        lista_valor_cd.append(valor_cd)

    print(f"A soma que vc gastou: R$ {sum(lista_valor_cd)}")
    print(f"O valor médio gasto foi de {sum(lista_valor_cd) / quant_cd} Reais")

    