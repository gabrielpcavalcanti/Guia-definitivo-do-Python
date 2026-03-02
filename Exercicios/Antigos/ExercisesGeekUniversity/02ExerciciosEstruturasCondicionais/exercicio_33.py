"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, 
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de 
acordo com a segunda tabela). 

PREÇO ANTIGO                PORCENTAGEM DE AUMENTO
até R$ 50                            5%
entre R$ 50 e R$ 100                 10%
acima de R$ 100                      15% 

PREÇO NOVO                              MENSAGEM 
até R$ 80                               Barato 
entre R$ 80 e R$ 120 (inclusive)        Normal 
entre R$ 120 e R$ 200 (inclusive)       Caro 
acima de R$ 200                         Muito caro 
"""

preco_antigo = int(input("Digite o preço antigo: "))

if preco_antigo < 50:

    preco_novo = preco_antigo + preco_antigo * 0.05

elif preco_antigo > 50 and preco_antigo < 100:

    preco_novo = preco_antigo + preco_antigo * 0.1

elif preco_antigo > 100:

    preco_novo = preco_antigo + preco_antigo * 0.15

else:
    print("Valor inválido")

if preco_novo <= 80:
    print("Barato")

elif preco_novo > 80 and preco_novo <= 120:
    print("Normal")

elif preco_novo >= 120 and preco_novo <= 200:
    print("Caro")

elif preco_novo > 200:
    print("Muito caro")

