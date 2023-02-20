"""
Faça um algoritmo qua laia o preço da um produto a mostre seu 
novo preço, com 5%. de desconto. 
"""

valor = float(input("Digite um valor: "))

novo_valor = valor - valor * 0.05

print("Valor normal: R$ {}. Valor com desconto: R$ {:.2f}".format(valor,novo_valor))
