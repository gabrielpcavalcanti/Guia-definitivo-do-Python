"""
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um
vetor. Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos,
sendo que caso o usuário digite um número que já foi digitado anteriormente, o programa
deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário
deve ser pesquisado no vetor, verificando se ele existe entre os números que já foram
fornecidos. Exibir na tela o vetor final que foi digitado.
"""

vector_01: list[int] = []

print("Digite os valores do primeiro vetor: \n")

while len(vector_01) != 10:

    value: int = int(input("Digite um valor inteiro: "))
    
    if value in vector_01:
        print("Valor repetido. Digite outro valor.")
        continue
    else:
        vector_01.append(value)

print(vector_01)
