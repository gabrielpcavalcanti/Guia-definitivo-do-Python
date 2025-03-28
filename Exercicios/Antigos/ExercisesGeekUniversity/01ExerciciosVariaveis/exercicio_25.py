"""
Leia a área em acres e apresente-a convertidade em metros quadrados.
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.
"""

A = float(input("Digite a área  em acres: "))

M = A * 4048.58

print("A área em meter quadrados é: {:.2f}".format(M))
