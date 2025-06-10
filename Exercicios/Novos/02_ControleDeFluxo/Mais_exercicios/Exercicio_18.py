"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser 
ao vendedor. Para calcular a comissão, considere a tabela abaixo: 
 
Venda mensal                                                            Comissão 
Maior ou igual a R$ 100.000,00                                          R$ 700,00 +16% das vendas 
Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00                 R$ 650,00 +14% das vendas
Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00                  R$ 600,00 +14% das vendas 
Menor que R$ 60.000,00 e maior ou igual a R$ 40.000,00                  R$ 550,00 +14% das vendas 
Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00                  R$ 500,00 +14% das vendas 
Menor que R$ 20.000,00                                                  R$ 400,00 +14% das vendas 
"""

valor_venda: float = float(input("Digite o valor da venda: "))

if valor_venda >= 100_000:
    print(f"Ele vai ganhar de comissão: r$ {round(700 + (valor_venda * 0.16), 3)}")

elif valor_venda < 100_000 and valor_venda >= 80000:
    print(f"Ele vai ganhar de comissão: r$ {round(650 + (valor_venda * 0.14), 3)}")

elif valor_venda < 80000 and valor_venda >= 60000:
    print(f"Ele vai ganhar de comissão: r$ {round(600 + (valor_venda * 0.14), 3)}")

elif valor_venda < 60000 and valor_venda >= 40000:
    print(f"Ele vai ganhar de comissão: r$ {round(550 + (valor_venda * 0.14), 3)}")

elif valor_venda < 40000 and valor_venda >= 20000:
    print(f"Ele vai ganhar de comissão: r$ {round(500 + (valor_venda * 0.14), 3)}")

elif valor_venda < 20000:
    print(f"Ele vai ganhar de comissão: r$ {round(400 + (valor_venda * 0.14), 3)}")
