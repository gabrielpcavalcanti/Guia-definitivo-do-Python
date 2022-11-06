# Funções dir( ) e help( )

São funções para te auxiliar durante a escrita do código. Eles tem o objetivo de mostrar
os métodos, as funções, a documetação disponivel para determinado objeto.

Normalmente eles eles não ficam no código final, pois são para a consuta de determinada
função interna do Python ou não.

A função dir( ) mostra todos os métodos e atributos de determinado objeto. Basta colocar o objeto dentro dos parentêses para funcionar.

Obs: Se não souber o que é método ou atributo, veremos na parte de orientação ao objeto. Mas sá para desencargo de conciência, métodos é outro nome para função.

```python
dir(5)
```

```python
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

```python
dir("oi")
```

```python
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Perceba que ele listou todos os métodos possíveis para determinado objeto, no caso foi números inteiros e Strings, respectivamente.

Agora se quisermos saber para que serve determinado método, utilizamos a função help( ). Ela mostrará a documentação do método.

```python
help(max)
```

```python
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.

None
```

```python
help("oi".upper)
```

```python
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

None
```

Obs: Caso não esteja usando o terminal é necessário colocar a função print( ). print(help("oi".upper)), por exemplo, para poder aparecer na tela a informação do método.

No primeiro caso, o help mostra a documetação de uma função inteira, todos os argumentos
possíveis; No segundo caso, ele mostra o que o método upper faz com a String, ou seja,
transforma todas as letras em maiúsculo.

Tanto o dir( ) quanto o help( ) são funções internas do Python. Se preferir não utilizar elas durante a escrita do código, como alternativa, acesse a documentação oficial do Python para entender melhor sobre determinado objeto ou pesquise na internet.

Obs: Podemos utilizar a função help( ) para qualquer outra função do Python, inclusive o própio help ou uma função criada pelo usuário. Sempre utlize essa função ou leia a documentação, caso haja dúvida.
