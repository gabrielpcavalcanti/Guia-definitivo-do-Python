# Operadores Lógicos

São dois os operadores Loógicos. Sempre retornam um valor booleano, ou seja, verdadeiro ou falso.

* 'E': Simbolizado por and.
* 'OU': Simbolizado por or.

### Tabela verdade do E:

O valor so vai ser verdadeiro se as duas condições forem verdadeiras. O resto vai ser falso.

``` Python
print(True and True) 
print(True and False) 
print(False and True) 
print(False and False) 
```

```python
True
False
False
False
```

### Tabela verdade do OU:

O valor so vai ser falso se as duas condições fore, falsas

```Python
print(True or True) 
print(True or False) 
print(False or True) 
print(False or False) 
```

``` Pyhton
True
True
True
False
```

podemos tambem ter a operação de negação, representada pela palavra not. Ela muda o valor de verdade.

``` Python
a = True
b = False

print(not a)
print(not b)
```

```python
False
True
```
