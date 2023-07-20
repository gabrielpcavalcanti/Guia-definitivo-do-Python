"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo 
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral 
e a um exame final. A média das três notas mencionadas anteriormente obedece aos 
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo 
com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de 
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verticações necessárias.
"""

nota_laboratorio = float(input("Digite a primeira nota: "))
nota_semestral = float(input("Digite a segunda nota: "))
nota_final = float(input("Digite a terceira nota: "))

media_ponderada = (nota_laboratorio * 2 + nota_semestral * 3 + (nota_final * 5)) / 10

if 0 <= media_ponderada <= 2.9:
    print()
    print("Você foi reprovado com média {}".format(media_ponderada))

elif 3 <= media_ponderada <= 4.9:
    print()
    print("Você ficou em recuperação com média {}".format(media_ponderada))

elif media_ponderada >= 5:
    print()
    print("Você foi aprovado com média {}".format(media_ponderada))

else:
    print()
    print("ERRO!!!")

