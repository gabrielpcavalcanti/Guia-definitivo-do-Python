"""
Leia o comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = I * 2.54, sendo C o comprimento em centímetros e I o comprimento em polegadas.
"""

I = float(input("Digite o comprimento em polegadas: "))

C = I * 2.54

print("O comprimento em centimetros é: {:.2f}".format(C))
