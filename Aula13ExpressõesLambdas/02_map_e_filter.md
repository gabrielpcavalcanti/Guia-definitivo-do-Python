# Map e filter

São duas funçãoes do Pyhton que funcionam muito bem com expressões lambdas. Elas possuem as mesmas caracaterísticas, mas realizam tarefas diferentes, vejamos cada uma delas.

## Map

Map é uma função do Python que facilita nossa vida de uma forma bem interessante. Cria um objeto contendo todos os valores retornados de uma função ou de uma expressão lambda e que pode ser utilizado apenas uma vez, antes do conteúdo presente seja deletado, ajundando no gerenciamento de memória. 

O único "defeito" do Map é que só é possível utilizar o Map para funções e lambdas que contenham um parâmetro. 

Se ficou perdido, vamos ver como a sintaxe funciona e um exemplo prático.

```Python
variavel = map('função ou lambda', 'iteravel')
```

A função Map recebe dois argumentos: uma função ou lambda e um iterável. O iterável será o parâmetro da função ou do lambda. O Map vai criar um objeto que pode ser transformado em qualquer outro tipo de dado, mas geralmente utilizamos listas ou truplas.

Vejemos um exemplo:

```Python
def quadrado(num):
    return num ** 2


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(quadrado, numeros))

print(quadrados)

```

```Python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

criamos a função quadrado, que recebe apenas um valor e uma lista contendo números. Cada número da lista funciona como parâmetro dentro da função. Map percorre todos os valores e retorna um objeto que será transformado por uma lista.

Agora um outro exemplo, utilizando lambdas:

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubo = list(map(lambda x: x ** 3, numeros))

print(cubo)

```

```Python
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

cuidado para não deletar o conteúdo do Map, ele vai deletar automaticamente, então tem que saber a hora de utililzar o conteúdo dele.

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubo = map(lambda x: x ** 3, numeros)

print(list(cubo))
print(list(cubo))

```

```Python
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
[]
```

## Filter

O filter server para filtrar dados de uma coleção. Criamos uma condição (será o filtro) e a função criará um objeto contendo todos os valores que passaram pelo filtro.
Tem uma "cara" muito similar com o Map, ambos possuem dois argumentos, funcionam apenas com funções de um parâmetro, e seu conteúdo é deletado após uma utilização.

Vamos ver um exemplo para entender como funciona e sua sintaxe.

```Python
variavel = filter('função ou lambda', 'iteravel')
```

```Python
numeros = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

valores_maiores_que_10 = list(filter(lambda valor: valor > 10, numeros))
valores_menores_que_10 = list(filter(lambda valor: valor < 10, numeros))

print(valores_maiores_que_10)
print(valores_menores_que_10)
```

```Python
[27, 64, 125, 216, 343, 512, 729, 1000]
[1, 8]
```

Temos uma aplicação bastante interessante com o filter. Em vez de utilizamos um parâmetro, podemos utilizar o None com o objetivo de fiiltrar dados nulos dentro de uma lista.

```Python
lista = ['oi', 'tudo bem', '', 'como vai', '', '', 'arroz']

lista_update = list(filter(None, lista))

print(lista_update)
```

```Python
['oi', 'tudo bem', 'como vai', 'arroz']
```

## Map e filtros juntos

Podemos utilizar essas duas funções combinadas. Primeiro fazemos um filtro e depois aplicamos o resultado a função ou lambda que desejar. Vamos ver como funciona.

```Python
nomes = ["Gabriel", "joão", "Sofia", "Rafael", "Larissa"]

nomes_up = list(map(lambda nome: f"{nome}", filter(lambda nome: len(nome) > 5, nomes)))
```

```Python
['Gabriel', 'Rafael', 'Larissa']
```

Se não entendeu, vou escrever ele de outra forma para que fique mais claro. Apenas "quebrei" o código em pedaços para que fique mais fácil a organozação.

```Python
nomes = ["Gabriel", "joão", "Sofia", "Rafael", "Larissa"]

filtro = filter(lambda nome: len(nome) > 5, nomes)

nomes_final = map(lambda nome: f"{nome}", filtro)

print(list(nomes_final))
```

```Python
['Gabriel', 'Rafael', 'Larissa']
```
