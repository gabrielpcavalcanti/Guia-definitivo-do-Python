"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

while True:

    lista = []

    quant_num = int(input("Digite a quantidade de numeros que você queira colocar numa lista: "))

    for i in range(quant_num):
        num = float(input("Digite um número: "))
        
        if 0 <= num <= 1000: 
            lista.append(num)
            
            if len(lista) == quant_num:
                max_lista = max(lista)
                min_lista = min(lista)
                sum_lista = sum(lista)

                print()
                print(lista)
                print("O valor Máximo é: {} \nO valor mínimo é {} \nE a soma dos valores é: {}".format(max_lista, min_lista, sum_lista))
                
        else:
            print("Erro, número negativo ou maior que 1000.")
            
    break
    
    