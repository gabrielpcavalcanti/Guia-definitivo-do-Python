# Ambiente virtual

## Introdução

Ambientes virtuais é uma de muitas características da linguagem Python. Elas servem para deixar o Python ‘raiz’ intocado e fazer todos os seus testes e instalação de pacotes nas virtuais environments. 

Python ‘raiz’ é o Python que é instalado no computador (O que fizemos aula passada). É bom deixa-lo sem nenhuma modificação, para que não tenha problemas futuros. 

Os ambientes virtuais servem justamente para evitar isso. Eles copiam todos os aspectos do Python ‘raiz’. Com isso é possível baixar todos os pacotes que quiser, na versão que quiser. Caso ser algum problema, basta deletar. O Python ‘raiz’ fica intocado. 

Outra funcionalidade dos ambientes virtuais é que podemos ter ambientes virtuais com diversas versões do Python e com diversão versões dos pacotes. Basta instalar a versão que deseja no computador, seguindo os mesmos passos da aula passada.

Veremos duas maneiras de criar ambientes virtuais e como trocar de versão dos Python pelo terminal 

## Criação do ambiente virtual – Primeiro método

### 1 - Criando um ambinete virtual

Abra o cmd e digite:

```
python -m venv <ambiente virtual>
```

O nome ambiente virtual é opcional, pode colocar o nome que quiser, como DataScience, webdevelope, ou simplesmente teste, teste2, cookie. Uma dica é colocar o nome relativo ao trabalho que está fazendo. 

Ele cria o ambiente virtual no diretório especificado do cmd. Escolha o local onde queira criar o ambiente virtual e lembre dele para não ter problemas depois.

### 2 - Ativando um ambinete virtual

Criamos o ambiente virtual, mas agora é preciso ativa-lo, para poder entrar dentro do ambiente e instalar as bibliotecas que quiser. 

Para ativar, entre no cmd, vá até a pasta do ambiente virtual, com o comando cd, até a pasta Scripts. Lá irá ter um arquivo activate. 

Basta digitar: 

```
activate
```

Se quiser ativar dentro pasta do ambinete virtual, use o comando no terminal:

```
Scripts\activate
```

### 3 - Sair do ambinete virtual

Digite 

```
deactivate 
```

dentro do ambiente virtual ou fechar o terminal.

### 4 - Deletar um ambiente vietual

Caso queira deletar o virtual env, basta ir no diretório que está a pasta, clicar com o botão direito do mouse e excluir.

Como é uma pasta, é a unica forma de fazer sem ser pelo terminal.

Se quiser fazer pelo terminal, use os comandos do cmd: va na pasta com o cd e use **del nome_do_arquivo**

## Criação do ambiente virtual – Segundo método

Esse segundo método é um pouco mais complicado para fazer as configurações, mas feito isso, fica bem mais simples e rápido para criar, deletar e ativar.  

### 1 - Instalando o virtualenv

Abra o cmd e digite:

```
pip install virtualenv
```
Isso irá instalar um pacote dentro do Python ‘raiz’ (nesse caso, não haverá problema). 

Se seu pip estiver desatualizado, utilize o comando:

```
python –m pip install --upgrade pip
```

Caso não estiver, baixe o segundo pacote, com o comando:

``` 
pip install virtualenvwrapper-win
```

### 2 - Adiconando um caminho para os ambientes virtuais

Vá nas variáveis do sistema. Clique em nove e digite:


Nome da variável: "WORKON_HOME"

Valor da variável: %USERPROFILE%Enves

e clique em OK. 

Isso irá criar uma Pasta chamada Envs na pasta do usuário. Todas os ambientes virtual serão criados lá, sem a necessidade de ficar mudando de diretório.  

### 3 - Criando e ativanado um ambiente virtual

Abra o terminal e digite:

```
mkvirtualenv <nome do ambiente>
```

Com esse comando o ambiente virtual é criado e ativado.

### 4 - Sair do ambinete virtual

Digite 

```
deactivate 
```

dentro do ambiente virtual ou fechar o terminal.

### 5 - Reativar o ambiente vietual

Use o comando:

```
workon <ambiente virtual>
```

### 6 - Deletar um ambiente vietual

Pode fazer da mesma forma da maneira um ou simplismente digitar:

```
rmvirtualenv <ambiente virtual>
```

### 7 - Listar os ambiente virtuais existente

```
workon
```

Listar pacotes instalados no ambiente virtual atual

```
lssitepackages
```

### 8 - Criar um ambiente virtual e instalar pacotes automaticamente

Se você quiser criar um ambiente e instalar pacotes do requirements.txt ao mesmo tempo:

```mkvirtualenv nome_do_ambiente -r requirements.txt

```

Isso instala todas as dependências listadas no arquivo requirements.txt logo após a criação do ambiente.

## Instalando pacotes

### 1 - Usando o pip

Para instalar um pacote, use o comando:

```
pip install <nome do pacote>
```

Lembre que para instlar bibliotecas dentro de um abinte virtual tem que se certificar que está no ambiente virtual que deseja. 

Para saber isso, vai a aprecer o nome do ambiente em parenteses antes do diretorio que estiver dentro do terminal, por exemplo:

```
(AmbienteVirtual) C:\Users\Avell>
```

Para verificar quais bibliotecas instalados dentro e fora dos ambientes virtuais, use o comando:

```
pip freeze
```

Para desistalar uma biblioteca em específico, use:

```
pip uninstall <nome da biblioteca>
```

Para saber mais comandos do pip, abra o arquivo 02_Comandos_do_cme_e_pip nessa mesma pasta.

## Trocar versões do Python

Em algumas situações é preciso ter várias versões do python instaladas no computador. Projetos diferentes podem necessitar versões do Python e de bibliotecas específicas. 

Lembre que tudo que ira ser mostrado só vale se tiver mais de uma versão do Python instalada no computador. Caso não tenha, todos os ambientes virtuais serão criadas no Python que estiver instalada no computador.

### 1 - Mudar a ordem dos caminhos nas variáveis de ambiente

Quando Python vai ler um arquivo, ele sempre procura o primeiro arquivo nas variáveis de ambiente, então troque a ordem lá que estará utilizando uma versão difernte do Python

Em outras palavers, selecione Path e clique em editar. A lista que é mostarda tem hierarquia, ou seja, os caminhos que estiver em cima, serão acessados primeiro no path. Se quiser uma versão diferente do python, inverta a ordem da lista.  

### 2 - Mudar as versões no terminal

A versão padrão será a que estiver listada primeiro nas variáveis de ambiente, mas se quiser acessar uma versão específica instalada no terminal, basta utilizar o comando

```
py -<versão> 
```

Por exemplo, py -3.10 ou py -3.7.

### 3 - Criando ambientes virtuais

Para criar um ambiente virtual com uma diferente versão, basta mudar as variáveis de ambiente para a versão que deseja e criar a virtual env (simples assim). 

Uma maneira mais rápida, sem ter que precisar mudar nas variáveis do ambiente e utilizar o comando:

```
virtualenv --python=<versão> <ambiente virtual>” 
```
O Interessante com esse método é que se sair do ambiente virtual, o python principal se torna a versão do ambiente virtual. Mas se fechar o cmd e abrir de novo. A versão do python volta a ser a padrão.

---
Proxima Aula: 03_Comandos_cmd_e_pip.md -> Pasta 01_PreparacoesIniciais.
