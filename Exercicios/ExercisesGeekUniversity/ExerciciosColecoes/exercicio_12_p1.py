"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos 
juntamente com o maior, o menor e a média dos valores. 
"""

lista_num = []

for i in range(5):

    num = int(input("Digite um número: "))
    lista_num.append(num)

print(lista_num)
print(max(lista_num))
print(min(lista_num))
print(sum(lista_num) / len(lista_num))
