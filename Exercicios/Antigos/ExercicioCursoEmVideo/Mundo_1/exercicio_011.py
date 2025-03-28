"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))

area = largura * altura

quantidade_de_tinta  = area // 2

print()

print(f'A área a ser pintada é de {area} metros quadrados e vai precisar de {quantidade_de_tinta} litros de tinta')
