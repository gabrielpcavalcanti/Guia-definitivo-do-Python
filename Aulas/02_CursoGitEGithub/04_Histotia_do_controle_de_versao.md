# História do comtrole de versão

Rerirei esse texto do curso de controle de versão que fiz da Google. Todo os créditos a eles.

Como você já sabe, o controle de versão é um sistema que registra as alterações feitas em um arquivo ou conjunto de arquivos ao longo do tempo para que seja possível acessar versões específicas posteriormente. No desenvolvimento de software, os sistemas de controle de versão (VCS) permitem que os desenvolvedores gerenciem as alterações em seu código e acompanhem quem fez cada alteração. Mas como surgiu esse software?

O controle de versão tem uma longa história que remonta à década de 1980. Na verdade, os sistemas de controle de versão foram criados antes da Internet!

Um dos primeiros sistemas de controle de versão importantes foi o Concurrent Versions System (CVS). Ele foi desenvolvido pela primeira vez em 1986 por Walter F. Tichy na Purdue University e lançado publicamente em 1990.

O CVS armazena informações sobre cada arquivo em uma estrutura de pastas, incluindo o nome do arquivo, seu local na estrutura de pastas, quem o modificou pela última vez e quando foi modificado pela última vez. O CVS também armazena informações sobre pastas, incluindo seus nomes e quem as criou.

Ele foi popular por muitos anos; no entanto, tem algumas falhas significativas em seu projeto. O CVS não inclui verificações de integridade, o que significa que seus dados podem ser corrompidos. Quando você atualiza ou envia alterações para o sistema, se ocorrer um erro, o sistema aceita os arquivos parciais ou corrompidos. Além disso, o sistema foi projetado principalmente para arquivos de texto, não para arquivos binários, como imagens ou vídeos.

O principal sucessor do CVS foi o Subversion (SVN).

A CollabNet desenvolveu o Subversion em 2000 e resolveu muitos dos problemas presentes no CVS. Para garantir a integridade dos dados, incluiu verificações de integridade em seu projeto. Ele também suportava o controle de versão de arquivos binários melhor do que o CVS. Graças a esses aprimoramentos, o SVN tornou-se popular na comunidade de código aberto, com a oferta de hospedagem gratuita para projetos de código aberto pelo Google e pelo SourceForge.

Entretanto, o Subversion usava um modelo de VCS centralizado. Isso significa que todas as operações precisam ser feitas usando um servidor centralizado. Se o servidor ficasse inativo ou lento, isso impediria o desenvolvimento.

Em 2005, dois novos projetos foram iniciados para desenvolver sistemas de controle de versão distribuídos: Mercurial e Git. Ambos os projetos foram criados em resposta a um evento envolvendo o desenvolvimento do kernel do Linux.

Anteriormente, o kernel do Linux usava um VCS proprietário conhecido como BitKeeper. O BitKeeper foi um dos primeiros sistemas de controle de versão distribuídos, lançado inicialmente em 2000. Originalmente, o BitKeeper forneceu uma licença gratuita a Linus Torvalds para apoiar o desenvolvimento do Linux. Entretanto, em 2005, a licença foi revogada. Essa controvérsia levou à criação dos projetos Mercurial e Git.

O Mercurial foi desenvolvido por Olivia Mackall. Ele foi desenvolvido como um VCS distribuído de alto desempenho. Muitas plataformas que ofereciam hospedagem do Subversion começaram a oferecer também a hospedagem do Mercurial. Ele se tornou popular porque os usuários do Subversion acharam fácil fazer a transição para um repositório Mercurial, graças aos provedores de hospedagem e à sua pequena curva de aprendizado.

O Git foi desenvolvido por Linus Torvalds para hospedar o código-fonte do kernel do Linux. Como o Mercurial, ele é um VCS distribuído. Seu primeiro lançamento público ocorreu em 2007.

O Git tornou-se popular na comunidade de código aberto devido ao seu design de VCS distribuído e ao fato de o Github oferecer hospedagem gratuita do Git para projetos de código aberto. Desde então, o Git se tornou o sistema de controle de versão escolhido para muitos projetos de software de código aberto e proprietário.

Traduzido com a versão gratuita do tradutor - DeepL.com.

---
