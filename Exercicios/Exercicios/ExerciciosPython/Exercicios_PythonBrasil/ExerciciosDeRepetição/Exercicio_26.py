"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

while True:
    
    quant_eleitores = int(input("Digite a quantidade de eleitores: "))
    candidato_total = []
    candidato_1 = []
    candidato_2 = []
    candidato_3 = []

    while len(candidato_total) != quant_eleitores:
        candidato = input("Digite o candidato que deseja votar(1, 2 ou 3): ")
        candidato_total.append(candidato)

        if candidato == '1':
            candidato_1.append(candidato)
        elif candidato == '2':
            candidato_2.append(candidato)
        elif candidato == '3':
            candidato_3.append(candidato)
        else:
            print("erro. número do candidato inválida. Digite novamente.")
            candidato_total.pop()
            continue
    
    print()
    print(f"Total de eleitores: {quant_eleitores}.")
    print(f"Total de votos do candidato 1: {len(candidato_1)}")
    print(f"Total de votos do candidato 2: {len(candidato_2)}")
    print(f"Total de votos do candidato 3: {len(candidato_3)}")
    
    print("Deseja sair? digite s para sair e n para rodar o programa denovo.")
    sair =input().lower()

    if sair == 's':
        break
    elif sair == 'n':
        continue
    else:
        print("Erro.")

        