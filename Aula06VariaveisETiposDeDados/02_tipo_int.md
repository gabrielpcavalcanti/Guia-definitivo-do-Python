# Tipo inteiro (int)

O tipo inteiro tem as mesmas propiedades e definições da matemática. Ele abrange todos
os números negativos, positivos e o zero que não tenha ponto flutuante - números decimais.

Podemos armazenar qualquer número inteiro dentro de variáveis e a partir dela fazer operaçãoes com outras variáveis ou com outros tipos numéricos.

```python
num = 459
num_1 = 5
num_2 = -10
num_3 = num_1 + num_2
num_4 = num_3 * num_3
num_5 = num_1 + (4 - num_4)

print(num)
print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)
```

```python
459
5
-10
-5
25
-16
```

Se o número interio for muito grande fica difícel de ler no computador, conseguir vizualizar com clareza. Para contornar isso é posível inserir  _  a cada tres números.

```python
num_6 = 1_000_000_000
num_7 = 1_356_478

print(num_6)
print(num_7)
```

```python
1000000000
1356478
```
