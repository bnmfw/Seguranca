# Geração de Número Pseudo Aleatórios
Para a geração de números pseudoaleatórios os algoritmos implementados foram o `Lagged Fibonacci Generator` e o `Xorshift`.
Para gerar um relatório de performance dos algoritmos rode, a partir da pasta principal do projeto:
```
make rng
```
Cada algoritmo gerará por padrão 1 milhão de números pseudo aleatórios, para cada combinação de bits indicada no enunciado do trabalho.
Será reportado para cada conjunto de 1 milhão de números:
- O tempo de geração (i5-6200U);
- O número de repetições no conjunto;
- A média da distribuição gerada e seu erro relativo à ideal;
- O desvio padrão da distribuição gerada e seu erro relativo à ideal.

  Tais análises estatisticas não serão feitas para conjuntos gerados a partir de números com mais de 512 bits.

#### Dados Xorshift
Nunca houve nenhuma repetição na distribuição
| Bits | Tempo médio por número (us) | Erro relativo da média (%) | Erro relativo do desvio padrão (%) |
|---|---|---|---|
|40|1.02|0.04|0.01|
|56|1.02|0.08|0.09|
|80|1.03|0.06|0.03|
|128|1.08|0.00|0.05|
|168|1.14|0.02|0.01|
|224|1.15|0.01|0.04|
|256|1.32|0.08|0.01|
|512|1.55|0.03|0.03|
|1024|1.85|-|-|
|2048|2.58|-|-|
|4096|3.93|-|-|

#### Dados Lagged Fibonacci Generator
Nunca houve nenhuma repetição na distribuição
| Bits | Tempo médio por número (us) | Erro relativo da média (%) | Erro relativo do desvio padrão (%) |
|---|---|---|---|
|40|0.51|0.06|0.06|
|56|0.54|0.01|0.05|
|80|0.56|0.01|0.03|
|128|0.59|0.04|0.05|
|168|0.66|0.03|0.02|
|224|0.63|0.01|0.03|
|256|0.60|0.04|0.00|
|512|0.70|0.61|0.76|
|1024|0.82|-|-|
|2048|1.09|-|-|
|4096|1.14|-|-|

## Análise de Complexidade Xorshift
O Algoritmo foi implementado de acordo com o exemplo de [implementação da wikipédia](https://pt.wikipedia.org/wiki/Xorshift#Exemplo_de_implementa%C3%A7%C3%A3o).

O Algoritmo parte de um estado inicial, e realiza operações de xor com o próprio estado bitshiftado.

A operação de bitshift pode ser entendida como elevar o estado a uma potencia de 2 (mesmo que fracionária), o que não parece muito _aleatório_, 
mas a operação de xor garante que essencialmente ruido sera introduzido ao estado.

O estado inicial (2³¹-1) foi escolhido por ser um primo que eu gosto. 

Para análise de complexidade é de extrema importância ressaltar que operações bit a bit em python nem sempre são **O(1)**!
Como python permite o uso de número arbitrariamente grandes, operações bit a bit são **O(1)** apenas para números de 64 bits ou menos.
Para números acima de 64 bits a complexidade passa a ser **O(n)** onde **n** é **o número de bits usados pelo número**.

Implementação do Algoritmo:
```
self.state ^= self.state << 13
self.state %= self.mod
self.state ^= self.state >> 17
self.state %= self.mod
self.state ^= self.state << 5
self.state %= self.mod
```
O algoritmo é implementado sem laços, com 9 operações apenas. Assim, a complexidade do algoritmo é **O(1)** para números menores que 64 bits e **O(n)** para o restante.
A Equação `T = bits / 1379 + 1.02` aproxima muito bem o tempo usado para cada caso.

## Análise de Complexidade Lagged Fibonacci Generator
O Algoritmo foi implementado de acordo com a [explicação da wikipédia](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator).

O Algoritmo possui internamente uma vetor de **k** posições ja inicializado com número arbitrários.

A cada iteração, o último elemento do vetor (**i**) é operado com um operador binário qualquer com outro elemento **j** da lista.

O novo valor é inserido no inicio do vetor, e o último apagado, assim mantendo o tamanho do vetor e movendo os outros elementos como se numa fila.

Para essa implementação os valores de **i** e **j** foram 55 e 24 pois foi isso que o ChatGPT recomendou.

O vetor é inicializado como `[((i + 3) ** i - i * 13) % mod for i in range(size)]` pois isso me parece bem aleatório.

A operação binária escolhida foi a soma.

A discussão de complexidade para operações bit a bit se aplica para operação de soma.

Implementação do Algoritmo:
```
value = self.state_queue[-self.small] + self.state_queue[-self.big]
value %= self.mod
self.state_queue.pop(0)
self.state_queue.append(value)
```

As duas primeiras linhas do algoritmo tem complexidade **O(1)** para números com menos de 64 bits e **O(n)** para o restante.
As outras duas linhas são uma deleção e uma inserção em lista que tem complexidade **O(tamanho da lista)**, ou seja **O(1)** pois o tamanho da lista é constante neste caso.

Assim a complexidade do algoritmo como um todo é **O(1)**/**O(n)**.

A Equação `T = bits / 2785 + 0.51` aproxima decentemente o tempo usado para cada caso.

