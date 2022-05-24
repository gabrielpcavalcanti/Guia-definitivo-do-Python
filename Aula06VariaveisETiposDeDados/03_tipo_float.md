# Tipo float

Representa os núemros reais da matemática, ou seja, os que possuiem casas decimais. Podem ser positivos ou negativos.

Como a linguagem segue o padrão amaricano, o separador decimal é o ponto. A vírgula possui outra função na linguagem, separação de argumentos na função, separação de elementos numa lista ou dicionário e na criação de truplas.

obs: Se não entendeu algum termo, não se preocupe, veremos mais na frente, tudo com detalhes.

A divisão no python sempre gera um número do tipo float, a menos que for utilizado o Cast ou o símbolo // (transforma a divisão num inteiro). Ambos os casos descartam a parte decimal, elas não execultam o arredendamento. Se quiser arendondar o número, utilize a função round( ).

A soma, subtração e multiplicação de numeros reais, geram numeros reais; A soma, subtração e multiplicação de um número real por um inteiro, gera também um núemero real.

```python
num = 4.5
num_1 = 7.8
num_2 = 5
num_3 = -8.6

res_1 = num + num_1
res_2 = num_1 // num_2
res_3 = num_2 / num_3
res_4 = round(res_3, 2)
res_5 = num_3 * num_2

print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)
```

```python
12.3
1.0
-0.5813953488372093
-0.58
-43.0
```
