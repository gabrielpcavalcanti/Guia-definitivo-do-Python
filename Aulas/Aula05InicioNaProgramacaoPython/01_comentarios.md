# Comentários

Todos os princípios utilizados para escrever comentários estão no arquivo filosofia_do_Clean_code.md da pasta 03_Padrões_e_bons_habitos. 

O que pretendo com essa aula é mostrar a "sintaxe" do comentário no Python e como eles funcionam.

Comentários no python podem ser feitos de duas formas:

* A primeira é utilizando #. Esse tipo de comentário é de apenas uma linha. Se quisermos ter um comentário numa linha abaixo, é preciso utilizar outra #;

* O segundo tipo e utilizando três aspas dupas """ e fechando com mais três aspas duplas """ ou três aspas simples no começo e no final. Nesse caso, tudo que estiver dentro das aspas. será um comentário, ou seja, não será lido pelo interpretador.



```python
# Esse é um comentário de uma única linha. Ele não será lido pelo interpretador.

"""
Esse é um comentário de varias linhas.
Tudo que estiver dentro das aspas, será um comentário

"""

'''
Essa é outra forma de fazer comentários de várias linhas
Não é uma forma usual de fazer isso, mas é possível.

'''

```

Utiliza-se o segundo tipo de comentário para explicar funções. Chamamos nesse caso de docStrings (documentação da função).

Os comentário não serão lidos pelo interpretador do Python. Eles estão lá para explicar o código e somente isso.

---
