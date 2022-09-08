import statistics

dados = list(range(10))

media = statistics.mean(dados)

res = filter(lambda valor: valor > media, dados)

print(list(res))
print(list(res))

help(res)
