"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite um número inteiro: "))

list = []

for i in range(num_1 + 1, num_2, 1):
    if num_1 < num_2:
        list.append(i)
    else:
        print("intervalo inválido")
        break

print(sum(range(num_1 + 1, num_2)))


