# Expressões Lambdas

São funções que não possuem nome. 

Podemos criar uma função ou criar uma expressão lambda. Elas irão fazer a mesma coisa. Então pode se perguntar: pq existe esse tipo de expressão? 
O uso dela como uma função própia não é muito útil e quase não se usa, mas elas servem para coletar dados em argumentos específicos dentro de funções.

Tudo que você pode fazer com funções é possícel fazer com lambdas. Com isso, todos os erros e possibilidades de funções são transportadas para lambdas.

Antes de verificar isso, vamos ver como uma expressão lambda funciona:

```Python
lambda parâmetros: retorno desejado
```

Sabendo disso, vamos ver como elas se comparam a funções

```Python
def soma(a,b):
    return a + b

print(soma(4,4))
print(soma(2,4))

soma_1 = lambda a,b: a + b

print(soma_1(4,4))
print(soma_1(2,4))
```

```Python
8
6
8
6
```

Perceba que não é muito útil essa implementação, utilizar funções funciona muito melhor do que lambdas, nesses casos.

Agora vamos ver uma aplicação que realmente faz as expressões lambdas se tornarem muito poderosas.

```Python
autores = ['Isaac Asimov' , 'Douglas Adams' , ' Ray Bradbury' , 'H. G. Wells' , 'Robert Heinlei' , 'Leigh Brackett', 'Arthur C. Clarkel', 'Frank Herbert' , 'Orson Scott Card'] 

autores.sort(key=lambda nome: nome.strip().split(' ')[-1].lower())

print(autores)
```

```Python
['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', ' Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarkel', 'Robert Heinlei', 'Frank Herbert', 'H. G. Wells']
```

Utilizamos uma expressão lambda dentro do argumento da função sort( ). Fazer isso para diversas funções diferentes é o que faz os lambdas serem poderosos.

Nas próximas aulas veremos algumas funções que funcionama muito bem com expressões lambda: Map, filter, reduce, any, all, generators, sorted, min, max, reversed, len, abs, sum, round e zip,
