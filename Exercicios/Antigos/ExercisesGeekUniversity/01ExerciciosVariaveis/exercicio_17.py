"""
Leia o comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: I = C / 2.54, sendo C o comprimento em centímetros e I o comprimento em polegadas.
"""

C = float(input("Digite o comprimento em centímetros: "))

I = C / 2.54

print("O comprimento em polegadas é: {:.2f}".format(I))
