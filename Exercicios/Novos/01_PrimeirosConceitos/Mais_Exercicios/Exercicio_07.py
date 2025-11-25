"""
Leia a velocidade em km/h e apresente-a convertida em m/s e vice-versa.
A fórmula de conversão é M = K / 3.6, sendo M a velocidade em m/s e K a velocidade em Km/h.
A fórmula de conversão é K = M * 3.6 , sendo M a velocidade em m/s e K a velocidade em Km/h.
"""

vel_kmh: float = float(input("Digite a velocidade em km/h: "))
vel_ms: float = float(input("Digite a velocidade em m/s: "))

print(f'A velocidade em m/s: {round(vel_kmh / 3.6, 2)}')
print(f'A velocidade em km/h: {round(vel_ms * 3.6, 2)}')
