# Filosofia do Clean code

1- falar do que se trata
2- falar das controvercias
3- falar como será usado
...

Uma maneira que gosto de trabalhar e escrever um reascunho de código da maneira que conseguir, sem me preocupar com os concelhos do clean code. Depois que escrevi e vi que está funcionando, aplico todos os concelhos até o código ficar bem escrito.

Fazer esse processo não é uma tarefa simples e demanda prática. Siguindo os conselhos abaixo, ficara mais simples e saberá o que deve ser feito para que seu código deixe de ser um rascunho. 

## Uso de nomes

Os padrões adotados no código escrito são os mostrados acima, mas todos eles estão seguindo alguns princípios descritos no clean code, mostrados abaixo.

### Say what you mean. Mean what you say.

Essa frase resume todos os princípios.

### Use nomes que revelem a intenção

Se um nome precisar de comentários, o nome não revala sua intenção e precisa ser alterado. Ele presisa mostrar porque existe, o que faz e como é utilizado.

```python
elapsed_time_in_days = 10  # Variable name
WikiPage  # Class name
post_payment  # Method name
```

### Evite desiformações

Evite nomes que dão pistas para significados diferntes ou ambiguos no código, evitando a desinformação.

Ex: Use hypotenuse instead of hp.

Não crie nomes de qualquer que seja o objeto muito pareceidos um com os outros. Será difícil diferenciar os dois.

Ex: XYZControllerForEfficientHandlingOfStrings e XYZControllerForEfficientStorageOfStrings.


### Faça distinções significativas

Não mude um nome para outro genérico por causa que já existe outro nome com o significado que você queria. Se os nomes são diferntes, eles tem que significar conceitos diferentes.

Não crie nome de objetos diferntes que já significam o mesmo de outro objeto já criado.

### Escolha claridade em vez de entreterimento

Pode ocorrer que durante um projeto, os programadores crie nome de objetos que fazem sentido no contexo interno, como piadas. É uma forma de se distrair, brincar ou até deixa easter eggs. A questão é: fora desse ambiente, o que está escrito não fará sentido.

Então sempre escolha claridade ao inves de intreterimento. 

Se quiser brincar, tudo bem, mas troque quando a brincadeira tiver perdido a graça.

### O tamanho do nome deve corresponder ao tamanho do escopo

Prefira nomes mais curtos, mas contanto que sejam claros e dê contexo. Caso não dê, use nomes mais longo. Melho um nome longo que um comentário ou doctring longa.

Permita-se criar nomes maiores se o escopo for maior, nomes menos se o escopo for melhor. Não precisa necessáriamente seguir isso (pode muito bem ter nomes curtos para escopos grandes e vice-versa).

Não tenha medo de perder tempo escolhendo um nome. Na verdade, você deve experimentar vários nomes diferentes e ler o código com cada um deles.

### Não deixe de usar palavras específicas da programação

Lembre-se de que as pessoas que leem seu código serão programadores. Então vá em frente e use termos de ciência da computação (CS), nomes de algoritmos, nomes de padrões, termos matemáticos e assim por diante.


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

### a) Não os elimine totalmente  

Existem situações que é imprencidível o uso de comentários. não tenha medo de utiliza-los, na verdade, é recomendado. 

### b) Se for obrigatório, escreva

Se tem alguma questão legal envolvida, como copyright e declarações de autoria é preciso escreve-los, não tem o que fazer. 

### c) Informado algo pontual

Caso veja necessidade de escrever um comentário que descreve algo que um objeto faz, é bem-vindo. 

### d) Explicação de intenção

Às vezes, um comentário vai além de apenas informações úteis sobre a implementação e fornece a intenção por trás de uma decisão.

### e) Esclarecimento de algo

Algumas vezes o nome de funções e métodos da própria linguagem não são claros e nesses casos você não pode mudar, então colocar um comentário esclarecendo o que a função faz é bem-vindo. 

### f) Avisando de consequências

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

## - Uso no tratamento dos erros

Sempre utilize o try-exept para identificar erros, faça teste e veja os erros que aparecem, trate esses erros, especificandos. 

Especificar demais pode ser algo ruim, tente dividir por categorias: Podemos classificá-los por suas fonte: eles vieram de um componente ou de outro? Ou seu tipo: são falhas de dispositivo, falhas de rede ou erros de programação?

