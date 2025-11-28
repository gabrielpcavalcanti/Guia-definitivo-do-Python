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

old_price: float = float(input("Digite o preço antigo do produto: "))

if old_price <= 50:
    increase_percentage: float = 0.05

elif old_price <= 100:
    increase_percentage = 0.10

else:
    increase_percentage = 0.15

new_price: float = old_price * (1 + increase_percentage)


if new_price <= 80:
    message: str = "Barato"

elif new_price <= 120:
    message = "Normal"

elif new_price <= 200:
    message = "Caro"

else:
    message = "Muito caro"


print(f"Preço antigo: R$ {old_price:.2f}")
print(f"Novo preço: R$ {new_price:.2f}")
print(f"Classificação: {message}")
