# Introdução

A partir de agora que a programação começa a ficar um pouco mais interessante. Todas as aulas anterioires concentram o básico da programação. É possível fazer muita e muitas tarefas apenas com o conhecimento adquirido, mas a partir de agora temos um novo paradigma da programação, utilizando funções criadas pelo próprio programador. É o paradigma funcional.

O Python aceita diversos paradigmas, o mais poderozo e que veremos depois é o POO (Programação orientada a objetos), mas é preciso primeiro aprender o paradigma funcional. 

Já era possível ver ele desde o início, mas fica mais complexo e sem necessidade. Agora a necessidade vai existir e irá ser utilizado. Na aula 03_Padroes_adotados.md já alertei sobre isso.

A partir de agora, todo programa terá essa estrutura básica:

```python
def main() -> None:
    ...
 
 
if __name__ == '__main__':
    main()

```

O programa pricipal ficará dentro da função main( ) e sempre será chamada dentro do `if __name__ == '__main__':`. 

## O que é o if __name__ == '__main__': no Python?

É usado para definir o ponto de entrada de um script, ou seja, indicar qual código deve ser executado somente quando o arquivo for rodado diretamente, e não quando ele for importado como módulo.

Sem ele, qualquer código no arquivo seria executado toda vez que ele fosse importado.

É o padrão profissional em Python e uma boa prática. Não existia necessidade antes porque apenas estavamos aprendendo a sintaxe e a parte básica.

A partir da próxima aula vamos ver de fato o que é uma função e todas as suas características.

---
