"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números 
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na 
tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a 
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas 
corretas, além de quantas vezes o aluno acertou. 
"""

# Esse exercicio não é possivel de ser feito com os conhecimentos abordados até agora (pelo menos eu não consegui). 
# No caso, variáveis e estruturas condicionais. mas caso queira ver a solução, está ai.

import random

Lista_resposta = []
resposta_correta = 0

for i in range(5):

    a = random.randint(1, 100)
    b = random.randint(1, 100)

    soma = a + b 
    Lista_resposta.append(soma)

    print(f"Qual a soma de {a} + {b}")
    resposta = float(input("Digite sua resposta aqui: "))

    if soma ==  resposta:
        resposta_correta += 1

print()
print(f"RESPOSTAS DA PROVA")

for k in range(5):

    print(f"Questão {k+1}: {Lista_resposta[k]} ")
    
print()
print(f"Quantas questões você acertou: {resposta_correta}")
