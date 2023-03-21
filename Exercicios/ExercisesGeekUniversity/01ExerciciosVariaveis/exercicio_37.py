"""
Faça um programa que leia um valor de um produto e imprima o valor com desconto. Considerando que o desconto é de 12%.
"""

value_product = float(input("Digite o valor do produto R$  "))

product_with_discount = value_product - (value_product * 0.12)

print("O valor com desconto é: $ {:.2f}".format(product_with_discount))
