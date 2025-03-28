"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
            

respostas_sim = []
respostas_nao = []
resposta = 's'
print("Digite sim ou nao.")

for x in perguntas:
    resposta = input(f"{x}: ").lower()

    if resposta == 'sim':
        respostas_sim.append(resposta)
    elif resposta == 'nao':
        respostas_nao.append(resposta)

if len(respostas_sim) == 2:
    print("Suspeito")
elif len(respostas_sim) == 3 or len(respostas_sim) == 4:
    print("Cúmplice")
elif len(respostas_sim) == 5:
    print("Assasino")
elif len(respostas_sim) == 1:
    print("Inocente")

