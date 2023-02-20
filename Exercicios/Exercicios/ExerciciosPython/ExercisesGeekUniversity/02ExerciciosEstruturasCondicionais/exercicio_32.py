"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lan- 
chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. 
Considere que a cada execução somente será calculado um pedido. O cardápio da lan- 
chonete segue o padrão abaixo: 

Especificação                 Código                      Preço 
Cachorro Quente                100                        1.20 
Bauru Simples                  101                        1.30
Bauru com Ovo                  102                        1.50 
Hamburguer                     103                        1.20 
Cheeseburguer                  104                        1.70 
Suco                           105                        2.20 
Refrigerante                   106                        1.00
"""

codigo = int(input("Digite o código do produto: "))

if codigo == 100:
    print("Você vai pagar por um Cachorro quente o valo de R$ 1,20")

if codigo == 101:
    print("Você vai pagar por um Bauru simples o valo de R$ 1,30")

if codigo == 102:
    print("Você vai pagar por um Bauru com ovo o valo de R$ 1,50")

if codigo == 103:
    print("Você vai pagar por um Hamburguer o valo de R$ 1,20")

if codigo == 104:
    print("Você vai pagar por um Cheeseburguer o valo de R$ 1,70")

if codigo == 105:
    print("Você vai pagar por um suco o valo de R$ 2,20")

if codigo == 106:
    print("Você vai pagar por um Refrigerante o valo de R$ 1,00")


# O programa acima está muito simplista, mas foi o que eu entendi do enunciado, Se quiser deixar o programa mais completo é preciso utilizar
# assuntos que ainda não vimos. Caso tenha curiosidade, o código está abaixo.

lista_codigos = []
soma = 0

print("PEDIDO")

while True:

    codigo = int(input("Digite o código do produto (Digite 999 para parar o pedido): "))

    if codigo != 999:
        lista_codigos.append(codigo)
    if codigo == 999:
        break

for i in lista_codigos:

    if i == 100:
        soma += 1.20

    if i  == 101:
        soma += 1.30

    if i  == 102:
        soma += 1.50

    if i == 103:
        soma += 1.20

    if i  == 104:
        soma += 1.70

    if i  == 105:
        soma += 2.20

    if i  == 106:
        soma += 1.00

print(f"Valor total do pedido: R$ {soma}")
