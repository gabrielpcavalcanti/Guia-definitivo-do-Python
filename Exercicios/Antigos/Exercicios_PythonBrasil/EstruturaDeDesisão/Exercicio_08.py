"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

price1 = float(input("Digite o valor do produto: "))
price2 = float(input("Digite o valor do produto: "))
price3 = float(input("Digite o valor do produto: "))

print()

if price1 > price2 > price3:
    print(price3)
elif price1 > price3 > price2:
    print(price2)
elif price2 > price3 > price1:
    print(price1)
elif price2 > price1 > price3:
    print(price3)
elif price3 > price1 > price2:
    print(price2)
elif price3 > price2 > price1:
    print(price1)
else:
    print("Erro")