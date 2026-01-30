"""b) Calcule a área do circulo e o volume da esfera e mostre na tela."""

PI_CONSTANT: float = 3.141592

radius: float = float(input("Digite o raio do círculo: "))

circle_area: float = PI_CONSTANT * (radius ** 2)
esphere_volume: float = (4/3) * PI_CONSTANT * (radius ** 3)

print(f'A área do círculo é: {circle_area:.2f}')
print(f'O volume da esfera é: {esphere_volume:.2f}')
