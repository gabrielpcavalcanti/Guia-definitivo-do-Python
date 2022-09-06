numeros = range(1, 10)

pares = {numero: ("par" if numero % 2 == 0 else "impar") for numero in numeros }

print(pares)