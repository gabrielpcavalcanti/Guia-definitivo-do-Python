# Padrões adotados no curso

No Python e em qualquer liunguagem de programação, existem boas regras de conduta a serem usadas e maneiras mais adequadas de escrever o código, tornado-o mais claro a todos. 

O PEP8 é um guia de estilo e o PEP257 é uma convensão para docstring, eles serão usado nesse curso. Além do mais, outros padrões serão utilizados e serão mostrados aqui (próprios e do clean code). É o que eu acredito ser a melhor forma de escrever um certo conceito da programação no python. Mas assim como na observação feita no arquivo do PEP8, se não enteder algum conceito, não fique assustado. 

Esse padrões não precisam ser adotados e você que escolhe eles. Uma vez adotado, siga com eles durante todo o projeto, para manter a consistencia. Escolhi eles porque acredito que seja a melhor forma de escreve e aprender Python.

Trecho retirado do livro clean code que expressa a motivação de ter bons hábitos: "Talvez você tenha pensado que “fazer funcionar” era a primeira ordem de negócios para um desenvolvedor profissional.  A funcionalidade que você cria hoje tem uma boa chance de mudar próxima versão, mas a legibilidade do seu código terá um efeito profundo em todas as alterações que serão feitas. O estilo de codificação e a legibilidade estabelecem precedentes que continuam a afetar a capacidade de manutenção e a extensibilidade muito depois de o código original ter sido alterado de forma irreconhecível. Seu estilo e sua disciplina sobrevivem, mesmo que seu código não."

Observações: 

- Não utilizarei tudo desde o início, mas com o tempo, mais tópicos serão dados e o padrão de escrita do código mudará um pouco até um ponto que vejo como sendo bem escrito. Não uso tudo desde o início, pq não há necessidade e ficaria muito complexo sem necessidade.

- Em projetos e em exercícios mais simples, a maioria desses padrões são desnecessários, mas com o passar o tempo, eles ficam mais complexos e a necessidade de adota-los fica maior, então usar o PEP8 e esses padrões é bom saber desde o início.

- Algumas vezes vai parecer que o código fica mais poluído, mas escrito de uma forma elegante, se torna muito útil, como veremos. Muitos dos padrões afetados aqui são obrigatórios em outros linguas, o pyhton da liberdade de escrever em diversas maneiras. 

- Alguns dos padrões adotados vão paracer com outras linguagens de programação. Não faria sentiso isso porque o Python facilita as coisas e tem sua própria forma de escrever e pode ser pedante de escrever, mas em pontos específicos, isso é bom e mostrarei aqui. 


