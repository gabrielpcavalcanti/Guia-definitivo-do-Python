"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
pais_a = float(input("Digite a população do país A: "))
pais_b = float(input("Digite a população do país B: "))
taxa_crescimento_a = float(input("Digite a taxa de crescimento do país A em %: "))
taxa_crescimento_b = float(input("Digite a taxa de crescimento do país B em %: "))
ano = 1

taxa_crescimento_a = taxa_crescimento_a / 100
taxa_crescimento_b = taxa_crescimento_b / 100

while pais_a < pais_b:
    pais_a = pais_a + pais_a * taxa_crescimento_a
    pais_b = pais_b + pais_b * taxa_crescimento_b
    ano += 1

    if pais_a < pais_b:
        continue
    else:
        print("A quantidade de anos necessárias para a população do país A ser igual ou ultrapassar a de B foi: {}"
              .format(ano))
        break