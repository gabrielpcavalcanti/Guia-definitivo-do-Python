"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e 
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno 
e indcar se o aluno foi aprovado ou reprovado. A nota para aproçâo deve ser igual ou 
superior a 60 pontos.
"""

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media_ponderada = (nota_1 + nota_2 + (nota_3 * 2)) / 4

if media_ponderada >= 6:
    print()
    print("Você foi aprovado com média {}".format(media_ponderada))

else:
    print()
    print("Você foi reprovado com média {}".format(media_ponderada))

