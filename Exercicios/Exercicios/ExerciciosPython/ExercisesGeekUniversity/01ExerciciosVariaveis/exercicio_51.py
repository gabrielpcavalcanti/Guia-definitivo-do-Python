"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).
"""

coord_x = float(input("Digite o valor da coordenada x: "))
coord_y = float(input("Digite o valor da coordenada y: "))

dist = ((coord_x)**2 + (coord_y)**2)**(1/2)

print('A distância em relação a origem é: {dist}')
