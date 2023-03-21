"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

lista_idade = []
lista_altura = []

for i in range(5):
    idade = int(input("Digite a idade: "))
    lista_idade.append(idade)
    altura = float(input("Digite a altura: "))
    lista_altura.append(altura)

# Ordem normal
print(lista_idade)
print(lista_altura)

lista_idade.reverse()
lista_altura.reverse()

# Ordem inversa
print(lista_idade)
print(lista_altura)