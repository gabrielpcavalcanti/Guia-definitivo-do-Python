# git status e git log

Sempre é bom ver qual é a situação atual do seu repositório, mostrar quais commits, mudanças e branches você está agora.

Para isso, use o comando:

```
git status
```

Um arquivo pode estar em um dos vários estados em um repositório Git. Aqui estão alguns estados importantes:

untracked: Não está sendo rastreado pelo Git
staged: Marcado para inclusão no próximo commit
committed: Salvo no histórico do repositório.

O git status també nos informa isso.

## git log

Um repositório Git é uma lista (potencialmente muito longa) de commits, em que cada commit representa o estado completo do repositório em um determinado momento.

O comando git log mostra um histórico dos commits em um repositório. Isso é o que torna o Git um sistema de controle de versão. Você pode ver:

Quem fez um commit
Quando o commit foi feito
O que foi alterado
Um hash de commit
Cada commit tem um identificador exclusivo chamado "hash de commit". Trata-se de uma longa sequência de caracteres que identifica o commit de forma exclusiva. Aqui está um exemplo do meu:

5ba786fcc93e8092831c01e71444b9baa2228a4f

Por conveniência, você pode se referir a qualquer commit ou alteração no Git usando os primeiros 7 caracteres de seu hash. No meu caso, é 5ba786f.

para acessar o histórico, utilize o comando

```
git log
```

Se quiser ter algumas opções a mais, 

```
git --no-pager log -n <10>
```

É possível também ver o conteúdo de um commit sem a necessidade de mexer diretamente nos arquivos de objeto. utilizado o comando:

```
git cat-file -p <hash> 
```

Há alguns sinalizadores que gosto de usar de vez em quando para facilitar a leitura do resultado.

A primeira é --decorate. Pode ser uma das seguintes opções:

- short (o padrão)
- full (mostra o nome completo da referência)
- no (sem decoração)
- oneline (visão mais compacta do log)

```
git log --oneline
```

Um comando poderoso para verificar os branchs e merges:

```
git log --oneline --decorate --graph --parents
```




### Alguns termos que é preciso saber:

- tree: git's way of storing a directory
- blob: git's way of storing a file

Eles irão aparecer no decorrer do curso

---
