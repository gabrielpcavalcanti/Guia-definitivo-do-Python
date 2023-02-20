"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

while True:

    lista = []

    quant_num = int(input("Digite a quantidade de numeros que você queira colocar numa lista: "))

    for i in range(quant_num):
        num = float(input("Digite um número: "))
        lista.append(num)
    
    max_lista = max(lista)
    min_lista = min(lista)
    sum_lista = sum(lista)

    print()
    print(lista)
    print("O valor Máximo é: {} \nO valor mínimo é {} \nE a soma dos valores é: {}".format(max_lista,min_lista,sum_lista))
