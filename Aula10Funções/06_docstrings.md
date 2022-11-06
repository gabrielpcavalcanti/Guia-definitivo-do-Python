# DocStrings

É uma boa prática, mas não obrigatório, colocar a chamada DocString. Ela serve para explicar o que determidada função faz. 

Nem toda vez o nome da função explica com detalhes o que faz, ai que ela entra. Começa colocando tres " e termina com outros três  ". Pode-se usar ' também. Isso facilita a leitura do código para você e para os outros. Nem toda função necessita de DocStrings, mas é bom colocar sempre que achar importante.

DoStrings e comentários tem diferenças. As DocStrings resume o que a função faz, indica os parâmetros da função e os retornos. Os comentários dão informações pontuais de uma linha ou um conjunto pequenos de linha.

Existem vários modelos de doc-strings. Podem ser de uma linha com o da função hello_word( ) ou várias linhas. Como visto abaixo.

```python
def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """

    return argument1

# Ou

def some_functions_2(arg2):
    """
    Description of some_functions_2

    Args:
        arg2 (undefined):

    """

# ou

def some_functions_3(arg3):
     """[summary]

    Args:
        arg2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    return 'oi'
```

A doc-string é a documentação da função, então podemos acessar ela utilizando o comando **help** ou no método `__doc__`.

```python
def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """

    return argument1


print(help(some_function))
print(some_function.__doc__)

```

```Python
Help on function some_function in module __main__:

some_function(argument1)
    Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

None
Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

```
