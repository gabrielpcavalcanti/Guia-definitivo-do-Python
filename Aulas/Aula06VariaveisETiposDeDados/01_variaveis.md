# Variáveis

Em aulas anteriores vimos o uso de variáveis em elguns exemplos. Naquele momento não era
necessário saber com detalhes o que são variáveis, agora sim, já que elas nos abrem uma
nova porta de oportunidades e serão sempre utilizadas, sempre mesmo.

Na programação, variável é um elemento que possui um nome, tipo e valor. Ela pode variar
durante a execução do programa (daí o nome) e possui uma posição de memória.

Podemos colocar basicamento tudo que que quisermos dentro de uma variável. Podemos colocar valores, funções, classes, operações, resultados, coleções, e usar essas variáveis para fazer outras operações com outras variáveis. As possibilidades são inúmeras.

### Nome

Os nomes das variáveis no Python possuem algumas regras a seram seguidas. Abaixo estão o que não se deve colocar, todo o resto é premitido:

* Palavras reservadas como print, max, int(), lower, etc.

* Números no início: 5numero, 35renda, etc.

* Alguns caracteres: ^, &, *, @, !, ., ;, <, >, +, -, etc. O único permitodo é o _ .

* Espaço: As variáveis não podem ter espaços, utilize o _ .

Obs: Podemos utilizar letras maiúsculas, não é recomendado fazer isso e não segue a PEP8. Coloque sempre letras minúsculas e se for uma palavra composta, separe com _ .

Dica: Sempre utilizar nomes de variáveis que façam sentido, ou seja, não utilise a, b, r, etc. Use, por exemplo, numero, caixa, tamanho, altura. Nomes que indicam coisas na vida real.

### Tipo

O Python possui quatro tipos principais, int, float, Strings e Booleanos.

O tipo int ingloba todos os números inteiros; O tipo float, todos os números reais; O tipo
String, armazena qualquer tipo de texto; Por fim, o tipo boolean que armazena os valores lógicos True ou False.

Podemos utilizar as variáveis para armazenar valores que estão dentro de desses quatro citados acima.

Veremos em outra aulas, com detalhe, cada um dos tipos da linhuagem Python.

```python
tamanho = 4

numero = 5.6

num_1, num_2 = 4.5, 34 # Aqui, num_1 recebe 4.5 e num_2 recebe 34.

frase = "Isso é uma String"

temperatura = (4 * 4) + 2

so_mais_um_exemplo = (tamanho * numero) - temperatura

e_verdade = True

palavra = input("Digite uma palavra: ")

maximo = max()

```

### Valor

O valor de uma variável é o tipo que ela assume num determinado momento. As variáveis podemo mudar de tipo durante o código. O nome desse processo é chamado de Cast.

O cast é feito colocando o valor que queremos transformar dentro de funções, são elas:

* int() -> Transforma em inteiro.
* float() -> Transforma em float
* str() -> transforma em String
* list() -> transforma em lista

Lembrando que nem sempre é possível transformar um valor em outro. Uma String não pode virar um número a menos que o texto seja um número.

```python
numero_real = 4.5
numero_inteiro = int(numero_real)

numero_inteiro_2 = 3
nimero_real_2 = float(numero_inteiro_2)

um_numero_de_uma_string = int("45")

print(numero_inteiro)
print(numero_real_2)
print(um_numero_de_uma_string)

```

```python
4
3.0
45
```

No Python não existe a ideia de costante. Em outras linguagens de programação, podemos declarar uma constante, já no Python não é possível. Para indicar que o valor é uma constante, o nome dela é toda em maiúsculo.

Ainda podemos mudar o valor da 'constante'. As letras em maiúsculo indicam, mas não impedem as mudanças de valor ou tipo.

```python
PI = 3.14159265358979
CPF = "123.456.789 - OO"
```

### Escopo de variáeis

É um espaço dentro do código que a váriável está ativa e o interpredor do Python reconhce. Há dois escopos na linguagem Python:
Global e local. 

No escopo global a váriavel pode ser utilizada em todo o programa,
no local, apenas quando for inicializada ou estiver dentro de um bloco de comando. 

Calma, vamos ver como funciona cada um. Se ainda não entender o que é um bloco de comando, veremos mais a frente.

``` Python
# Essa variável está no escopo global
variavel_1 = 5

# Pode ser utilizado tanto fora quanto dentro de um bloco de comando.

conta = variavel_1 + 5

if variavel_1 > 4:
    print("Oi, tudo bem?")
    conta2 = variavel_1 + 2 # Variavel no escopo local. Só funciona se o bloco de comando for ativado. Como variavel_1 é maior que 5, a estrutura condicional irá funcionar.

```

``` Python
Oi, tudo bem?
```

### Lembrete

A partir desse ponto já é legal começar a fazer alguns programas simples na linguagem para
fixar os conceitos e apreder a sintaxe do código.

Se já estiver fazendo isso, parabéns. Caso não, é bom começar.

Segue abaixo alguns exemplos de programas que utilizam todo conheceimento já adquirido, que
são: funções print( ) e input ( ), operadores, funções dir( ) e help( ) e variáveis.

Para ter acesso a uma gama bem maior de exercícios, veja meu outro [repositório](https://github.com/Gabriel-Cavalcanti/Exercicios) no GitHub.
