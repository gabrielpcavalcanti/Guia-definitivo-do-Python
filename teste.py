#Forma ruim
list01: list[int] = [1, 2, 3]
list02: list[int] = [4, 5, 6]

for valor_list01, valor_list02  in zip(list01, list02):
    print(list01[valor_list01])
    print(list02[valor_list02])