"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).
"""

coord_x: float = float(input("Digite o valor da coordenada x: "))
coord_y: float = float(input("Digite o valor da coordenada y: "))

dist: float = ((coord_x)**2 + (coord_y)**2)**(1/2)

print(f'A distância em relação a origem é: {dist}')
