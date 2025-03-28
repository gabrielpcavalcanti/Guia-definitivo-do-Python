"""
Escrava um programa qua pargunta a quantidade da Km percorridos por um carro alugado a a quantidada da dias pelos 
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
custa RS60 por dia a R$ 0,15 por Km rodado. 
"""

quant_dias = float(input("Quantos dias você alugou o carro?: "))
quant_km = float(input("Quantos quilometros você andou com o carro?: "))

preço = quant_dias * 60 + quant_km * 0.15

print("Você terá que pagar R$ {} por {} dias e por ter percorrido {} km".format(preço,quant_dias,quant_km))
