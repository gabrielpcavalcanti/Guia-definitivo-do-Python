"""
Leia o comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é: Y = M / 0.91  , sendo M o comprimento em metros e Y o comprimento em jardas.
"""

M = float(input("Digite o comprimento em metros: "))

Y = M / 0.91 

print("O comprimento em jardas: {:.2f}".format(Y))
