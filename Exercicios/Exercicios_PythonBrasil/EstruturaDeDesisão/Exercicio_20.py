"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
"""

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

print()

if 7 <= media < 10:
    print(f"Aprovado com média {media}")
elif media < 7:
    print(f"Reprovado com média {media}")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Erro")

