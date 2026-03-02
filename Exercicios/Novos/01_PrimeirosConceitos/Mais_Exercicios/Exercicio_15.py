"""
Faça um programa que leia o valor de horas de trabalho (em reais) e o número de horas trabalhas no mês. Imprima o valor a ser pago ao funcionário, adcionando 10% ao valor calculado. 
"""

price_per_hour = float(input("Digite a preço por hora trabalhada: "))

hour: int = int(input("Digite a quantidade de horas trabalhadas: "))

salary: float = (price_per_hour * hour) + ((price_per_hour * hour) * 0.1)

print(f'O valor a ser pago é R$ {salary}')
