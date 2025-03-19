# Branch

Esse é o primeiro conceito mais complexo do controle de versão. Quando utilizamos o comanfo git status, além de outras informações ele nos fornece o branch atual. Ele permite que você acompanhe as diferentes alterações separadamente. 

Por exemplo, digamos que você tenha um grande projeto da Web e queira experimentar a alteração do esquema de cores. Em vez de alterar diretamente o projeto inteiro (no momento, the main branch), você pode criar um novo branch chamada color_scheme e trabalhar nele. Quando terminar, se gostar das alterações, você poderá fazer um merge (conceito visto depois) com o branch color_scheme de volta ao branch principal para manter as alterações. Se não gostar das alterações, você pode simplesmente excluir o branch color_scheme e voltar para o branch principal.

Um Branch é apenas um ponteiro nomeado para um commit específico. Quando você cria um branch, está criando um novo ponteiro para um commit específico. O commit para o qual o branch aponta é chamado de ponta do branch. Como um Branch é apenas um ponteiro para um commit, elas são leves e “baratas” em termos de recursos para serem criadas. Quando você cria 10 ramificações, não está criando 10 cópias do seu projeto no disco rígido.

## Verificando o Branch atual

Apenas digite o comando

```
git branch
```

## Renomeano um Branch

Lembrando que esse comando só renomea, mas não define ele como o padrão.

```
git branch -m oldname newname
```

## Criando um novo Branch

Existem duas formas de criar um branch, a primeira apenas cria, mas não muda automaticamente e a segunda, crie e muda. Sempre prefira pela segunda opção.

```
git branch <meu_novo_branch>
```

```
git git switch -c <meu_novo_branch>
```

O sinalizador -c diz ao Git para criar um novo ramo se ele ainda não existir.

Quando você cria um novo branch ele usa o commit atual em que você está como base do ramo. Por exemplo, se você estiver no branch principal com 3 commits, A, B e C, e depois executar git switch -c my_new_branch, o novo branch "carregará" os três commits.

Mas commit novos pertencerão apenas ao novo Branch.

Uma forma mais antiga, mas que pode funcionar é utilizando o comando:

```
git checkout -b <meu_novo_branch>
```

Ele também troca automaticamente os branchs.

## Mudando de branch

Para mudar de branch, use o comando:

```
git switch <nome_branch>
```  

ou

```
git checkout <nome_branch>
```
