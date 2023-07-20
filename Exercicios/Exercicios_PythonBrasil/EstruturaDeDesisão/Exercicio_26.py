"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
 calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = float(input("Quantidade de litros: "))
tipo_combustivel = str(input("Qual o tipo de combustivel: ").upper())
preco_alcool = 1.9 * litros
preco_gasolina = 2.5 * litros

print()

if tipo_combustivel == 'A':
    if 0<= litros <= 20:
        descontoalcool20 = preco_alcool - (preco_alcool*0.03)
        print(f"Esse é o preço sem descontos: R$ {preco_alcool}")
        print(f"Esse é o preço com descontos: R$ {descontoalcool20}")
    elif litros > 20:
        descontoalcool50 = preco_alcool - (preco_alcool * 0.05)
        print(f"Esse é o preço sem descontos: R$ {preco_alcool}")
        print(f"Esse é o preço com descontos: R$ {descontoalcool50}")
    else:
        print("Erro")

elif tipo_combustivel == 'G':
    if 0 <= litros <= 20:
        descontoalcool40 = preco_alcool - (preco_alcool * 0.04)
        print(f"Esse é o preço sem descontos: R$ {preco_alcool}")
        print(f"Esse é o preço com descontos: R$ {descontoalcool40}")
    elif litros >20:
        descontoalcool60 = preco_alcool - (preco_alcool * 0.06)
        print(f"Esse é o preço sem descontos: R$ {preco_alcool}")
        print(f"Esse é o preço com descontos: R$ {descontoalcool60}")
    else:
        print("Erro")
else:
    print("Tipo de gasolsina não cadastrada")
