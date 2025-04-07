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

