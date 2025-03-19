# Merge

Qual é o objetivo de ter vários branchs?", você pode se perguntar. Na maioria das vezes, elas são usadas para fazer alterações com segurança sem afetar o seu branch principal (ou o da sua equipe). No entanto, quando estiver satisfeito com suas alterações, você deverá mesclá-las (merge) de volta ao branch principal para que elas sejam incorporadas ao produto final.

Em outros termos, o branch principal não tem nenhuma indicação ou conhecimento de nenhuma dessas alterações dos outros branchs, mesmo quando um push (veremos depois) acontece. Isso se da no fato que o main branch existe isoladamente. O novo branch precisa ser mesclado de volta ao branch principal para reconhecer as alterações no novo branch.

O Merge é uma especie de commmit. Se você mesclar os outros branchs no main, o Git combinará os dois ramos criando um novo commit que tenha os dois históricos dos pais.

Em resumo, Um Merge commit é o resultado da mesclagem de dois Branchs.

## Fazendo um merge

Temos que estar no main branch para que funcione.

```
git merge <nome do branch que será mesclado com o main branch>
```

Esse tipo de Merge. Ele é chamado de fast-forward merge. 

A mesclagem irá:

1 - Encontrar o commit da "merge base" ou o "melhor ancestral comum" das duas ramificações. 

2 - Reproduz as alterações do main, a partir do melhor ancestral comum, em um novo commit.

3 - Reproduz as alterações do vimchadsonly no main, começando pelo melhor ancestral comum.

4 - Registra o resultado como um novo commit



