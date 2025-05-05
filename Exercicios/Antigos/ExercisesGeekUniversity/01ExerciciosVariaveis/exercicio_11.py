"""
Leia a velocidade em m/s e apresente-a convertida em km/s.
A fórmula de conversão é K = M * 3.6 , sendo M a velocidade em m/s e K a velocidade em Km/h.
"""

M = float(input("Digite a velocidade em m/s: "))

K = M * 3.6

print(f'A velocidade em km/h é: {round(K, 2)}')
