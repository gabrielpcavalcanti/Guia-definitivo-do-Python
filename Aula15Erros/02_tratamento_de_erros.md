# Tratamento de erros

Aprendendo os principais tipos de erros, o que devemos fazer agora é o tratamento deles. Quando estamos desenvolvendo uma aplicação
não faz mal aparecer o erro, basta corrigi-lo e seguir em frente. Agora quando o usuário estiver utilizando seu código, não pode aparecer erro algum ou o mínimo possível. Então utilizaremos o tratamento de erro para percorrer todos os possíveis erros que possam acorrer.

A dica de Ouro é a seguinte: Toda entrada de dados deve ser tratada!

Essa é a melhor prática que você pode ter saber quando utilizar o tratamento de erros. Lembre-se: A "função" do usuário é destruir seu sistema, então trate todos os erros possíveis.

Para tratar erros no Python utilizamos o bloco try/except.

```Python
try:
    # codígo que será testato.

except:
    # trata o erro. O que deve ser feito caso de problema.
```

## Tratando um erro genérico

Quando não queremos tratar um erro em específico, utilizamos apenas o except.

```Python
try:
    funcao()
except:
    print("Deu erro")


```

```Pyhton
Deu erro
```

## Tratando um erro específico

Quando sabemos o tipo de erro que pode acontecer, podemos trata-lo individualmente e até dar um apelido para que possamos utiliar a mensagem de erro no nosso código. Para fazer isso Coloque o nome do erro após o comando except. Caso queira dar o apelido, use o comando "as" após o nome do erro. 

```Python
try:
    primt('oi')

except NameError:
    print("É um erro de nome.")
```

```Python
É um erro de nome.
```

```Python
try:
    len(5)

except TypeError as erro:
    print(f"O tipo de erro foi: {erro}")


```

```Python
O tipo de erro foi: object of type 'int' has no len()
```

## Tratamento de múltiplos erros

Numa mesma passagem de código é possível que aconteça várias tipos de erros, podendo trata-los ao mesmo tempo.

```Python
try:
    num = int(input("Digite um número: "))
    num2 = num + num3
    
except ValueError  as erro:
    print(f"O tipo de erro foi: {erro}")

except NameError as erro2:
    print(f"O tipo de erro foi: {erro2}")


```

```Python
# Caso não digite um número
O tipo de erro foi: invalid literal for int() with base 10: 'o'

# Caso dgite um número
O tipo de erro foi: name 'num3' is not defined
```

## Tratamento de erro dentro de funções 

Podemos tratar erros dentro de funções. No caso, ela só irá execultar caso não haja nenhum erro.

```Python
def pega_valor(dicionario, chave)
    try:
        return dicionario[chave]
    except KeyError:
        return None 

dic = {"nome": "Gabriel"}

print(pega_valor(dic, "nome"))
print(pega_valor(dic, 4))

```

```Python
Gabriel
None
```

## Uso do else e do finally 

Podemos complementar o tratamento de erros utilizando o comando else e o comando finally. O primeiro somente é execultado caso não haja nenhum erro no sistema e o outro execulta caso haja o erro ou não. 

```Python
try:
    num = int(input("Digite um número: "))

except ValueError:
    print("Tem erro de valor")

else:
    print(num)


```

```Python
# opção 1
tem um erro no valor

# opção 2
# Qualquer número que digitar
```

```Python
try:
    num = int(input("Digite um número: "))

except ValueError:
    print("Tem erro de valor")

else:
    print(num)

finally:
    print("Acabou o programa")

    
```

```Python
# opção 1
Tem erro de valor
Acabou o programa

# opção 2
# Qualquer valor que digitar
Acabou o programa
```
