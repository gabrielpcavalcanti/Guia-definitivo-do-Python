"""
Leia a temperatura em Kelvin e apresente-a convertida em graus Celcius.
A fórmula de conversão é: C = K - 273.15 . Sendo K a temperatura em Kelvin e C a temperatura em Celcius.
"""

K = float(input("Digite a temperatura em Kelvin: "))

C = K - 273.15

print(f'A temperatura em graus Celcius é: {C}')