O mais importante deve ser como eles são tratados: crie classes gerais e e destinha os erros ou use classes diferntes para um uma exceção específica. Veja qual serve melhor.

## Código de terceiros

Third-party code helps us get more functionality delivered in less time.
 Where do we start when we want to utilize some third-party package?
 It’s not our job to test the third-party code, but it may be in our best
 interest to write tests for the third-party code we use.
 Suppose it is not clear how to use our third-party library. We might spend
 a day or two (or more) reading the documentation and deciding how we
 are going to use it. Then we might write our code to use the third-party
 code and see whether it does what we think. We would not be surprised
 to find ourselves bogged down in long debugging sessions trying to
 figure out whether the bugs we are experiencing are in our code or theirs.
 Learning the third-party code is hard. Integrating the third-party code is
 hard too. Doing both at the same time is doubly hard. What if we took a
 different approach? Instead of experimenting and trying out the new stuff
 in our production code, we could write some tests to explore our
 understanding of the third-party code. Jim Newkirk calls such tests
 learning tests.

 The learning tests end up costing nothing. We had to learn the API
 anyway, and writing those tests was an easy and isolated way to get that
 knowledge. The learning tests were precise experiments that helped
 increase our understanding.
 Not only are learning tests free, they have a positive return on
 investment. When there are new releases of the third-party package, we
 run the learning tests to see whether there are behavioral differences.
 Learning tests verify that the third-party packages we are using work the
 way we expect them to. Once integrated, there are no guarantees that the
 third-party code will stay compatible with our needs. The original
 authors will have pressures to change their code to meet new needs of
 their own. They will fix bugs and add new capabilities. With each release
 comes new risk. If the third-party package changes in some way
 incompatible with our tests, we will find out right away.
 Whether you need the learning provided by the learning tests or not, a
 clean boundary should be supported by a set of outbound tests that
 exercise the interface the same way the production code does. Without
 these boundary tests to ease the migration, we might be tempted to stay
 with the old version longer than we should.

 Interesting things happen at boundaries. Change is one of those things.
 Good software designs accommodate change without huge investments
 and rework. When we use code that is out of our control, special care
 must be taken to protect our investment and make sure future change is
 not too costly.
 Code at the boundaries needs clear separation and tests that define
 expectations. We should avoid letting too much of our code know about
 the third-party particulars. It’s better to depend on something you control
 than on something you don’t control, lest it end up controlling you.
 We manage third-party boundaries by having very few places in the code
 that refer to them. We may wrap them as we did with Map, or we may use
 an ADAPTER to convert from our perfect interface to the provided
 interface. Either way our code speaks to us better, promotes internally
 consistent usage across the boundary, and has fewer maintenance points
 when the third-party code changes.

## Unit tests

Nowadays I would write
 a test that made sure that every nook and cranny of that code worked as I
 expected it to. I would isolate my code from the operating system rather
 than just calling the standard timing functions. I would mock out those
 timing functions so that I had absolute control over the time. I would
 schedule commands that set boolean flags, and then I would step the
 time forward, watching those flags and ensuring that they went from
 false to true just as I changed the time to the right value.
 Once I got a suite of tests to pass, I would make sure that those tests
 were convenient to run for anyone else who needed to work with the
 code. I would ensure that the tests and the code were checked in together
 into the same source package.
 Yes, we’ve come a long way; but we have farther to go. The Agile and
 TDD movements have encouraged many programmers to write
 automated unit tests, and more are joining their ranks every day. But in
 the mad rush to add testing to our discipline, many programmers have
 missed some of the more subtle, and important, points of writing good
 tests.

First Law You may not write production code until you have written a failing unit test.
 
Second Law You may not write more of a unit test than is sufficient to fail, and not compiling is failing.

Third Law You may not write more production code than is sufficient to pass the currently failing test.

The tests and the production code are written together, with the
 tests just a few seconds ahead of the production code.

If we work this
way, those tests will cover virtually all of our production code. The sheer
bulk of those tests, which can rival the size of the production code itself,
can present a daunting management problem

