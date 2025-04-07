# GitHub

Aqui estão listados os principais comandos do GitHub. É possível fazer pelo terminal de comando, mas utilizar a interface é mais simple. Escolha a maneira que preferir. 

Lembre que é preciso criar um conta no GitHub e é preciso tricar o nome do Branch principal de master para main.

## Criando um repositório local

```
git remote add origin <URL>
```

## Git push

O comando git push empurra (envia) alterações locais para qualquer “remoto” - no nosso caso, o GitHub. Por exemplo, para enviar os commits do nosso ramo principal local para o ramo principal da origem remota, executaríamos:

Utilizando https, serão solicitadas minhas informações de login. Depois que essa ação for concluída, o GitHub reconhecerá que um novo branch foi adicionado. Em seguida, ele solicitará que eu crie uma solicitação de pesquisa que possa ser comparada com outro branch, neste caso, o branch principal. Lembre, é preciso criar uma conta no GitHub para que o processo funcione.

```
git push -u origin main
```

Outras formas

```
git push -u origin <localbranch>:<remotebranch>
```

Você também pode excluir um ramo remoto enviando um ramo vazio para ele:

```
git push -u origin :<remotebranch>
```

É sempre uma boa prática verificar em qual branch você está atualmente. Você pode usar git status ou git branch para fazer isso. Isso é importante porque, se você fizer alterações em um branch diferente, precisará especificar para onde está enviando.

Ele pegou os snapshots de commit que tenho no meu repositório local e os enviou para o repositório remoto. O Git então comparou esses arquivos com o que está no repositório remoto para encontrar quaisquer conflitos ou problemas. Se nenhum for encontrado, ele apenas os mesclará diretamente, o que é classificado como uma mesclagem automática. Se houver algum conflito, meu push falhará.

Antes de fazer um push, também é uma boa prática executar um git pull para obter as últimas alterações do repositório remoto e reduzir as chances de encontrar um conflito. Como tenho apenas um único arquivo e este será um novo repositório, não terei nenhum conflito ou problema.

## Git pull

o comando pull para obter as alterações mais recentes.

Normalmente, quando você está trabalhando em um projeto, você pode ter vários desenvolvedores enviando com diferentes branches, códigos diferentes e recursos diferentes. Para obter essas alterações, você precisa usar o comando git pull.

preciso executar o comando git pull. Isso obterá as últimas alterações do repositório remoto. Se alguma nova alteração for adicionada, ela será refletida na saída do shell.

Eu executo o comando e, neste caso, o Git me diz que um arquivo foi alterado com uma inserção. 

Com o git pull, você está pegando todos esses dados do servidor remoto. O Git então mescla o snapshot do remoto com o snapshot que está no seu local. Ele os mesclará automaticamente se não houver conflitos.

Execultar o Fetching é bom, mas, na maioria das vezes, queremos as alterações reais do arquivo em um repositório remoto, não apenas os metadados.

```
git pull [<remote>/<branch>]
```

A sintaxe [...] significa que o remote e o branch entre colchetes são opcionais. Se você executar o git pull sem nada especificado, ele extrairá o ramo atual do repositório remoto.

## Pull request

No GitHub, um pull request é uma maneira de propor alterações, normalmente para o resto da sua equipe ou para o mantenedor de um projeto para o qual você está contribuindo.

As solicitações de pull request permitem que os membros da equipe vejam quais alterações estão sendo propostas e as discutam antes de serem mescladas na base de código principal.

O objetivo de um pull request é obter uma revisão por pares das alterações feitas no branch. Em outras palavras, para validar que as alterações estão corretas ao codificar, muitas equipes terão condições em torno dos testes de unidade e testes de integração. Essas condições geralmente incluem a validação de que os padrões foram atendidos para mesclar de volta à linha principal, uma equipe também verificará se há problemas que possam ter sido perdidos.

No site do GitHub mostrará um novo branch com um prompt. Clique no botão comparar o pull request. Um pull request permite que a equipe saiba que há novas alterações e que eles revisem e que também desejo aprovar ou solicitar alterações na solicitação de pesquisa real. 

Outra coisa a ser observada na UX do GitHub é que você compara a Branch atual com o branch principal quando se faz um pull request. A equipe então revisará as mudanças e as aprovará ou recusará. Uma vez aprovadas, você pode então mesclar suas mudanças no branch principal. Isso é muito mais limpo do que todos trabalhando no branch principal.

## Git clone

Digamos que temos um projeto chamado coding project one que está localizado no Git hub com uma URL exclusiva. Em outras palavras, esse projeto é armazenado em um servidor remoto. Quando um usuário deseja copiar esse projeto para seu dispositivo local, ele precisa executar um clone se for a primeira vez ou puxá-lo para obter as últimas alterações.

Para clonar um projeto, um usuário deve primeiro escolher uma pasta em sua máquina local. O coding project one é então clonado do servidor e copiado para a pasta escolhida. O usuário pode então fazer alterações no projeto e enviá-las de volta para o servidor.

```
git clone <URL-do-repositório>
```

Também é possível usar o CLI e o SSH.

Outros usuários trabalhando na base de código não verão essas alterações em suas máquinas locais, a menos que puxem as últimas alterações do servidor. Uma das vantagens disso é que você pode trabalhar offline e, em seguida, confirmar suas alterações quando estiver pronto.

---
