## Funções Auxiliares

### Exponenciação Modular Rápida
Eu implementei de cabeça.

Exponenciação rápida famosamente tem complexidade **O(log n)** sendo n o tamanho do expoente, 
Como as outras funções neste projeto usam **n** como sendo o **numero de bits** ao invés do tamanho do número. (bits = log tamanho)

Como lidamos com inteiros longos, operações aritiméticas para valores com mais de 64 bits não são **O(1)**.
Multiplicação (*) e divisão inteira (//) tem complexidade **O(n²)** para inteiros longos.

Isso implica, portanto que a complexidade do seguinte bloco seja **O(n²)**:
```
if exp % 2: result = (result * base) % mod      
base = (base * base) % mod
exp //= 2
```
Este bloco, por sua vez é executado enquanto ```exp > 0``` que, 
por cair pela metade em toda iteração, faz com que o bloco seja repetido **n** vezes (bit shifta exp toda iteração).

Desta forma a função como um todo tem complexidade **O(n)** até 64 bits e **O(n³)** caso constrário onde n é **o número de bits do expoente! não o valor absoluto!**

### Simbolo de Jacobi
Eu não entendi como isso funciona mas eu fiz igualzinho o da [wikipédia](https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_C++) e deu certo 😁!

Acho que você ja pegou a ideia da analise de complexidade com o último exemplo.

```
while not a % 2:
    a //= 2
    r = n % 8
    if r == 3 or r == 5:
        t = -t
```

Esse bloco tem complexidade **O(n³)** para números acima de 64 bits e **O(n)** abaixo.

O bloco está dentro de um laço que depende do valor de a e eu aaaacho que faz ser **O(1)** mas não tenho certeza.

Enfim, a complexidade final é a mesma da Exponenciação.