Keeping Tests Clean: What this team did not realize was that having dirty tests is equivalent to,
 if not worse than, having no tests. The problem is that tests must change
 as the production code evolves. The dirtier the tests, the harder they are
 to change. The more tangled the test code, the more likely it is that you
 will spend more time cramming new tests into the suite than it takes to
 write the new production code. As you modify the production code, old
 tests start to fail, and the mess in the test code makes it hard to get those
 tests to pass again. So the tests become viewed as an ever-increasing
 liability.

 From release to release the cost of maintaining my team’s test suite rose.
 Eventually it became the single biggest complaint among the developers.
 When managers asked why their estimates were getting so large, the
 developers blamed the tests. In the end they were forced to discard the
 test suite entirely.
 But, without a test suite they lost the ability to make sure that changes to
 their code base worked as expected. Without a test suite they could not
 ensure that changes to one part of their system did not break other parts
 of their system. So their defect rate began to rise. As the number of
unintended defects rose, they started to fear making changes. They
 stopped cleaning their production code because they feared the changes
 would do more harm than good. Their production code began to rot. In
 the end they were left with no tests, tangled and bug-riddled production
 code, frustrated customers, and the feeling that their testing effort had
 failed them.

 The moral of the story is simple: Test code is just as important as
 production code. It is not a second-class citizen. It requires thought,
 design, and care. It must be kept as clean as production code.

 It is unit tests that keep our code flexible,
 maintainable, and reusable. The reason is simple. If you have tests, you
 do not fear making changes to the code! Without tests every change is a
 possible bug. No matter how flexible your architecture is, no matter how
 nicely partitioned your design, without tests you will be reluctant to
 make changes because of the fear that you will introduce undetected
 bugs.

 you can improve that architecture and design without
 fear!

 So having an automated suite of unit tests that cover the production code
 is the key to keeping your design and architecture as clean as possible.
 Tests enable all the -ilities, because tests enable change.
So if your tests are dirty, then your ability to change your code is
 hampered, and you begin to lose the ability to improve the structure of
 that code. The dirtier your tests, the dirtier your code becomes.
 Eventually you lose the tests, and your code rots.

 What makes a clean test? Three things. Readability, readability, and
 readability. Readability is perhaps even more important in unit tests than
 it is in production code. What makes tests readable? The same thing that
 makes all code readable: clarity, simplicity, and density of expression. In
 a test you want to say a lot with as few expressions as possible.

 That is the nature of the dual standard. There are things that you might
 never do in a production environment that are perfectly fine in a test
 environment. Usually they involve issues of memory or CPU efficiency.
 But they never involve issues of cleanliness.

One Assert per Test.

Single Concept per Test
Perhaps a better rule is that we want to test a single concept in each test
function. We don’t want long test functions that go testing one
miscellaneous thing after another. 
Listing 9-8 is an example of such a
test. This test should be split up into three independent tests because it
tests three independent things. Merging them all together into the same
function forces the reader to figure out why each section is there and
what is being tested by that section.

F.I.R.S.T.8

 8. Object Mentor Training Materials.

 Clean tests follow five other rules that form the above acronym:
 Fast Tests should be fast. They should run quickly. When tests run slow,
 you won’t want to run them frequently. If you don’t run them frequently,
 you won’t find problems early enough to fix them easily. You won’t feel
 as free to clean up the code. Eventually the code will begin to rot.

 Independent Tests should not depend on each other. One test should not
 set up the conditions for the next test. You should be able to run each test
 independently and run the tests in any order you like. When tests depend
 on each other, then the first one to fail causes a cascade of downstream
 failures, making diagnosis difficult and hiding downstream defects.

 Repeatable Tests should be repeatable in any environment. You should
 be able to run the tests in the production environment, in the QA
 environment, and on your laptop while riding home on the train without
 a network. If your tests aren’t repeatable in any environment, then you’ll
 always have an excuse for why they fail. You’ll also find yourself unable
 to run the tests when the environment isn’t available.

 Self-Validating The tests should have a boolean output. Either they pass
 or fail. You should not have to read through a log file to tell whether the
 tests pass. You should not have to manually compare two different text
 files to see whether the tests pass. If the tests aren’t self-validating, then
 failure can become subjective and running the tests can require a long
 manual evaluation.

 Timely The tests need to be written in a timely fashion. Unit tests should
 be written just before the production code that makes them pass. If you
 write tests after the production code, then you may find the production
 code to be hard to test. You may decide that some production code is too
 hard to test. You may not design the production code to be testable.

If you let the tests rot, then your code will rot too. Keep your tests clean.
