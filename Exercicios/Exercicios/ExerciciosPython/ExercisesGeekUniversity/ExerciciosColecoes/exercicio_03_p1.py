"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das 
componentes deste vetor, armazenando o em outro vetor. Os conjuntos têm 
10 elementos cada. Imprimir todos os conjuntos. 
"""

lista_num = []
lista_num_quadrado = []

for i in range(10):

    num = int(input("Digite um número: "))
    lista_num.append(num)

for k in lista_num:
    
    num_quadrado = k**2
    lista_num_quadrado.append(num_quadrado)

print(lista_num)
print(lista_num_quadrado)
