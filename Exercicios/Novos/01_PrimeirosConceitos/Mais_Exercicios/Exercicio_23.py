"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta.
Faça um programa que leia quanto cada um apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

punter_1: float = float(input("Valor inverstido do primeiro apostador: "))
punter_2: float = float(input("Valor inverstido do segundo apostador: "))
punter_3: float = float(input("Valor inverstido do terceiro apostador: "))

award: float = float(input("Digite o valor do prêmio: "))

value_1: float = (punter_1 / award) * award
value_2: float = (punter_2 / award)
value_3: float = punter_3 / award

print(value_1)
print(value_2)
print(value_3)
