# Algumas funções integradas

Veremos aqui algumas funções integradas no Python.

## Sorted( )

funciona quase da mesma forma do método sort( ) visto em listas, com a diferença dele funcionar com qualquer iterável e retorna uma lista 
nova, não modifica uma já existente. Sempre retorna uma lista, mesmo que o dado original não for.

```Python
num = [1, 5, 9, 14, 55, 77]
num_2 = (0, 4, 45, 3, 23, 41)

num.sort()
print(num)

print(sorted(num))

new_list = sorted(num_2)
print(new_list)

print(tuple(new_list))
```

```Python
[1, 5, 9, 14, 55, 77]
[1, 5, 9, 14, 55, 77]
[0, 3, 4, 23, 41, 45]
(0, 3, 4, 23, 41, 45)
```

Temos outros parâmetros que podemos utilizar com a função sorted( ), como é o caso do reverse. 

```Python
num_2 = (0, 4, 45, 3, 23, 41)

print(sorted(num_2, reverse=True))
```

```Python
[45, 41, 23, 4, 3, 0]
```

## Reversed( )

Assim como o sorted( ), o reversed( ) funciona para todos os conjutos de dados e não somente listas, como é o caso do método reverse( ). Ele gera um objeto diferente. É preciso
utilizar o cast para tansformar ele em lista ou trupla.

```Python
num_3 = (1, 5, 5, 6, 8, 2)

print(list(reversed(num_3)))
```

```Python
[2, 8, 6, 5, 5, 1]
```

## Máx e Mín 

São duas funções já conhecidas, mas elas podem funcionar de formas mais interessantes, além de indicar o valor máximo ou mínimo de uma coleção.

A primeira maneria é uma forma mais simples de comparar valores. Normalmenta utilizmos condicionais, mas podemos usar max( ) e min( ), diretamente.

```Python
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um número: "))

print(f'O valor máximo entre esses números é {max(num_1, num_2)}')
print(f'O valor máximo entre esses números é {min(num_1, num_2)}')

```

Podemos ainda utiizar expressões lambdas com as funções max( ) e min( ).

```Python
nomes = ["Gabriel", "Sofia", "Maria", "José"]

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

```

```Python
Sofia
Gabriel
Gabriel
José
```
