"""
Leia o tamanho do lado de um quadrado e imprima a sua área.
"""

size_square: float = float(input("Digite o tamanho do lado do quadrado: "))

area_square: float = size_square ** 2

print(f'A área do quadrado é: {area_square:.2f}')
