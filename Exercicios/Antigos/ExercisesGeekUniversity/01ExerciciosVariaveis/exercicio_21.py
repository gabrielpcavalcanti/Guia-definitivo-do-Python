"""
Leia a massa em libras apresente-o convertido em quilogramas. 
A fórumula de conversão é: K = P * 0.45, sendo a massa em libras e K em quilogramas.
"""

P = float(input("Digite a massa em libras: "))

K = P * 0.45

print(f'A massa em quilogramas é: {round(K, 2)}')
