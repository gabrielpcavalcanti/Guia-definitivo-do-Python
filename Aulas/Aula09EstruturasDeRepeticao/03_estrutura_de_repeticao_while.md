# Estrutra de repetição: While

É o segundo tipo de estrutura de repetição vista no Python, funciona de forma um pouco diferente do for, veremos a seguir.

A estrutura do while funciona da seguinte maneira:

```python
while #condição:
    pass
```

While significa equanto, ou seja, enquanto uma certa condição for verdadeira executa o bloco de comando. Em algum momento a condição tem que ficar falsa, porque se não, o loop se torna infinito.

```python
n = 0

while n < 10:
    print(n)
    n += 1

```
```Python
0
1
2
3
4
5
6
7
8
9
```

Perceba que dentro do bloco de comando, é posto um incremento para a variável n. Se isso não ocorre, o loop fica infinito. Não necessáriamento o loop tem que finalizar, há casos que o loop fica infinito de propósito, como o de uma janela aberta quando roda um programa (ela tem que ser infinita, se não o programa fecha sem o controle do usuário).

## While else

Podemos acresentar um else após o bloco de comando do while terminar. Isso serve para quando a condição do while for falsa, um outro bloco de comando ser execultado.

Lembrando que não é obrigatório uso do else, apenas opcional. Nem todas as linguagens permitem isso, no python é possível.

```python
n = 0

while n < 10:
    print(n)
    n += 1

else:
    print()
    print(f'O valor de n é {n}')
    print("Esse comando é utilizado quando n for igual a 10.")

```

```Python
0
1
2
3
4
5
6
7
8
9

O valor de n é 10
Esse comando é utilizado quando n for igual a 10.
```

## Alguns usos do While 

* O primiro jeito de usar o while é fazendo com que ele conte uma lista de números. Para isso é necessário colocar um condição de pausa, para que a lista não seja infinita. 

```Python
c = 1
while c <= 10:
    print(c)
    c += 1

print()

# Se quisermos colocar o os números correndo na horizontal, basta colocar print(x, end=' ')

x = 1
while x <11:
    print(x, end=' ')
    x = x + 1
 
print()

# Se quisermos colocar os números numa lista, basta fazer o seguinte.

z = 1
lista = []
while z <=10:
    lista.append(z)
    z += 1
print(lista)

print()

```
```Python
1
2
3
4
5
6
7
8
9
10

1 2 3 4 5 6 7 8 9 10 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

* O segundo modo de usar o while é combinado com as condições. Com elas, podemos decidir se o loop continua rodando ou ele para.
Podemos testar diversas condições, como visto a seguir:

```Python
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
