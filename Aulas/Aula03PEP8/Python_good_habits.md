# Python Good Habits

No Python e em qualquer linugagem de programação, existem boas regras de conduta a serem usadas e maneiras mais adequadas de escrever o código, tornado-o mais claro a todos. 

Você não precisa seguir essas recomendações, mas será bom aprende-las desde o início. Ficará natural e fácil com o aprender da programação. 

O PEP8 é um guia de stilo. O que vou fazer aqui é mostrar a melhor forma de escrever um certo conceito da programação no python. Mas assim como na obsarvação feita no arquivo do PEP8, se não enteder algum conceito, não fique assustado. Todas os termos e a sintaxe serão vistas posteriormente.

Durante a explicação de cada tópico nas aulas, eu ireir enfatizar as formas aqui mostrarei aqui, mas como lá terá muito mais conteúdo, aqui fica um arquivo só com o essencial de cada bom hábito e não a explicação do que significa cada assunto. 

## #1 - Strings

Quando for cocatenar strings, sempre use as f-Strings. É possível usar o fomart( ) e +, mas o melhor jeito são as f-Strings.

```python
num_1 = 10
num_2 = 15
nome = 'Gabriel'

# Format()

string_01 = "Eu tenho {} reais e {} dolares e meu nome é {}.".format(num_1, num_2, nome)

# +

string_02 = "Eu tenho " + str(num_1) + " reais " "e " + str(num_2) +  " dolares e meu nome é " + nome+ "."

# f-Strings

print(f"Eu tenho {num_1} reais e {num_2} dolares e meu nome é {nome}.")

```

## #2 - Abertura e fechamento de arquivos

É possível abir um arquivo, modificar ele e depois fecha-lo. Um problema pode surgir caso um arquivo seja aberto e algo aconteça na modificação, fazendo o arquivo nunca fechar. 

Para evitar isso, sempre utilize o with statement. Ele fechara o arquivo de qualquer forma, mesmo que haja uma exceção. 

```python

def open_close(arquivo):

    file = open(arquivo, 'w')
    file.write("Oi\n")
    file.close()

```

Não use a forma de cima, use a de baixo, com o with statement.

```python

def open_close(arquivo):

    with open(arquivo) as file:

        file.write("Oi\n")

```

## #3 - Sempre defina o nome da exceção

Quando estiver tratando erros, sempre especifique os erros nas excessões.

```python

try:
    num = int(input("Digite um número: "))
    num2 = num + num3
    
except ValueError  as erro:
    print(f"O tipo de erro foi: {erro}")

except NameError as erro2:
    print(f"O tipo de erro foi: {erro2}")

```

## #4 - 