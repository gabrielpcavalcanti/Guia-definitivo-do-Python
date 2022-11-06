# Função input( )

Continuamos com o nosso estudo na programação. Após ver a primeira função, print( ), estamos
aptos para seguir em frente. A próxima função que iremos ver é a input( ), onde possibilita
a entrada de dados pelo usuário.

É uma das funções mais utilizadas no Python. O objetivo dela é permitir que o usuário escreve algo no teclado e apareça na tela ou armazena numa variável. Essa função aumenta o nosso leque de possíbilidades dentro da programação.

Obs: Veremos o que é variável em outra aula.

Obs: Não é necessário escrever algo dentro o input( ). Colocamos um texto para o usuário saber o que deve ser digitado. Isso evita erros e confunsões.

```python
input("Digite algo no teclado: ")

palavra = input("Digite uma palavra: ") # Não irá aparecer nada na tela pois armazenamos numa variável. Se declararmos a variável, irá sim aparecer o que o usuário escreveu.

```

Podemos ter a saida que quiser, mas todas serão Strings. A menos que especifiquemos o tipo de variável. Isso é chamado se cast, ou seja, transformar um tipo em outro. Lembre: nem sempre é possível fazer isso.

```python
int(input("Digite algo: "))
float(input("Digite algo: "))
str(input("Digite algo: "))
```

Obs: tipo de dados e variáveis serão vistos com maior detalhe em outra aula.
