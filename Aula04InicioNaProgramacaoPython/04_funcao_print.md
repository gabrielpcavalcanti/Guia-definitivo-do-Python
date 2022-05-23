# Função print( )

Acabamos de quebrar a maldição, trazendo sorte para a nossa jornada e apredendemos nosso
primeiro comando em Phython, a função interna print( ).

Por incrível que pareça a função print( ) apresenta diversas pequenas configurações que
podem ser feitas e passam despercebidos da maioria dos programadores.

Se utilizarmos a função interna help( ), podemos ver o que função print( ) faz.

```python
print(help(print))
```

```python
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

None
```

Podemos ver no código que temos alguns parâmetros opcionais dentro da função print( ) (toda vez que tiver um nome seguido de = dentro de uma função, esse parâmetro é opcional).

Os dois mais importantes são o sep e o end. O primeiro é a separação, por meio do espaço,
dos valores dentro de String; O segundo faz com que toda vez que termine de imprimir, o
cursos será mandado para a linha abaixo.

ps: Caso não saiba o que é String, calma, veremos em outra aula.

Se quisermos mudar o padrão do parâmetro é só especificar ele dentro da função e colocar
o que quisermos (desde que seja possível). Por exemplo: podemos utilizar o separador como sendo - ou # ou %, mas não podemos mudar o tipo, como colocar True.

Dica: Sempre brinque com os parâmetetros das funções. Quando mais você testa, mais você aprende.

### Parâmetro sep

```python
print("oi,", "tudo bem", sep='-')
```

```python
oi-tudo bem
```

### Parâmetro end

```python
print("oi,", end=' ')
print("tudo bem")
```

```python
oi, tudo bem
```

Obs: Se abrir o interpretador do python, não é necessário utilizar a função print() para mostrar algo na tela. Mas se estiver escrevendo um script e executar ele, se torna necessário a utilização da função.