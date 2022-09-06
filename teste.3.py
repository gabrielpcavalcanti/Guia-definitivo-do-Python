numeros = range(1,50)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(pares)
print(impares)