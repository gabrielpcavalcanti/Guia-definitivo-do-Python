"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores 
lidos na ordem inversa. 
 """

vector: list[int] = []

while True:

    if len(vector) > 5:
        break

    value: int = int(input("Digite um valor inteiro: "))

    if value % 2 == 0:
        vector.append(value)
        continue

print(vector[::-1])
