"""
Leia a altura e o raio de um cilindro e imprima o volume.
O volume de um cilindro é calculado por meio da seguinte forma: V = PI * (radius ** 2) * height, onde PI = 3.141592 
"""

PI = 3.141592

height: float = float(input("Digite a altura do cilindro: "))
radius: float = float(input("Digite o raio do cilindro : "))

volume: float = PI * (radius ** 2) * height

print(f'O volume é {volume:.2f}')
