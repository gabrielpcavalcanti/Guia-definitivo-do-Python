"""
Leia o volume em litros e apresente-o convertido em metros cúbicos.
A fórmula de conversão é M = L / 1000, Sendo L o volume em litros e M o volume em metros cúbicos.
"""

L = float(input("Digite o volume em litros: "))

M = L / 1000

print(f'O volume em metros cúbicos é: {round(L, 2)}')
