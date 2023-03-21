"""
Leia a distância em quilometros e apresente-a convertida em milhas.
A fórmula de conversão é M = K / 1.61. Sendo K a distância em quilometros e M a distância em milhas.
"""

K = float(input("Digite a disância em quilometros: "))

print(f'A distância em milhas é {round(K / 1.61, 2)}')
