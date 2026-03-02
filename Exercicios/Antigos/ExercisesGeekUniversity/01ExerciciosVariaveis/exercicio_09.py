"""
Leia a temperatura em Celcius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: K = C + 273.15 . Sendo K a temperatura em Kelvin e C a temperatura em Celcius.
"""

C = float(input("Digite a temperatura em graus Celcius: "))

K = C + 273.15

print(f'A temperatura em Kelvin é: {K}')
