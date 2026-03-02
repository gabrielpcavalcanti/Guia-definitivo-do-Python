"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo_carne = input("Digite o tipo da carne (Pode ser file, alcatra ou pucanha): ")
quant_carne = float(input("Quantidade de carne que queira comprar: "))

print()

tipo_pagamento = input("Tipo de pagameto (dinheiro ou cartao tabajara): ").upper()

if tipo_carne == 'file':

    if tipo_pagamento == 'cartao tabajara':
        if 0 <= quant_carne <= 5:
            preco_file = quant_carne * 4.9
            desconto = preco_file * 0.05
            preco_file_final = preco_file - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_file} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_file_final}")
        elif quant_carne > 5:
            preco_file = quant_carne * 5.8
            desconto = preco_file * 0.05
            preco_file_final = preco_file - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_file} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_file_final}")

        else:
            print("Erro")

    elif tipo_pagamento == 'dinheiro':
        if 0 <= quant_carne <= 5:
            preco_file = quant_carne * 4.9
            desconto = 0
            preco_file_final = preco_file - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_file} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_file_final}")
        elif quant_carne > 5:
            preco_file = quant_carne * 5.8
            desconto = 0
            preco_file_final = preco_file - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_file} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_file_final}")
        else:
            print("Erro")

elif tipo_carne == 'alcatra':

    if tipo_pagamento == 'cartao tabajara':
        if 0 <= quant_carne <= 5:
            preco_alcatra = quant_carne * 5.9
            desconto = preco_alcatra * 0.05
            preco_alcatra_final = preco_alcatra - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_alcatra} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_alcatra_final}")
        elif quant_carne > 5:
            preco_alcatra = quant_carne * 6.8
            desconto = preco_alcatra * 0.05
            preco_alcatra_final = preco_alcatra - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_alcatra} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_alcatra_final}")

        else:
            print("Erro")

    elif tipo_pagamento == 'dinheiro':
        if 0 <= quant_carne <= 5:
            preco_alcatra = quant_carne * 5.9
            desconto = 0
            preco_alcatra_final = preco_alcatra - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_alcatra} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_alcatra_final}")
        elif quant_carne > 5:
            preco_alcatra = quant_carne * 6.8
            desconto = 0
            preco_file_final = preco_alcatra - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_alcatra} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_alcatra_final}")
        else:
            print("Erro")

elif tipo_carne == 'picanha':

    if tipo_pagamento == 'cartao tabajara':
        if 0 <= quant_carne <= 5:
            preco_picanha = quant_carne * 6.9
            desconto = preco_picanha * 0.05
            preco_picanha_final = preco_picanha - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_picanha} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_picanha_final}")
        elif quant_carne > 5:
            preco_picanha = preco_picanha * 7.8
            desconto = preco_picanha * 0.05
            preco_picanha_final = preco_picanha - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_picanha} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_picanha_final}")

        else:
            print("Erro")

    elif tipo_pagamento == 'dinheiro':
        if 0 <= quant_carne <= 5:
            preco_picanha = quant_carne * 6.9
            desconto = 0
            preco_picanha_final = preco_picanha - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_picanha} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_picanha_final}")
        elif quant_carne > 5:
            preco_picanha = quant_carne * 7.8
            desconto = 0
            preco_file_final = preco_picanha - desconto
            print(f"tipo da carne: {tipo_carne} \nquantidade da carne: {quant_carne} \npreço total: R$ {preco_picanha} "
                  f"\nTipo de pagamento: {tipo_pagamento} \nValor do desconto: {desconto} \nvalor a pagar: R$ {preco_picanha_final}")
        else:
            print("Erro")
else:
    print("Erro")

