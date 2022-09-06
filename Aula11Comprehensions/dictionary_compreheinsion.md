# Dictionary Compreheinsions

Segue a mesma lógica das list compreheinsions, mas agora iremos criar um dicionário, não mais uma lista.

Sabemos que dicionários possem chave e valor, podemos colocar qualquer tipo de dados neles, então podemos criar qualquer dicionário que quisermos.

a sintaxe é a mesma das list compreheinsions, so substituir os [ ] por { }.

```Python
{"chave": "valor" for valor ou interavel ou chave in iteravel}
```

vamos ver alguns exemplos:

```Python
numeros = [1, 2, 3, 4, 5]

quadrado = {numero: numero ** 2 for numero in numeros}

print(quadrado)

```

```Python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```Python
string = "abcde"
numeros = range(1,6)

correspondencia = {string[i]: numeros[i] for i in range(0, len(string))}

print(correspondencia)
```

```Python
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

```Python
numeros = range(1, 51)

pares = {numero: ("par" if numero % 2 == 0 else "impar") for numero in numeros }

print(pares)
```

```Python
{1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar', 6: 'par', 7: 'impar', 8: 'par', 9: 'impar'}
```