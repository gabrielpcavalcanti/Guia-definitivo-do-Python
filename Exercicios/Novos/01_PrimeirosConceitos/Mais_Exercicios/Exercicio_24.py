"""
Faça um programa para ler duas dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno como a tela.
"""

lenght:float = float(input("Digite o comprimento do terreno: "))
widht:float = float(input("Digite a largura do terreno: "))
price:float = float(input("Digite o preço do metro de tela: R$ "))

area:float = lenght * widht

cost:float = area * price

print(f'O custo para cercar o terreno com a tela é de R$ {cost}')
