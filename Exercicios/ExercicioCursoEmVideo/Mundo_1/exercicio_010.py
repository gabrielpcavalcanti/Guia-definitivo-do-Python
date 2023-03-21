"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = float(dinheiro / 5)

print("com {} você pode comprar US$ {:.2f}".format(dinheiro, dolar))
