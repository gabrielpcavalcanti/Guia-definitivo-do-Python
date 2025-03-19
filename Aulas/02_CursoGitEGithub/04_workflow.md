# Workflow

Usar o controle de versão sem um fluxo de trabalho adequado é como construir uma cidade sem semáforos; sem o gerenciamento adequado, tudo se tornará um caos.

Por exemplo, digamos que você esteja trabalhando em um grande projeto e editando um arquivo. Outro desenvolvedor também começa a editar um arquivo. Ambos enviam o arquivo para o VCS ao mesmo tempo. Agora há um conflito! Como o conflito deve ser resolvido? Um bom fluxo de trabalho terá um processo para resolver conflitos.

Outro exemplo é quando um novo desenvolvedor júnior se junta à sua equipe. Se o código do projeto for usado em um sistema crítico, é arriscado permitir que ele envie alterações de código diretamente. Para resolver isso, muitos desenvolvedores usam um sistema de revisão por pares em que outro desenvolvedor deve revisar o código antes que ele possa ser incorporado.

Os fluxos de trabalho são essenciais para garantir que o código seja gerenciado corretamente e reduzir a ocorrência de erros. Projetos diferentes terão fluxos de trabalho diferentes. Neste curso, você aprenderá alguns fluxos de trabalho comuns usando o sistema de controle de versão Git.

Vamas aplicar o worflow inical seguindo os passos adiante. Nas próximas aulas tratarei de temas mais complexos. 

## 1 - Instalando o git

Podemos usar o Git em qualquer sistema operacional, vou mostrar como instalar no windows.

Antes de instalar o Git, verifique se ele já não está instalado. Para isso, digite o comando no terminal:

```
git --version
```

Se já estiver, vá para o próximo passo, caso não esteja, digite:

```
sudo apt install git-all
```

Ou entre no site https://gitforwindows.org/ e faça o download.

## 2 - Criando um repositório

O primeiro passo caso queira começar um projeto é escolher onde ele estará salvo no seu computador. Escolhendo isso, temos que transformar ele em um repositório utilizando o git.

caso não saiba, um repositório é basicamente um diretório que contém um projeto (outros diretórios e arquivos). A única diferença é que ele também contém um diretório .git oculto. Esse diretório oculto é onde o Git armazena todas as informações internas de rastreamento e controle de versão do projeto.

Para transformar a pasta do projeto num repositório, use o comando:

```
git init
```

Ele criará o diretório .git oculto.

## 3 - Verificando o stats do repositório

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

## 4 - Preparação para o commit (Staging)

Esse comando serve para adicionar os arquivos que serão incluidos no próximo commit.

Sem a preparação, todos os arquivos do repositório seriam incluídos em toddos os commits 

O comando para o staging é:

```
git add <nome do arquivo>
```

## 5 - Fazendo um commit 

Um commit é uma "foto" instantânea do repositório em um determinado momento. É uma forma de salvar o estado do repositório e é como o Git mantém o controle das alterações no projeto. Um commit vem com uma mensagem que descreve as alterações feitas no commit.

Quando todas os arquivos estiver selecionados, use o comando:

```
git commit -m "mensagem do commit"
```
 
---

Metade do seu fluxo de trabalho como desenvolvedor será composto apenas por três comandos simples:

- git status
- git add
- git commit

É a maior parte do que você precisa para trabalhar efetivamente como desenvolvedor individual. Outros 40% do Git se referem à colaboração e ao armazenamento do seu trabalho em um servidor remoto.

Os últimos 10% referem-se principalmente à correção de erros, reversão de alterações e outros tópicos avançados. Não se preocupe, também abordaremos esses tópicos.

---

Antes de entrar nesses assuntos (que estarão em outro arquivo), vamos falar de outro comandos.

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
got --no-pager log -n <10>
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
