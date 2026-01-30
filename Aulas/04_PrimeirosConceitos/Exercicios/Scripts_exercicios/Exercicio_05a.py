"""
a) Crie um prgrama que escreva dois números e mostre a soma entre eles, o sucessor e antecedor de um deles, o dobro de um multipliado pelo outro e a raiz quadrada dos dois. Formate as Strings da maneira que quiser.
"""

number_01: float = float(input("Digite um número: "))
number_02: float = float(input("Digite outro número: "))

print(f'A soma entre {number_01} e {number_02} é {number_01 + number_02}')
print(f'O sucessor de {number_01} é {number_01 + 1} e o antecessor é {number_01 - 1}')
print(f'O dobro de {number_01} multiplicado por {number_02} é {(2 * number_01) * number_02}')
print(f'A raiz quadrada de {number_01} é {number_01 ** (1/2):.2f} e a raiz quadrada de {number_02} é {number_02 ** (1/2):.2f}')
