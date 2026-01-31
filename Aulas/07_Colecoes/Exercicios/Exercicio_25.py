"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais 
que não são múltiplos de 7 ou que terminam com 7.
"""

first_100: list[int] = list(range(1,101))

first_100_without_multiple_7: list[int] = list(filter(lambda x: x % 7 == 0, first_100))

print(set(list(set(first_100).difference(set(first_100_without_multiple_7)))).difference({17,27,37,47,57,67,77,87,97}))
