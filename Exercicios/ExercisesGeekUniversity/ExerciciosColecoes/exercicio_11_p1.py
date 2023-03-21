"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a 
quantidade de números negativos e a soma dos números positivos desse vetor. 
"""

lista_num = []
num_neg = 0
soma_pos = 0

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

for k in lista_num:

    if k < 0:
        num_neg += 1
    
    if k > 0:
        soma_pos += k

print(lista_num)

print(f"Quantidade números negativos: {num_neg}")
print(f"Soma numeros positivos: {soma_pos}")
