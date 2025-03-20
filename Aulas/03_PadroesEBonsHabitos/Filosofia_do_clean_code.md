# Filosofia do Clean code

1- falar do que se trata
2- falar das controvercias
3- falar como será usado
...

Uma maneira que gosto de trabalhar e escrever um reascunho de código da maneira que conseguir, sem me preocupar com os concelhos do clean code. Depois que escrevi e vi que está funcionando, aplico todos os concelhos até o código ficar bem escrito.

Fazer esse processo não é uma tarefa simples e demanda prática. Siguindo os conselhos abaixo, ficara mais simples e saberá o que deve ser feito para que seu código deixe de ser um rascunho. 


## - Uso de funções

Existem certas características que toda as funções deveriam ter. No dia a dia da programação, nem sempre é fácil atingir esse ideal, na verdade pode ser bastente difícil.

Vamos ver eles aqui:

### a) Devem apenas fazer uma única tarefa

Uma função sempre deve execultar uma única tarefa. Se ela faz mais de uma coisa, ela pode ser desmembrada para tarefaz isoladas. 

Para verificar que uma função está apenas executando uma tarefa, ela so deve execultar as etapas que estão a um nível de abstração do nome declarado da função. Isso não é uma tarefa tão simples, mas tenha isso sempre em mente.

Sempre se pergunte se pode separar ela em mais partes. Se separendo elas, a tarefa atribuida some, ela já está execultando a tarefa e não precisa mais ser desmembrada. Caso contrário, desmembre.

Uma função pode fazer mais de uma coisa e, pior ainda, fazer coisas que nem sabe que está acontecendo. Isso se chama side effects. Trasnsformando as função em apenas uma tarefa, reduz muito esse problema, mas algumas vezes pode ser que não resolva. Fique atento.

Algumas vezes ocorre o contrário. Existe duas funções ou mais que fazem a mesma coisa. Isso se chama duplicatas. Elas nunca são necessária e só confundem. Remova todas até que sobre uma.

### b) Uma função tem que ser pequena

Funções muito grandes tendem a ter mais de uma tarefa, que já vimos que não é o ideal, ficam mais difícil de ler e entender. Mantendo as funções curtas evitam que isso aconteça.

Além disso, funções não devem ter neasting e muitos blocos de if/else. No máximo dois blocos de identação. 

O número máximo de linhas recomendada para uma função e de 20 linhas.

### c) Tente contar uma história com suas funções

obedeça uma hierarquia no programa, sempre coloque funções mais gerais no incício e vá descendo com funções hierequicamente abaixo delas. Isso fará sentido e aprenta como se contasse uma história no seu código, fica mais organizado e elegante.

Essa "filosofia" faz parte do que chamamos de step-down rule. Detalhando um pouco mais: A ideia principal é que o código deve ser escrito de forma que o leitor entenda primeiro os conceitos de alto nível antes de mergulhar nos detalhes de implementação.

O código deve ser estruturado de cima para baixo, seguindo uma hierarquia lógica:

Comece com funções/métodos de alto nível (métodos devem descrever o "o que" o código faz, sem muitos detalhes). Em seguida detalhe as implementações conforme o código desce (As funções chamadas no nível superior devem ser definidas logo abaixo, explicando o "como").

Por fim, cada nível responde perguntas do nível acima, ou seja, se uma função chama outra, a implementação da função chamada deve aparecer logo abaixo.

### d) Poucos argumentos nas funções

Tente ao máximo ter a menor quantidade de argumentos possíveis. Se uma função necessita de argumentos, utilize, mas não crie argumentos inúteis.

Uma forma de fazer isso é escolhendo bem o tipo de dado escolhido para que possa reduzir os argumentos. Por exemplo, ter agumentos separados podem ser unidos numa lista, caso faça sentido.


## - Uso de comentários

