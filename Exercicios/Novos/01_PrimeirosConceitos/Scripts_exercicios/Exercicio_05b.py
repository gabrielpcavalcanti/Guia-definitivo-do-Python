"""
b) Declare dois números e formate eles das seguintes formas: mostre eles com vigula nas casas multiplas de 1000, transforme os dois em porcentagem, alinhe eles no meio, à direita e à esquerda."
"""

number_01: int = 100_000_000
number_02: float = 23.569

# Virgulas nas casas decimais multiplas de 1000.
print(f'{number_01:,}')
print(f'{number_02:,}')

# Em procentágem
print(f'{number_01:%}')
print(f'{number_02:%}')

# Alinhado no meio, à direita e à esquerda.
print(f'{number_01:^20}')
print(f'{number_01:>20}')
print(f'{number_01:<20}')

print(f'{number_02:^20}')
print(f'{number_02:>20}')
print(f'{number_02:<20}')
