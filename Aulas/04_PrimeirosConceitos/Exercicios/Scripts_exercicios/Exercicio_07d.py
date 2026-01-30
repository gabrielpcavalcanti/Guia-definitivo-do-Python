"""
d) Escrava um programa qua pargunta a quantidade da km percorridos por um carro alugado a a quantidada da dias pelos 
quais ele foi alugado. Calcule o preço a pagar.

Sabendo que o carro custa RS60 por dia a R$ 0,15 por km rodado.**
"""

quant_days: int = int(input("Quantos dias você alugou o carro?: "))
quant_km = float(input("Quantos quilometros você andou com o carro?: "))

price: float = (quant_days * 60) + (quant_km * 0.15)

print(f'Você terá que pagar R$ {price:.2f} por {quant_days} dias e por ter percorrido {quant_km} km')
