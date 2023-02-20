# Dicionários

Fazendo uma relação entre dicionários em Python e sua definição, temos que no Python ele é
formado com chaves e valores, correspondendo com a palavra e sua definição.

Em algumas linguagems de programação, dicionários são conhecidos como mapas.

Os valores podem ser qualquer tipos de dados e as chaves geralmente são Strings, mas pode ser
um inteiro, por exemplo, ou qualquer tipo de dado.

Os dicionários são declarados por { } e as chaves e valores são separados por : . Cada par chave-valor é separado por vírgula.

Obs: Não é possível usar a palavra **dict** já que é reservada.

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}
```

Outra forma de criar dicionário é por meio da palavra **dict**. Não é uma forma usual, mas é possível ser feita.

```Python
dic_2 = dict(br="Brasil", eua="Estados unidos", can="Canadá")
```

Uma forma ainda mais estranha de cirar dicionários é pelo método .fromkeys( ). Ele recebe dois parâmetros, um iteravél e um valor. Vejamos as possibilidades:

```Python

# Primeira forma

outro = {}.fromkeys("a", "b")
 
print(outro) 

# Segunda forma

usuario = {}.fromkeys(["nome", "pontos", "email"], "desconhecido")

print(usuario) 

# Terceira forma

teste = {}.fromkeys(range(1, 11), "novo")

print(teste)

```
```Python
{'a': 'b'}
{'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido'}
{1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}
```

## Acessando dados dos dicionários

Funciona da mesma forma das listas ou truplas, só com a diferença que não vai mostrar o índice e sim o seu valor associados.

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}

print(dic['pri'])
print(dic['terc'])

```

```python
1
3
```

Outra forma de acessar elemento de um dicionário é por meio do método .get( ).

```Python
dic_2 = dict(br="Brasil", eua="Estados unidos", can="Canadá")

print(dic_2.get("br"))
print(dic_2.get("ru"))

pais = dic_2.get("ru", "Não encontrado") #Podemos colocar um parâmetro opcional que é acionado quando o valor da chave não é encontrado no dicionário.

print(pais)

```

```Python
Brasil
None
Não encontrado
```

Podemos ainda acessar somente as chaves ou valores, utilizando os métodos values( ) e keys( ).

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}

print(dic.keys())
print(dic.values())

```

```python
dict_keys(['pri', 'sec', 'terc'])
dict_values([1, 2, 3])
```

## Verificar se um elemento está dentro de um dicionário 

Igual a qualquer tipo de dado, utilizamos o termo **in** para fazer essa verificação.

```Python
dic = {'pri': 1, 'sec': 2, 'terc': 3}

print('pri' in dic)
print('prie' in dic)

if 'pri' in dic:
    print("Está no dicionário")

else:
    print("Não está no dicionário")

```

```Python
True
False
Está no dicionário
```

## Criando elementos e adcionando em um dicionário

Igual a listas, dicionários também são mutáveis. Para acionior um elemento no dicionário, fazemos igual as listas.

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}

dic['quat'] = 4

print(dic)

```

```Python
{'pri': 1, 'sec': 2, 'terc': 3, 'quat': 4}
```

É possível também fazer mudanças em elemento do dicionário utilizando essa mesma forma de criar e adcionar elementos.

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}

dic['pri'] = 4

print(dic)

```

```Python
{'pri': 4, 'sec': 2, 'terc': 3} 
```

## Adicionando um dicionário a outro

Utilizamos o método upadate( ).

```python
dic = {'pri': 1, 'sec': 2, 'terc': 3}
dic_3 = {'quart': 4, 'quit': 5, 'sext': 6}

dic.update(dic_3)

print(dic)
```

```python
{'pri': 1, 'sec': 2, 'terc': 3, 'quart': 4, 'quit': 5, 'sext': 6}
```

## Limpando e deletando um dicionário

Para limpar os elementos de um dicionário, usamos o método clear( ) e para efetivamente deletar, usamos a palavra del.

Se quisermos só deletar um elemento, usamos o pop( ).

```python
dic_4 = {4: 3, 45: 4, 'banana': 'fruta'}

