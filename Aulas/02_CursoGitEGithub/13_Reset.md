# Reset

Um dos principais benefícios de usar o Git é a capacidade de desfazer alterações. Há muitas maneiras diferentes de fazer isso, mas, primeiro, começaremos voltando ao histórico de commits sem descartar as alterações.

Há duas maneira de fazer um reset: de forma "soft"e "hard".

## Git Reset Soft

O comando git reset pode ser usado para desfazer o(s) último(s) commit(s) ou quaisquer alterações no índice (alterações preparadas, mas não confirmadas) e na árvore de trabalho (alterações não preparadas e não confirmadas).

```
git reset --soft <COMMITHASH>
```

A opção --soft é útil se você quiser apenas voltar a um commit anterior, mas manter todas as suas alterações. As alterações confirmadas serão não confirmadas e preparadas, enquanto as alterações não confirmadas permanecerão preparadas ou não preparadas como antes.

COMMITHASH pode ser encontrado no git log. 

## Git Reset Hard

```
git reset --hard <COMMITHASH>
```

Isso é útil se você quiser apenas voltar a um commit anterior e descartar todas as alterações.

Isso redefinirá seu diretório de trabalho e o índice para o estado desse commit, e todas as alterações feitas após esse commit serão perdidas para sempre.

## Tenha bastente CUIDADO

Quero enfatizar o quanto esse comando pode ser perigoso. Se você simplesmente excluísse um arquivo confirmado, seria trivialmente fácil recuperá-lo porque ele é rastreado no Git. Entretanto, se você usasse o git reset --hard para desfazer o commit desse arquivo, ele seria excluído para sempre.

Se quiser redefinir para um commit específico, você pode usar o comando git reset --hard e fornecer um hash de commit.

---
