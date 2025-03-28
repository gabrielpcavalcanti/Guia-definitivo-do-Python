"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais 
e os escreva na tela. 
"""

lista_num = []

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

elementos_unicos = set(lista_num)

print(10 - elementos_unicos)
