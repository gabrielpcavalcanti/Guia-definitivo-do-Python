"""
Leia um valor em Real e a cotação do Dolar. Imprima o valor do Dolar.
"""

real = float(input("Digite o valor em Real: R$  "))
quotation = float(input("Digite a cotação do Dolar: "))

print(f'O valor em Dolares é $ {round(real / quotation, 3)}')
