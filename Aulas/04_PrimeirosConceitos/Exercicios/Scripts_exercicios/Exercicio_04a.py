"""
a) Leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0. Sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.
"""

temp_celcius: float = float(input("Digite a temperatura em graus Celsius: "))

temp_fahrenheit: float = (temp_celcius * (9/5)) + 32

print(f'A temperatura de {temp_celcius} graus Celcius é a mesma que {temp_fahrenheit:.2f} em graus Fahrenheit.')
