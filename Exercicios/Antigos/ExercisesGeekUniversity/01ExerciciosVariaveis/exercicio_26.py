"""
Leia a área em metros quadrados e apresente-a convertidade em hectares.
A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H a área em hectares.
"""

M = float(input("Digite a área em metros quadrados: "))

H = M * 0.0001

print("A área em hrctares é: {:.2f}".format(H))