Nada pode ser tão útil quanto um comentário bem colocado. Nada pode bagunçar mais um módulo do que comentários dogmáticos frívolos. Nada pode ser tão prejudicial quanto um comentário velho e grosseiro que propaga mentiras e desinformação.

Uso de comentários é muitas vezes impressindível, mas na maioria dos casos significa que o código foi mal escrito e deveria ser reescrito, ou seja,

**Não comente código ruim - reescreva.**

Se ver a necessidade de escrever um comentário explicando o código que sente que está mal feit, reescreva, tente ver se consegue se expressar atraves do código.

É melhor gastar tempo tempo reescrevendo o código para torna-lo bom do que atualizar os comentários e deixar o código ruim. A maior motivação de escrever comentários é código mal escrito.

Se seguir essa "lei" a quantidade de comentários irá diminuir muito. Não irá cessar, pq comentários não são ruins por essência e são muito úteis quando utilizado corretamente.

## Não os elimine totalmente  

Existem situações que é imprencidível o uso de comentários. não tenha medo de utiliza-los, na verdade, é recomendado. 

### a) Se for obrigatório, escreva

Se tem alguma questão legal envolvida, como copyright e declarações de autoria é preciso escreve-los, não tem o que fazer. 

### b) Informado algo pontual

Caso veja necessidade de escrever um comentário que descreve algo que um objeto faz, é bem-vindo. 

### c) Explicação de intenção

Às vezes, um comentário vai além de apenas informações úteis sobre a implementação e fornece a intenção por trás de uma decisão.

### d) Esclarecimento de algo

Algumas vezes o nome de funções e métodos da própria linguagem não são claros e nesses casos você não pode mudar, então colocar um comentário esclarecendo o que a função faz é bem-vindo. 

### e) Avisando de consequências

Pode ocorrer que procesimento demore muito tempo ou não está completo e caso rode o programa, dará problemas. Comentários avisando questões como essas são válidos.

## Comentários que nunca devem ser feitos

### a) Escritos com pressa

Imagine uma situação em que você está com pressa para terminal algo e deixa um comentário avisando o que se deve fazer, caso esqueça, mas esse comentário fica mal escrito e pode ser que você mesmo não entenda o que escreveu, imagina outra pessoa. 

Quando for escrever um comentário, escreva-o bem. Se for para ser ruim, não escreva.

### b) Redudantes

Igual ao significado da palavra, é excessivo, supérfluo. Não existe a necessidade. Por exemplo, escrever o que um comando básico faz (vc deve saber a sintaxe da linguagem utilizada) ou escrever para cada comando um comentários (cada linha de códico tem um comentário, não faça isso).

### c) Gera desinformação

Muitas vezes comentários não são atualizados para versões mais recentes dos códigos, tornado-se errados de diversas maneiras, como falar dizer algo que não acontece ou fazer o contrário do que está dizendo. Comentários inacurados causam muito mais dado do que se não tivesse nehum comentário.

### d) Ruidosos

Comentátios que não trazem nada de novo, dizem o óbvio, mostram a frustação de um desenvolvedor, falam nada etc

### e) Marcadores de posição

Às vezes, os programadores gostam de marcar uma posição específica em um arquivo de origem. Eles são uma bagunça que e devem ser eliminadas.

### f) comentário de comandos

É comum de testarmos vários maneiras para resolver um programa e para não ter que abrir vários arquivos, comentamos comandos que não queremos testar. Isso facilita o processo de teste do código.

Isso só funciona quando for um rascunho de código. Quando resolver qual a melhor forma de resolver o problema, elimie os códigos que testou antes, não os deixe lá de decoração. 

### g) comentários não locais **talvez coloque nos padrões**

Comentários devem explicar o que está acontecendo no local onde ele está escrito, e não em outro escopo. 

### h) Detalhosos

Comentários com muito detalhes e muitas linhas são inuteis. Provavelmente tem uma forma de reduzir o tamanho e muitas vezes ninguém irá ler ou mesmo entender.

