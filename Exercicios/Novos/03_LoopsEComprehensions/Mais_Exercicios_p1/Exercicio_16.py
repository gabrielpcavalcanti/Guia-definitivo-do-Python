"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um 
código inteiro. Se 0 código for zero, finalize 0 programa; se for 1 , mostre 0 vetor na ordem 
direta; se for 2, mostre o vetor na ordem inversa Caso, o código for diferente de 1 e 2 
escreva uma mensagem informando que 0 código é inválido. 
"""

vector: list[float] = []

for _ in range(5):
    value: float = float(input("Digite um valor inteiro: "))

    vector.append(value)

cases: int = int(input(("Digite um número: ")))

while True:
    match cases:

        case 0:
            break

        case 1:
            print(vector)
            break

        case 2:
            print(vector[::-1])
            break

        case _:
            print("Caso inválido.")
            continue
