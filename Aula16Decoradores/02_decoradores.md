# Decoradores

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

Vejamos um exemplo:

```Python
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()
```

```Python
Foi um prazer conhecer você!
Meu nome é Pedro
Tenha um excelente dia!
Foi um prazer conhecer você!
Quero dormir...
Tenha um excelente dia!
```

## utilizando decoration patterns

```Python
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Felicity'))

print(ordernar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())
```


## decoradores com argumento:

```Python
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))  # 22

print(soma_dez(1, 21))  # 22


print(comida_favorita('pizza', 'churrasco'))


print(comida_favorita('sanduiche', 'pizza'))
```

