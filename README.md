# Relatório do trabalho sobre números primos

O relatório está organizado em diferentes arquivos `README.md` presentes em diferentes submódulos do projeto.

O relatório é melhor lido na ordem:

- **1** [Gerar Números Pseudo-aleatórios](https://github.com/bnmfw/Seguranca/blob/main/rng/README.md)
- **2** [Funções Axuiliares](https://github.com/bnmfw/Seguranca/blob/main/utils/README.md)
- **3** [Testadores de Primalidade](https://github.com/bnmfw/Seguranca/blob/main/primes/README.md)

Ta bem caprichadinho espero que goste.

## Notação de Complexidade

Para as análises de complexidade no relatório **b** representa o número de bits do valor, enquanto **n** representa o próprio valor.

Vale lembrar que **b** = **log(n)**. Não estranhe quando você encontar uma função de complexidade logaritmica mas ela estiver descrita como **O(b)**, é porque estou analisando o número de bits.

Como python permite o uso de números arbitrariamente grandes, operações bit a bit e aritiméticas são **O(1)** apenas para números de 64 bits ou menos.

Para números acima de 64 bits o número tem de ser decomposto e processado em partes, portanto a complexidade passa a ser **O(b)** para operações bit a bit e soma, enquanto divisão e multiplicação e resto passam a ser **O(b²)**, exceto quando estas útltimas 3 operações são feitas utilizando 2 ou uma de suas potencias como operador, onde a operação pode ser subsitituida por bitshifts para multiplicação e divisão e descartar a parte superior do número para resto, nestes casos a complexidade passa a ser **O(b)**.

Durante as análises de complexidade este conhecimento será levado em questão. A notação **<Complexidade para 64 bits ou menos>|<Complexidade para maiores\>** será usada ao longo das análises. Exemplo:

Operação >> é **O(1)|O(b)**

Operação // é **O(1)|O(b²)**

## Dificuldades encontradas:

O python odeia trabalhar com floats muito grandes, tiver que mudar algumas partes do códido (em especial a função randint) pra trabalhar somente com inteiros.

Implementei exponenciação rápida modular de otário, a função `pow()` do python faz a mesmissa coisa com os mesmos parâmetros. Pelo menos eu posso falar com certeza da complexidade dela e não tive que ler documentação.

O simbolo jacobiano é esquisito e misterioso, eu entendi o que ele faz mas não exatamente _como_. Encontrar um exemplo de implementação dele também não foi direto por que eu nem sabia se tava certo, fiquei gerando varios asserts com ele pra ver se tinha o comportamento esperado e comparando com um online. Tive certeza que estava correto só quando testei o Solovay inteiro e vi que ele estava com o comportamento correto.

Sinceramente, a maioria dos algoritmos foram feitos assim. Podem questionar "Por que você escolheu esses parametros?" ou "Como tem certeza que o algoritmo está correto?", e a resposta é "empiricamente". Os geradores de números pseudo aleatórios foram testados para ver se estavam gerando distribuição uniformes e estavam, isso é prova o bastante que estão corretos. Os testes de primalidade estão coerentes para os primeiros 10 mil primos e tem alta concordância para números altos como visto no teste da disputa. 
