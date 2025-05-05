"""
Escreva um prgrama de ajuda para os vedendores. A partir de um valor total lido, mostre:
O total a pagar com um desconto de 10%;
O valor de cada parcela, no parcelamento de 3x sem juros;
A comição do vendedor, no caso da venda ser a vista (5% no valor com desconto);
A comição do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

value: float = float(input("Digite o valor do produto R$ "))

value_10_percent_discount: float = value - (value * 0.1)

value_parcel: float = value / 3

commission_01: float = value_10_percent_discount * 0.05

commission_02: float = value * 0.05

print(f'O valor do produto é R$ {value}\nO valor da parcela (3x sem juros), R$ {value_parcel}')
print(f'A comissão para vendas a vista R$ {commission_01}\nA comissão para valores parcelados R$ {commission_02}')
