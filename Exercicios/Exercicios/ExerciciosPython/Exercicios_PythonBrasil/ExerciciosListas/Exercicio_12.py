"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

altura_13 = []
idade_13_altura_inferior = []

for i in range(5):
    idade = int(input("Digite a idade do aluno: "))
    altura = int(input("Digite a altura do aluno em cm: "))
    
    if idade > 13:
        altura_13.append(altura)

media_altura = int(sum(altura_13) / len(altura_13))

for x in altura_13:
    if x < media_altura:
        idade_13_altura_inferior.append(x)

print(idade_13_altura_inferior)
