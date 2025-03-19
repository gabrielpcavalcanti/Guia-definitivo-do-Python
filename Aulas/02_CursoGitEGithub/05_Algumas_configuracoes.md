# Algumas configurações do git

Antes de entrar em tópicos mais complexos é bom saber algumas configurações que você pode fazer no Git.

## Ver todas as configurações do repositório

```
git config --list --local
```

## Ver uma configuração em específico

```
git config --get <vonfiguracao>
```

## Nome e e-mail

Verificar nome:

```
git config --get user.name
```

Verificar e-mail: 

```
git config --get user.email
```

Definir nome e e-mail:

```
git config --add --global user.name <"github_username_here">
git config --add --global user.email <"email@example.com">
```

## Branchs

Definir o branch padrão:

```
git config --global init.defaultBranch <master>
```

Ainda veremos o que é branch.

Obs: O branch padrão do Git é **master** e do GitHub é **main**.

E para Renomear um Branch

```
git branch -m oldname newname
```

## Duplicadas

Normalmente, em um armazenamento de chave/valor, como um dicionário Python, não é permitido ter chaves duplicadas. Por mais estranho que pareça, o Git não se importa.

```
git config --unset-all <example.key>
```
O sinalizador --unset-all é útil se você realmente quiser eliminar todas as instâncias de uma chave da sua configuração. Por outro lado, o sinalizador --unset só funciona com uma única instância de uma chave.

## Remove a Section

```
git config --remove-section <section>
```

O sinalizador --remove-section é usado para remover uma seção inteira da sua configuração do Git. 

---
