"""
Sejam a e b lados de um triângulo, onde a hipotenusa é obtida pela equação hipo = square_roo(a**2 + b**2). Faça um programa que receba os valores de 
a e b e calcule o valor da hipotenusa atravez da equação. Imprima o resultado dessa operação. 
"""

a = int(input("Digite o valor do cateto:  "))
b = int(input("Digite o valor do cateto: "))

hipo = (a**2 + b**2) ** (1/2)

print(f'A hipotenusa é: {int(hipo)}')
