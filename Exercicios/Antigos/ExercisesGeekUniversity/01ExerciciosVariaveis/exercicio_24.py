"""
Leia a área em metros quadrados e apresente-a convertidade em acres.
A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres.
"""

M = float(input("Digite a área em metros quadrados: "))

A = M * 0.000247

print("A área em acres é: {:.2f}".format(A))
