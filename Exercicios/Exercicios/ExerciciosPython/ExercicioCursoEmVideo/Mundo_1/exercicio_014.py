"""
Escreva um programa que converta uma tamperatura 
digitada am °C converta para °F.
"""

temperatura_celcius = float(input("Informe a temperatura em °C: "))

temp_f = (temperatura_celcius * 9/5) + 32

print("A temperatura {}°C corresponde a {}°F".format(temperatura_celcius,temp_f))
