# Break e continue

O while e o for permite a utilização de dois comandos: break e continue. A função deles é parar a excução de um pedaço do loop, no caso do continue
ou de todo o loop, no caso do break.

O continue é posto quando queremos analizar uma condição dentro do blobo while. Quando o bloco da condição terminar, o loop volta a funcionar
normalmente.

```python
n = 0

while n <=5:
    if n == 3:
        print(25)
        n += 1
        continue
    print(n)
    n += 1

```
```Python

0
1
2
25
4
5
```

O comando break é mais agressivo. No momento que ele é executado, o bloco do while se encerra por completo.

```python
x = 0

while x <= 10:
    if x == 6:
        break
    print(x)
    x += 1

```
```Python
0
1
2
3
4
5
6
```

Segue abaixo dois exemplos mais complexos:

```python
print("Exemplo 1")

while True:
    nota =int(input("Digite uma nota de 0 a 10: "))

    if nota < 0 or nota > 10:
        continue
    else:
        print("O valor é válido é vale:", nota)
        break

print()

# Podemos também fazer uma condição para Strings

print("Exemplo 2")

usuario = input("Digite o seu usuário: ")
senha = input("Digite sua senha: ")

while usuario == senha:
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite sua senha: ")
if usuario != senha:
    print(usuario)
    print(senha)

print()
```

No caso do for, funciona da mesma forma, segue um exemplo:

```Python
for i in range(10):

    if i % 2 == 0:
        print(i)
        continue

    if i == 7:
        print("Foi digitado o 6 e o programa parou.")
        break

```
```Python
0
2
4
6
Foi digitado o 6 e o programa parou
```
