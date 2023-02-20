"""
Faça um algoritmo qua leia o salário de um Funcionário a mostre seu 
novo saláno, com 15% d3 aumanto. 
"""

salario = float(input("Digite o salário:  "))

novo_valor = salario + salario * 0.15

print("Seu salário: R$ {}. Valor com o aumento de 15%: R$ {:.2f}".format(salario, novo_valor))
