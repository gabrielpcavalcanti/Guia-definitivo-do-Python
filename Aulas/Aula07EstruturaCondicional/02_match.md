# Match

É um tipo de estrutura condicional idêntica ao Switch, que existe em outras linguagens de programação como C e no Java. Aqui no Python é chamada
de Match. 

Funciona da seguinte forma, vc tem uma variável que pode receber diversos valores e quer ver o que acontece caso o valor seja igual a um ou 
igual a outro, por meio de casos.

```Python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

No programa acima, a variável name pode recebe um nome e esse nome está em três diferentes casos, exemplificado pela palavra reservada case. Perceba que funciona com a mesma lógica do if else, somente outra forma de escrever, aumentar o repertório.
