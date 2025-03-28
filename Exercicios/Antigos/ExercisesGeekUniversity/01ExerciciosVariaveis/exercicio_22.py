"""
Leia o comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * Y , sendo M o comprimento em metros e Y o comprimento em jardas.
"""

Y = float(input("Digite o comprimento em jardas: "))

M = 0.91 * Y 

print("O comprimento em metros é: {:.2f}".format(M))
