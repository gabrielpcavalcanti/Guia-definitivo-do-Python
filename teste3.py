"""
lista = [1, 1, 2, 4, 5, 5, 6]

print(lista)

print(set(lista))

print(list(set(lista)))

def function(input: str | int):
    print(input.capitalize())

function("teste")
function(1)
function(10.2)

lista: list[any] = [1, '20', True]

"""

number: str = input("Digite um número: ")

centena: str = str(number[0])
dezena: str = str(number[1])
unidade: str = str(number[2])

print(f'A soma dos algarismos é {int(centena) + int(dezena) + int(unidade)}')
