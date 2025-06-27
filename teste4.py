import random

for i in range(10):
    print([dado for dado in range(random.randrange(1,15))])

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_numbers: list[int] = list(map(lambda num: num ** 2, numbers))

print(square_numbers)

print([number ** 2 for number in numbers])

amigos = ["gabriel", "sofia", "artur"]

print([amigo.capitalize() for amigo in amigos])