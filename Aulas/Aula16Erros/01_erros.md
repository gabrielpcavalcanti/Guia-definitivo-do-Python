# Erros

Nós erramos a todo o momento, em qualquer esfera da vida. Temos que aprender a lidar com eles para que nunca mais se repitam. Na programação não é diferente, ainda mais quando se está aprendendo, erramos muitas e muitas vezes.

O que é impotante na programação é saber ler a mensagem de erro, identificar onde está o erro, qual o tipo de erro e como corrigi-lo ou trata-lo. Veremos tudo isso nessa aula.

obs: O interpretador do Python para de executar o código quando ele encontra algum erro, tenha em mente isso.

## Ler mensagem de erro.

A mensagem muda de terminal para terminal, IDE para IDE, mas todas são muito parecidas. Nela possui onde está o erro e qual o nome dele. Alguns ainda mostram com detalhe tudo isso.

```Python
printf("oi")
```

```Python
Traceback (most recent call last):
  File "c:\Users\Avell\Documents\GitHub\Python_teoria\teste_erro.py", line 1, in <module>
    printf("oi")
NameError: name 'printf' is not defined. Did you mean: 'print'?
```

Nesse caso, ele mostrou em qual o arquivo ele está executando: "c:\Users\Avell\Documents\GitHub\Python_teoria\teste.3.py", a linha em que o erro ocorreu: line 1,
mostra o conteudo da linha: printf("oi") e o tipo de erro junto com uma possível solução: NameError: name 'printf' is not defined. Did you mean: 'print'?.

Saber ler isso é essencial para que possa corrigi-los ou trata-los. Com o tempo conseguimos indentificar qual é o tipo de erro e como resolver seu problema.

## Erro mais comuns no Python

* NameError

Ocorre quando uma variável ou funçao não foi definida.

```Python
max(num) # Variável num não definida.
printf("oi") # função printf não existe e portando não é definida.
```

```Python
Traceback (most recent call last):
  File "c:\Users\Avell\Documents\GitHub\Python_teoria\teste_erro.py", line 1, in <module>
    max(num) # Variável num não definida.
NameError: name 'num' is not defined. Did you mean: 'sum'?
```

* SyntaxError

Ele ocorre quando o python não reconhce uma secção do código como sendo válida. Você escreve algo que o Python não reconhece como parte da linguagem.

```Python
input('oi' # Faltou fechar os parênteses.
def funcao() # Esqueceu o :.
class = 2 # palavra reservada.
```

```Python
File "c:\Users\Avell\Documents\GitHub\Python_teoria\teste_erro.py", line 2
    input('oi' # Faltou fechar os parênteses.
         ^
SyntaxError: '(' was never closed
```

Veja que ele so mostrou o primeiro erro. Assim que ele identifica o erro, o programa para a execussão e tudo que vinher 
depois não é lido.

* TypeError

Ocorre quando uma função/operação/ação é aplicada a um tipo de dado errado.

```Python
print('oi' + 5) # Não podemos somar um tipo str com um tipo int.
```

```Python
Traceback (most recent call last):
  File "c:\Users\Avell\Documents\GitHub\Python_teoria\teste_erro.py", line 1, in <module>
    print('oi' + 5) # Não podemos somar um tipo str com um tipo int.
TypeError: can only concatenate str (not "int") to str
```

* IndexEroor

Ocorre quando tentamos acessar um índice de um dado e esse índice não existe.

```Python
nums = [1,2,3,4,5]

print(nums[6]) # Não existe indice 6 na lista nums.
```

```Python
Traceback (most recent call last):
  File "c:\Users\Avell\Documents\GitHub\Python_teoria\teste_erro.py", line 3, in <module>
    print(nums[6]) # Não existe indice 6 na lista nums.
IndexError: list index out of range
```

* ValueError

Ocorre quando uma função que pertence ao Python recebe argumentos com o tipo correto mais inapropiados.

```Python
 print(int('oi')) # Não temo como converter uma palavra em int, teria que ser um número
```

```Python
File "c:\Users\gabri\OneDrive\Documentos\GitHub\Python_teoria\teste_erro.py", line 1
    print(int('oi'))
IndentationError: unexpected indent
```

* KeyError

Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

```Python
carros = {'Ford': 'Focus', 'Fiat': 'Uno', 'BMW': ' X1'}

print(carros['Toyota'])
```

```Python
Traceback (most recent call last):
  File "c:\Users\gabri\OneDrive\Documentos\GitHub\Python_teoria\teste_erro.py", line 3, in <module>
    print(carros['Toyota'])
KeyError: 'Toyota'
```

* AttributeError

Ocorre quando usamos função que não são atribuidas a certo tipos de dados.

```Python
trupla = (1,2,3,4)

trupla.sort() # Não existe a função sort() para truplas.
trupla.upper() # Não existe a função upper() para truplas.
```

```Python
Traceback (most recent call last):
  File "c:\Users\gabri\OneDrive\Documentos\GitHub\Python_teoria\teste_erro.py", line 3, in <module>
    trupla.sort() # N�o existe a fun��o sort() para truplas.
AttributeError: 'tuple' object has no attribute 'sort'
```

* IndentationError

Ocorre quando não respitar a identação do Python.

```Python
def funcao(): # Não está identado.
pass

for i in range(5): # Não está identado.
print(i)
```

```Python
  File "c:\Users\gabri\OneDrive\Documentos\GitHub\Python_teoria\teste_erro.py", line 2
    pass
    ^
IndentationError: expected an indented block
```