dic_4.pop()

print(dic_4)

dic_4.clear()

print(dic_4)

del dict_4

print(dic_4)

```

```python
{4: 3, 45: 4}
{ }
NameError: name 'dict_2' is not defined
```

## Tamanho de um dicionários

Usamos a função len( ).

```python
dic_5 = {'maca': 3, 'pera': 4, 'banana': 9}

print(len(dic_5))

```

```python
3
```

# Valor máximo, mínimo e soma nos dicionários

Funciona da mesma forma que as listas, mas aqui todos os valores tem que ser do tipo numérico. Caso, não seja, dará erro.

```python
dic_5 = {'maca': 3, 'pera': 4, 'banana': 9}

print(sum(dic_5.values()))
print(max(dic_5.values()))
print(min(dic_5.values()))

```

```Python
16
9
3
```

# Copiar um dicionário

Há duas maineiras de fazer isso, utilizando o método .copy( ) ou fazendo um shellow copy (que altera ambos os dicionários).

```Python
dic_5 = {'maca': 3, 'pera': 4, 'banana': 9}

dic_6 = dic_5.copy()

print(dic_6)

dic_6["novo"] = "sim"

print(dic_5)
print(dic_6)

```

```Python
{'maca': 3, 'pera': 4, 'banana': 9}
{'maca': 3, 'pera': 4, 'banana': 9}
{'maca': 3, 'pera': 4, 'banana': 9, 'novo': 'sim'}
```

```Python
dic_5 = {'maca': 3, 'pera': 4, 'banana': 9}

dic_6 = dic_5

print(dic_6)

dic_6["novo"] = "sim"

print(dic_5)
print(dic_6)

```

```Python
{'maca': 3, 'pera': 4, 'banana': 9}
{'maca': 3, 'pera': 4, 'banana': 9, 'novo': 'sim'}
{'maca': 3, 'pera': 4, 'banana': 9, 'novo': 'sim'}
```

## Iterando sobre dicionários

Podemos iterar sobre dicionários tmb. Funciona da mesma forma de qualquer tipo de dado iteravél em Python. Veremos agora várias possibilidades: 

```Python
dic_7 = {'pri': 1, 'sec': 2, 'terc': 3, 'quart': 4, 'quit': 5, 'sext': 6}

for i in dic_7:
    print(i)

print()

for i in dic_7:
    print(dic_7[i])

```

```Python
pri
sec
terc
quart
quit
sext

1
2
3
4
5
6
```

```Python
dic_7 = {'pri': 1, 'sec': 2, 'terc': 3, 'quart': 4, 'quit': 5, 'sext': 6}

for i in dic_7:
    print(f"Chave: {i} e valor com valor {dic_7[i]}")

```

```Python
Chave: pri e valor com valor 1
Chave: sec e valor com valor 2
Chave: terc e valor com valor 3
Chave: quart e valor com valor 4
Chave: quit e valor com valor 5
Chave: sext e valor com valor 6
```

```Python
dic_7 = {'pri': 1, 'sec': 2, 'terc': 3, 'quart': 4, 'quit': 5, 'sext': 6}

for i in dic_7.values():
    print(i)

print()

for i in dic_7.keys():
    print(i)

```

```python
1
2   
3   
4   
5   
6   
    
pri 
sec 
terc
quart
quit
sext
```

```Python
dic_7 = {'pri': 1, 'sec': 2, 'terc': 3, 'quart': 4, 'quit': 5, 'sext': 6}

for i, j in dic_7.items():
    print(f"chave: {i}, valor: {j}")
    
```

```Python
chave: pri, valor: 1
chave: sec, valor: 2
chave: terc, valor: 3
chave: quart, valor: 4
chave: quit, valor: 5
chave: sext, valor: 6
```
