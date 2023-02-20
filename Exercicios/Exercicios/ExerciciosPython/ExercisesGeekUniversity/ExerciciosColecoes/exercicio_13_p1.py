"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon- 
tram o maior e o menor valor. 
"""

lista_num = []

for i in range(5):

    num = int(input("Digite um número: "))
    lista_num.append(num)

print(lista_num)
print(lista_num.index(max(lista_num)))
print(lista_num.index(min(lista_num)))
