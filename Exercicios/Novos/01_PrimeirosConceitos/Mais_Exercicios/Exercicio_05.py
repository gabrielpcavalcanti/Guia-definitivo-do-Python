"""
Leia a temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.00 * (F - 32.0) / 9.0 . Sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

temp_fahrenheint = float(input("Digite a temperatura em graus Fahrenheit: "))

temp_celcius = 5.00 * (temp_fahrenheint - 32.0) / 9.0

print(f'A temperatura em graus Celsius é: {temp_celcius}')
