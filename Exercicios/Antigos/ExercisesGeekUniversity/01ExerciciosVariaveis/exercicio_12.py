"""
Leia a distância em milhas e apresente-a convertida em quilometros.
A fórmula de conversão é K = 1.61 * M. Sendo K a distância em quilometros e M a distância em milhas.
"""

M = float(input("Digite a Distância em milhas: "))

print(f'A distância em quilometros é {round(1.61 * M, 2)}')