## Índice  
1. [if \_\_name__ == '\_\_main__' e def main( )](#1---if-__name__--__main__-e-def-main-)  

## 1 - if \_\_name__ == '\_\_main__' e def main( ) Organização da presedencia de comandos

Arquivos não devem ter mais de 500 linhas. Tente contar uma história, com começo meio e fim.

Sempre siga essa ordem, se um dos elementos seguintes não estiver presente no código, não tem problema, a ordem continua. Primeiro os docstring -> imports -> constantes -> classes -> funcões -> código solto -> def main -> if name main. 

Dentro de cada um dessas partes, a parte que tiver mais escopo fica em cima da parte que tiver menos escopo. Cria uma hierequia, mesmo que não precise.

Esse if statement e a função main( ) será explicado com muito detalhe quando formos falar de funções, modulos e classes. 

O padrão adotado nesse curso é que eles sempre serão utilizados quando tiver esses conceitos explicitamente envolvidos. 

As ideias por trás de usar a segunda forma quando utilizarmos funções, modulos e classes são:

- Para o código ficar mais organizado;
- Distinhir quais arquivos são scripts e quais são modulos.

Eles podem ser utilizados desde o início, mas o código fica maior e sem necessidade, como mostrado em um exemplo bem simples.

```python
# Forma mais simples
print("Hello World!")

```

```python
# Forma mais "complexa"
def main() -> None:
    print("Hello World!")
 
 
if __name__ == '__main__':
    main()

```

Os dois códigos darão o mesmo resultado, mas veja com um é mais simples que o outro. Para o incío, não há a necessidade de utilizar todos esses comando, mas com o passar do tempo e complexidade do código, será extremamente útil e adotado em todos os programas.

A segunda forma lembra outras linguagens de programação, como o Java e pode ser familiar para quem já programa. A sintaxe muda, mas o programa é a forma é a mesma. 

Será explicado com mais detalhes na aula, mas o padrão adotado é nessa ordem, de cim para baixo: classes, funções, função main( ) e if \_\_name__ == '\_\_main__':.

```python
class Class:

    def __init__(self):
        pass

    def func01(self):
        pass

    def func02(self):
        pass


def func03() -> None:
    pass

def func04() -> None:
    pass

def main() -> None:
    pass
 
if __name__ == '__main__':
    main()

```

Dica: Para não ter que escrever sempre a função main( ) e if statement, algumas IDE`s já vem pré-configuradas e/ou você pode escrever um tamplate e configurar na própria IDE. 

## 2 - Padrões para nomes

Os padrões para nomes adotados seguirão a maiora dos concelhos vistos no livro clean code. Não vou usar tudo a risca, mas boa parte sim, são bons concelhos. 

Procure o livro Clean code de Robert C Martin para saber mais sobre o assunto.

Nomear variáveis, funções, classes, métodos e assim por diante é uma tarefa que parece fácil a princípio, mas se não for bem feita pode levar a problemas sérios. tem uma frase que diz: **"Nomear variáveis é 50% do código, e a outra metade é tentar entender o que você quis dizer."** Se você nomear de forma "correta", seguindo um padrão, fica muito mais simples entender o que está acontecendo no código.

Vamos ver os padões adotado:

### a) Nome de objetos sempre em inglês e pronunciáveis

Independente se for uma variável, classe, função, trupla etc. Todos os nomes tem que estar em inglês. É a lingua universal utilzada por todos os programadores, então não fuja dessa "regra".

Nunca crie nomes que não estejam no vocabulário da lingua inglesa e que sejam inponunciáveis, como abreciações e trocadilhos. Sempre escreva o nome de forma correta.

### b) Nao usar l ou O isolado nos nomes

O l minúsculo e o O maiúsculo se paracem muito com os números 1 e 0, respectivamente. Então não será utilizado de forma isolada para nomear objetos.

### c) Tamanho dos nomes

É uma questão relativa, um mesmo nome pode ser grande para você e pequeno para mim. Um objeto com uma unica palavra, independente da extenção dela, é o padrão.

Concidero nomes muito grandes quando são compostos por mais de cinco palavras, com exceção de preposição e sufixos e prefíxos. Então nunca use para nomear nada. Menos que isso, independete da extenção de cada palavra, é o padrão adotado aqui.

### d) Letra única para nomear objetos

letras únicas geralmente são utilizadas para objetos que não tem muita importancia no código ou são utilizadas para testes. Se se não tem importância, nao deve ser utilizado e se for utlilizado para teste, mude o nome depois no código final.

Usar letras para constantes também é comum. Não faça isso, fica ruim de pesquisar pelo código e podem significar situações diferentes. Sempre escreve o nome da constante em letras maiúsculas. É o padrão adotado aqui.

Não utilizaremos numeros seriados, como a1, a2, c3 etc

### e) Uso de prefixos e sufixos

**Ver o padrao utilizado depois, ainda nao defini**

### f) Nome de classes e metodos

Classes devem ser nomeadas com substantivos ou frases nominais e não ter verbos.

Já os métodos tem que ter verbo ou frases verbais.

## 3 - Type annotations

Essa feature do Python é muito útil e quase ninguém adota ela, principalmente no inicío, mas mesmo depois, poucos códigos eu vejo utilizam os type annotation. Se você viu em algum projeto ou repositório, de parabéns a quem escreveu, ele teve cuidado e carinho pelo programa escrito.

Usar o type annotations em Python facilita a leitura dos programas e te alerta quando alguma variável está sendo declarada ou usada de forma errada. Algumas IDE`s avisam do erro, mas é bom utilizar a biblioteca mypy para um melhor checagem dos type annotations.

Usar Type annotations não interfere na execução do código, por exemplo declarar uma variável de um tipo e colocar outro no lugar, não vai fazer o programa "crachar", mas ele te alerta que algo está errado. 

Type annotation ajudam a IDE a acessar os métodos do tipo escolhido para a variável ou avisar que algo está inconsistente. Isso agiliza na escrita do código.

Vejamos cada um deles agora:

### a) Tipos de variáveis primitivas

Colocamos os : e em seguida o tipo de dado que queremos para a variável. str para strings, int para interiros, float para números reais e bool para booleanos.

```python
name: str = "Sofia"
age: int = 10
pi_estimated float = 3.14
logic: bool = True

```

### b) Listas

No caso da lista, podemos colocar somente list após os : ou pode especificar o tipo de dados que a lista contém. Sempre será especificado o tipo.

Se tiver mais de um tipo de dado numa lista, utilize o | para isso. 

```python
random_values: list = [1, '20', True, 2, 4, 'oi']
numbers_int: list[int] = [1, 2, 3]
single_letters: list[str] = ["a", "b", "c"]
numbers: list[int | float] = [42, 3.14, 2.71, 76]

```

### c) Truplas

Nas truplas, varias possibilidades de type annotation aparecem. Primeiro, podemos usar so o tuple, mas sempre será especificado os tipo.

Como trupla é um tipo de dado imutável, é separado o tipo de dados pela vírugula e na ordem que aparece. Não utilize |

O certo seria colocar todos os tipos de dados que a truplas comporta, mas para a notação não ficar sobrecarregada, utilizamos os ...

```python
points: tuple[int, int] = (10, 20)
dates: tuple[str, int,  float] = ("Alice", 25, 1.75)
intergers: tuple[int, ...] = (1, 4, 6, 153, 76, 232)

```

### d) Dicionários

Nos dicionários, é possível so utilizar o dict ou especificar os dados dentro dos parênteses, da mesma forma que as truplas, pela vírgula.

```python
student_age_grade: dict[str, int] = {"idade": 25, "nota": 90}

```

### e) Conjuntos

Nos conjuntos é possível passar so o type annotation set ou com o(s) tipos especificados. Sempre o tipo será especificado.

```python
fruits: set = {'apple', 'orange', 'grapes'}
single_numbers: set[int] = {1, 2, 3}
random_set: set[int | str] = {1, 4, 5, 'play', 45}

```

### f) Em parametros e argumentos de funções

Se quiser mais de um tipo de dado num argumento de uma função, utilize o | para isso. Se quiser apenas um tipo de dado, continua da mesma forma.

Coloca-se -> após o argumentos para identificar o retorno da função. Caso a função não tenha retorno, coloque None. Se tiver mais de um tipo de dado a ser retornado, utilize o |.

Antigamente se usava o método Union da biblioteca typing, mas não vamos utiliar esse método.

```python
def sumation(a: int | str, b: int) -> int:
    return a + b


def filter_pers(numeros: List[int]) -> List[int]:
    return [n for n in numeros if n % 2 == 0]


def subtraction(num_01: int, num_02: int) -> None:
    print(num_01 - num_02)

```

Caso o parâmetro da função possa receber tanto um tipo quando None, utilizamos o | e não "tipo = None", a menos que so seja possível o tipo None.

```python
def greet(name: str | None) -> None:

    if name is None:
        print("Tipo None")
    else:
        print("Tipo String")
        
```

### g) Em classes 

As classes funcionam da mesma forma que as funções.

Quando instânciar uma classe, podemos utilizar o nome da classe como uma type annotation, isso é bem útil. Pode paracer um pouco repetição de notação, mas facilita a IDE e o mypy a funcionar de forma correta.

```python
class Person:

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f'Hello, my name is {self.name}!'


Alice: Person = Person("Alice", 25)

print(p.greeting())

```

## 4 - Padrões para String

### a) Sempre use f-strings

Mesmo podendo fazer a concatenação tradicional, é preferivel o uso de f-strings em todos os casos e será adotado aqui. Ele facilita a leitura e é mais simples de escrever.

```python
name: str = "Alice"
age: int = 25

# Without f-string
traditional_message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
print(traditional_message)

# Using f-string
fstring_message = f'Hello, my name is {name} and I am {age} years old.'
print(fstring_message)

```

### b) Use Raw strings para caminhos e regex

As Raw Strings (r"") são usadas para interpretar strings literalmente, sem processar caracteres de escape (\).

Use elas Strings com caminhos de arquivos no Windows e Expressões regulares (regex), onde \ é comum.

Sempre use r"" quando precisar de textos com \ que não devem ser interpretados!

```python
# Caminho de arquivos 

# Sem raw strings
path_file: str = "C:\\novo\\teste\\arquivo.txt"
print(path_file)

# Com raw strings
path_file: str = r"C:\novo\teste\arquivo.txt"
print(path_fiel)

```

```python
# Regex
import re

pattern: str = r"\d+"  # Instead of "\\d+"
text: str = "Age: 25 years"

result = re.findall(pattern, text)
print(result)

```

## 5 - Padrão para Neasting

### a) Não teremos estruturas aninhadas do mesmo tipo

Nesting é algo problemático na programação, então para evitar, simplismente não terá nesting de mesmo tipo em nenhum programa. O que quero dizer é que dentro de um if, não terá outro if, mas dentro de um for, podemos ter um if, mas não outro for. E assim com qualquer outro comando dentro do Python.

```python
# Não pode fazer isso 
for i in range(10):
    for j in range(100):
        
        if x:
            ...
        
# Pode isso
for i in range(10):

    if x:
        ...

```

## 6 - Padrão para arquivos

### a) Sempre use with para abertura e fechamento de arquivos

Podemos abrir e fechar arquivos com os métodos .open( ) e .close( ), mas caso tenha algum problema entre esses dois comandos, o arquivo nunca vai ser fechado. Para evitar problemas sempre utize with.

```python
# Using open() e close()
file = open("example.txt", "w")  
file.write("Hello, world!\n")
file.close()

# Using with open()
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
```

## 7 - Padrão para exceções

Lidar com erros é algo inerente na programação. Um programa não será bem escrito se não tiver que lidar com eles. O problema surge se você lida com tantos erros que você não sabe o que seu programa faz. É preciso separar bem as duas partes: a logica e o tratamento de erros.

### a) Sempre especifique as exceções 

Tanto no tipo específico da exceções quanto colocando uma mensagem para o erro mostrando a operação que falhou e o tipo da falha.

**EXEMPLOS DESSA PARTE**

### b) Todas as exceções e blocos try/exept devem estar dentro de funções

Um bom hábito é criar um funções que execulta um única tarefa. Criar funções que fazem uma tarefa e ainda tratam das exceções não é uma única tarefa. Então delegue funções apenas para tratar os erros.

```python
def divide(a: float, b: float):
    """Performs division and returns the result."""
    return a / b

def handle_division(a, b):
    """Handles exceptions when performing division."""
    try:

        result = divide(a, b)
        print(f"Result: {result}")

    # Correct and commonly used form.
    except ZeroDivisionError:
        print("Error: Attempt to divide by zero!")
        
    # Correct and commonly used form.
    except TypeError:
        print("Error: Invalid types! Make sure to provide numbers.")
    
    # Incorrect form
    except Exception as error:
        print(f"Unexpected error: {error}")

    # Even worse form.
    except:
        print(f"Unexpected error.")

```

### c) Não passe *null*

algumas vezes o usuário vai passar dados errados, previna que ele passe o dado *null*.

**EXEMPLOS DESSA PARTE**

### d) - Context maneger

## Padrões para aspas

Para a função print e input, sempre use aspas duplas, a menos que o print possua uma f-string.

```Python
print("Hello, World!")
print(f'Hello, World!')

input("Digite seu nome: ")
```

Para Strings em variáveis, uso sempre aspas duplas, a menos que seja char.

```Python
name: str = "Gabriel"
surname: str = "Cavalcanti"
complete_name: str = "Gabriel Cavalcanti"
example_char: str = 'h'
```

Para Strings em uma lista, tuplas ou dicionários, use aspas simples.

```Python
geometric_forms: list[str] = ['triangle', 'square', 'hexagon']
vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
```

Para f strigas, uso aspas simples.

```Python
name: str = "Alice"
age: int = 25

print(f'Olá, meu nome é {name} e eu tenho {age} anos.')

```
Caso dentro de uma string tenha a necessidade do uso de aspas, use aspas dupas para a string e aspas simples dentro dela.

```Python
long_string = "Uso das 'aspas simples' dentro de uma string"
```

Se dentro de uma f string tenha o uso de aspas, use aspas duplas.

```Python
long_string = "Uso das 'aspas simples' dentro de uma string"

print(f'Olá, meu nome é "{name}" e eu tenho {age} anos.')

```

Caso a string seja muito longa e não quisermos usar o \n, use três aspas duplas, assim como nas docstrings.

```python
texto_longo: str = """No mundo da programação, escrever código limpo e eficiente é essencial. 
O Python, conhecido por sua legibilidade e simplicidade, permite que os desenvolvedores 
criem aplicações poderosas com menos linhas de código. Seja para desenvolver uma aplicação web, 
automatizar tarefas ou analisar dados, o Python oferece uma ampla variedade de bibliotecas e 
frameworks para ajudar você a alcançar seus objetivos de forma eficiente."""
```



## 8 - Padrões para programação orientada a objetos
