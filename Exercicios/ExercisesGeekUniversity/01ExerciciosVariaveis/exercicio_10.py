"""
Leia a velocidade em km/h e apresente-a convertida em m/s.
A fórmula de conversão é M = K / 3.6, sendo M a velocidade em m/s e K a velocidade em Km/h.
"""

K = float(input("Digite a velocidade em km/h: "))

M = K / 3.6

print(f'A velocidade em m/s: {round(M, 2)}')
