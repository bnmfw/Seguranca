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

Para números acima de 64 bits o número tem de ser decomposto e processado em partes, portanto a complexidade passa a ser **O(b)** para operações bit a bit e soma, enquanto divisão e multiplicação passam a ser **O(b²)**.

Durante as análises de complexidade este conhecimento será levado em questão. A notação **<Complexidade para 64 bits ou menos>|<Complexidade para maiores\>** será usada ao longo das análises. Exemplo:

Operação >> é **O(1)|O(b)**

Operação // é **O(1)|O(b²)**
