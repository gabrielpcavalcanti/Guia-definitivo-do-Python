"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morangos = float(input("Digite a quantidade de morangos, em Kg: "))
macas = float(input("Digite a quantidade de mocas, em Kg: "))

soma = morangos + macas

print()

if 0<= soma <=5:
    preco_morangos = 2.5 * morangos
    preco_macas = 1.8 * macas
    print(f"Valor a ser pago: R$ {preco_morangos} para morangos e R$ {preco_macas} para maças.")
elif soma > 5:
    preco_morangos = 2.2 * morangos
    preco_macas = 1.5 * macas
    preco = preco_morangos + preco_macas
    if soma > 8 or preco > 25:
        preco10 = preco - 0.1 * preco
        print("O valor é: R$ {}".format(preco10))
    else:
        print(f"Valor a ser pago: R$ {preco_morangos} para morangos e R$ {preco_macas} para maças.")
else:
    print("Erro")
