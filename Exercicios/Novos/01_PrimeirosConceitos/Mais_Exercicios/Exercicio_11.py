"""
Sejam a e b lados de um triângulo, onde a hipotenusa é obtida pela equação hipo = square_root(a**2 + b**2). Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação. 
"""

a: int = int(input("Digite o valor do cateto:  "))
b: int = int(input("Digite o valor do cateto: "))

hipo: float = (a**2 + b**2) ** (1/2)

print(f'A hipotenusa é: {int(hipo)}')
