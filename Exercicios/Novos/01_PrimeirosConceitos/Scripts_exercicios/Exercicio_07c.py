"""
c) Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.

Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

width: float = float(input("Digite a largura em metros: "))
hight:float = float(input("Digite a altura em metros: "))

area: float = width * hight

quantity_of_paint: int = area // 2

print(f'A área a ser pintada é de {area} metros quadrados e vai precisar de {quantity_of_paint} litros de tinta')
