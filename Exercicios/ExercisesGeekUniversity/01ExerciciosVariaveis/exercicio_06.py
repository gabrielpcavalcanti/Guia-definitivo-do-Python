"""
Leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0. Sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.
"""

C = float(input("Digite a temperatura em graus Celcius: "))

F = C * (9.0 / 5.0) + 32.0

print(f'A temperatura em graus Fahrenheit é: {F}')
