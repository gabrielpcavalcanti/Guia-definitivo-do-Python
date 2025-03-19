# Rebase 

“Rebase vs Merge” é um dos tópicos mais debatidos no mundo do Git. Muitas das discussões que você verá on-line se resumem ao fato de que muitos desenvolvedores (sim, até mesmo profissionais) não entendem o propósito do rebase e o usam incorretamente, causando uma série de estragos no Git, e depois culpam o comando rebase.

Para usar o rebase para trazer as alterações do ramo principal para um ramo atual (vamos supor que estamos em um ramo chamado jdsl), executaríamos isso enquanto estivéssemos no ramo jdsl:

```
git rebase main
```

Ele fará o seguinte:

1 - Fazer o checkout do commit mais recente do main em um local temporário.

2 - Repetir cada commit do jdsl, um de cada vez, nesse local temporário.

3 - Atualizar o ramo do jdsl para apontar para o último commit repetido no local temporário, tornando-o o novo jdsl permanente.

4 - O rebase não afeta o ramo principal; o jdsl agora inclui todas as alterações do principal.

## Quando usar o Rabese e quando usar o Merge

O git rebase e o git merge são ferramentas diferentes.

Uma vantagem do Marge  é que ela preserva o verdadeiro histórico do projeto. Ele mostra quando as ramificações foram mescladas e onde. Uma desvantagem é que ele pode criar muitos merge commits, o que pode tornar o histórico mais difícil de ler e entender.

Um histórico linear geralmente é mais fácil de ler, entender e trabalhar. Algumas equipes impõem o uso de um ou de outro em seu main branch, mas, de modo geral, você poderá fazer o que quiser com suas próprias ramificações.

Você nunca deve fazer o rebase de um public branch (como a principal) em qualquer outra. Ele foi verificado por outros desenvolvedores e, se você alterar seu histórico, causará muitos problemas para eles.

Entretanto, com sua própria ramificação, você pode fazer o rebase em outros branchs (inclusive em um public branch como a principal) quantas vezes quiser.
