"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule 
e imprima a média geral.
"""

lista_notas = []

for i in range(15):

    num = float(input("Digite a nota da prova: "))
    lista_notas.append(num)

media = (sum(lista_notas) / len(lista_notas))

print(lista_notas)
print(f"A média das notas da turma foi: {media}")
