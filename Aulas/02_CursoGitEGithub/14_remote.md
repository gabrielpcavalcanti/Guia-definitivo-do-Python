# Remote

Podemos ter “remotes”, que são apenas repositórios externos com quase o mesmo histórico do Git que o nosso repositório local.

Remoto refere-se a qualquer outro repositório remoto para o qual os desenvolvedores podem enviar alterações. Pode ser um repositório centralizado, como o fornecido pelo hub do Git, ou repositórios em outros dispositivos de desenvolvedores. 

O código remoto é acessado por meio de um URI exclusivo e acessível somente àqueles que têm permissão local. Por outro lado, refere-se à sua máquina, que pode ser um laptop, um desktop ou até mesmo um dispositivo móvel, e só pode ser acessada por você para demonstrar ambos em ação.

Quando se trata do Git (a ferramenta CLI), não há realmente um repositório “central”. O GitHub é apenas o repositório de outra pessoa. Somente por convenção e conveniência é que nós, como desenvolvedores, começamos a usar o GitHub como uma “fonte de verdade” para o nosso código.

No git, outro repositório é chamado de “remote”. A convenção padrão é que, quando você estiver tratando o remoto como a “fonte autorizada da verdade” (como o GitHub), você o chamará de “origin”.

Por “fonte autorizada da verdade” queremos dizer que é aquela que você e sua equipe tratam como o repositório “verdadeiro”. É aquele que contém a versão mais atualizada do código aceito. 

## Criar um repoitório remoto

```
git remote add <name> <uri>
```

---
