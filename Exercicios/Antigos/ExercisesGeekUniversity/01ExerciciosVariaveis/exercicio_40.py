"""
Uma empresa contrata um encanador a R$ 30.00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia 
líquida que deverá ser paga, sabendo que são decontados 8% para imposto de renda.
"""

pay = 30

days = int(input("Digite o número de dias: "))

total = pay * days

liquid = total - (0.8 * total)

print(f'A quantia líquida é {liquid}')
