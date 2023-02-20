"""
Leia a massa em quilogramas apresente-o convertido em libras. 
A fórumula de conversão é: P = K / 0.45, sendo a massa em libras e K em quilogramas.
"""

K = float(input("Digite a massa em quilogramas: "))

P = K / 0.45

print(f'A massa em libras é: {round(P, 2)}')
