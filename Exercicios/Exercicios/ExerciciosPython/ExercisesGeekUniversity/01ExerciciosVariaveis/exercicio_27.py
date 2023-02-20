"""
Leia a área em hectares e apresente-a convertidade em metros quadrados.
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
"""

H = float(input("Digite a área em hectares: "))

M = H * 10000

print("A área em metros quadrados é: {:.2f}".format(M))
