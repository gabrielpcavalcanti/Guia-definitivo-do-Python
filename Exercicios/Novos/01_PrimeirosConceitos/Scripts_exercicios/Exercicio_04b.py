"""
b) Leia a temperatura em Kelvin e apresente-a convertida em graus Celcius.
A fórmula de conversão é: C = K - 273.15 . Sendo K a temperatura em Kelvin e C a temperatura em Celcius.
"""

temp_kelvin: float = float(input("Digite a temperatura em Kelvin: "))

temp_celcius: float = temp_kelvin - 273.15

print(f'A temperatura de {temp_kelvin} Kelvin é a mesma que {temp_celcius:.2f} em graus Celcius.')
