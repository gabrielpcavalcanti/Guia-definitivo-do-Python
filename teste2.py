nomes = ["Gabriel", "joão", "Sofia", "Rafael", "Larissa"]

filtro = filter(lambda nome: len(nome) > 5, nomes)

nomes_final = map(lambda nome: f"{nome}", filtro)

print(list(nomes_final))