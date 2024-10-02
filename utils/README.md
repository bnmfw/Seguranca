# Funções Auxiliares

### Exponenciação Modular Rápida
Eu implementei de cabeça.

Exponenciação rápida famosamente tem complexidade **O(log n)** sendo n o tamanho do expoente, 
```
if exp % 2: result = (result * base) % mod      
base = (base * base) % mod
exp >>= 1
```

Ao lembrar que a operação * é **O(1)|O(b²)** e o bloco é repetido **O(b)** vezes é evidente que a função como um todo tem complexidade **O(b)|O(b³)**.

### Simbolo de Jacobi
Eu não entendi como isso funciona mas eu fiz igualzinho o da [wikipédia](https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_C++) e deu certo 😁!

Esse bloco segue uma estrutura parecida com o anterior.

```
while not a % 2:
    a >>= 1
    r = n % 8
    if r == 3 or r == 5:
        t = -t
```

Assim sua complexidade é **O(b)|O(b³)**.

O bloco está dentro de um laço que depende do valor de a e eu aaaacho que faz ser **O(1)** mas não tenho certeza.

Enfim, a complexidade final é a mesma da Exponenciação.

### Crono
Manejador de contexto pra contar o tempo, nada de mais
