"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta.
Faça um programa que leia quanto cada um apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor 
investido.
"""

punter_1 = float(input("Valor inverstido do primeiro apostador: "))
punter_2 = float(input("Valor inverstido do segundo apostador: "))
punter_3 = float(input("Valor inverstido do terceiro apostador: "))

award = float(input("Digite o valor do prêmio: "))

value_1 = (punter_1 / award) * award
value_2 = (punter_2 / award)
value_3 = punter_3 / award

print(value_1)
print(value_2)
print(value_3)

print(value_1+value_2+value_3)
