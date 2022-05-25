# Tipo String

Representa qualquer tipo de texto em Pyhton, independente de ser apenas um caractere ou um texto inteiro. Para criar Strings basta usar aspas simples ou aspas dupas.

É possível colocar aspas simples dentro de aspas duplas e vice-versa. O que quero dizer é que se começar uma String com aspas dupas, tem que terminar com aspas duplas, mas dentro da String pode haver aspas simples. O caminho contrário também funciona.

Podemos armazenar Strings em variáveis e fazer algumas operações utilizando métodos. Para quem não sabe, métodos é uma ação que o Python pode execultar em um dado. Todo método é seguido de parênteses. 

Lembre: Se quiser verificar os métodos, utilize a função dir( ). E se quiser saber para que serve, utilize a função help( ).

```python
string_1 = "oi tudo bem"
string_2 = 'isso é uma string utilizando aspas simples'
string_3 = " começa com aspas duplas, mas 'posso escrever coisas com aspas simples dentro das aspas duplas', mas tenho que terminar com aspas duplas "
string_4 = 'o mesmo vale para as "aspas simples" '
```

Se uma Sring ficar muito grande, podemos separar ela com o comando \n. Quando o Python for ler esse termo, ele pulará uma linha e continuará escrevendo.

```python
string_5 = "teste para o comando \nesse texto está na linha de baixo"
print(string_5)
```

```python
teste para o comando
esse texto está na linha de baixo
```

```python
print(dir("teste"))
```

```python
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```

Alguns desses métodos são interessantes, veremos alguns.

* upper: Transforma todas as letras em maiúscula.

```python
nome = "cachorro feliz"
print(nome.upper())
```

```python
CACHORRO FELIZ
```

* lower: Transforma todas as letras em minúsculo.

```python
nome_1 = "Fulano De Tal"
print(nome_1.lower())
```

```python
fulano de tal
```

* title: Transforma a primeira letra de cada palavra em maiúsculo.

```python
nome_2 = "amor de mae"
print(nome_2.title())
```

```python
Amor De Mae
```

* capitalize: Trasnforma a primira letra da String em maiúsculo.

```python
nome_4 = 'eu sou feliz'
print(nome_4.capitalize())
```

```python
Eu sou feliz
```

* split: Cria uma lista com as palavras da String. O separador padrão e o espaço.

```python
nome_3 = "amor de pai"
print(nome_3.split())
```

```python
['amor', 'de', 'pai']
```

* Todas que começam com is: Verifica o valor lógico da expressão. Por exemplo, isnumeric, verifica se é numérico. Veremos algumas.

```python
# isnumeric: Verifica se é um número.

nome_5 = '473'
print(nome_5.isnumeric())
```

```python
True
```

```python
# isupper: Verifica se está em maiúsculo.

nome_6 = 'iowww'
print(nome_5.isupper())
```

```python
False
```
```python
# isspace: Verifica se possui espaços.
nome_7 = 'arvore'
print(nome_7.isspace())
```

```python
False
```

* Strip: Remove os espaços em branco de uma String. Possui duas variações lstrip() e rstrip(). 

```python
s = " teste "
s_strip = s.strip() # Remove o espaço em branco de cada lado.
s_lstrip = s.lstrip() # Remove o espaço em branco do lado esquerdo.
s_rstrip = s.rstrip() # Remove o espaço em branco do lado direito.

print(s)
print(s_strip)
print(s_lstrip)
print(s_rstrip)
```

```python
 teste 
teste
teste 
 teste
```

Podemos fazer o chamado slice de Strings. Cada caracter de uma String possie um índice. Começa em 0 e vai até a quantidade de caracteres. O slice permite escolher quis indices mostrar. colocamos os ídices dentro de [n:p:q].

n: indica o primiro caracter que vai parecer.

p: indica o ultimo caracter que vai parecer - 1. exemplo: 'teste'[0:3] -> te. O intervalo que Python trabalha é fechado aberto, ou seja, o primeiro termo está incluso, mas o último não.

q: indica a quantidade de 'pulos' até o próximo caracter. Imprime o primeiro, pula uma certa quantidade, indicada pelo usuário, imprime o outro, até acabar.

dica: Para descobrir a quantidade de termos de uma String, lista, trupla, dicionário, utilize a função len( ).

```python
nome_8 = 'teste para o slice'

print(len(nome_8))

print(nome_8[4]) 
print(nome_8[1:7])
print(nome_8[4:9])
print(nome_8[::-1])
print(nome_8[:9:3])
```

```python
18
e
este p
e par
ecils o arap etset
ttp
```

No python é possível criar variáveis e colocar-las dentro de Strings. Há três formas de fazer isso:

* Utilizando a ,

```python
num = 5
num_2 = 4.3

print("Esse é o número" , num,  " e esse é o número" , num_2)
```

```python
Esse é o número 5  e esse é o número 4.3
```

* Utilizando o .format()

```python
num = 5
num_2 = 4.3
num_3 = 45.84815178181

print("Esse é o número {}, esse é o número {}e esse é o número {}. Arredondando o tereiro número, temos: {:.2f}".format(num, num_2, num3, num3)) # :.2f arredonda número real para duas casas decimais.
```

```python
Esse é o número 5, esse é o número 4.3 e esse é o número 45.84815178181. Arredondando o tereiro número, temos: 45.85
```

* utilizando as f-Strings

```python
num = 5
num_2 = 4.3
num_3 = 45.84815178181

print(f'Esse é o número {num}, esse é o número {num_2}e e esse é o número {num_3}. Arredondando o tereiro número, temos: {round(num_3, 2)}') # round() arredonda número real para quantas casas decimais quisermos.
```

```python
Esse é o número 5, esse é o número 4.3 e esse é o número 45.84815178181. Arredondando o tereiro número, temos: 45.85
```

Podemos cocatenar duas Strings utlizando o +

```python
nome_9 = "oi,"
nome_10 = " tudo bem"

print(nome_9 + nome_10)
```

```python
oi, tudo bem
```

E por fim, podemos 'multiplicar' Strings. A multiplicação nesse caso faz a String repetir n vezes.

```python
nome_11 = "oi"

print(5 * nome_11)
```

```python
oioioioioi
```
### SyntaxError

A medida que evoluimos na programação, percebemos que nem tudo são flores. Iremos nos deparar
com diversos tipos de erros no nossos programas e temos que estar preparados para corrigi-los.

Com o tempo conseguimos indentificar qual é o tipo de erro e como resolver seu problema.

obs: Para mais detalhes sobre cada um dos tipos de erros, visite essa aula:
começe desde cedo a entender os tipos de erros para quando começar a estudar eles efetivamente, ficar tudo mais fácil de compreender.

Um dos erros mais comuns quando estamos falando de Strings é o erro de sintaxe. Ele ocorre
quando o python não reconhce uma secção do código como sendo válida. 

Um exemplo é o caso de confundir no uso aspas simples e duplas no meio de uma String.
