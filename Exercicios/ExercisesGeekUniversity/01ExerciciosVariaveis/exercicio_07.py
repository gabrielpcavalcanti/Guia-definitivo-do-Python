"""
Leia a temperatura em graus Fahrenheit e apresente-a convertida em graus Celcius.
A fórmula de conversão é: C = 5.00 * (F - 32.0) / 9.0 . Sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.
"""

F = float(input("Digite a temperatura em graus Fahrenheit: "))

C = 5.00 * (F - 32.0) / 9.0

print(f'A temperatura em graus Celcisus é: {C}')
