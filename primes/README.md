# Geração de Número Pseudo Aleatórios
Para o teste de primalidade o segundo algoritmo implementado foi o `Solovay-Strassem` pois `Fermat` é ruim e `Frobenius` é muito complicado (não entendi).
Para gerar um relatório de performance dos algoritmos rode, a partir da pasta principal do projeto:
```
make miller
make solo
```
Para comparar os geradores rode:
```
make dispute
```
Para o experimento de teste de primalidade foi gerado um número aleatório inteiro no intervalo [2^(bit-1) - 2^(bit)], ou seja ele é sempre um numero que utiliza todos os bits designados.

Para cada número de bits o mesmo experimento foi realizado usando o `Miller-Rabin`, o `Solovay-Strassem` e o acordo de ambos para decidir se o número era de fato primo. 

A mesma seed foi usada em todos os experimentos, todos algoritmos encontraram os mesmos primos.

[Todo número primo maior que 3 ou é um antecessor ou sucessor de um múltiplo de 6.](https://owlcation.com/stem/Every-Prime-Number-Larger-Than-3-is-1-Away-From-a-Multiple-of-6-A-Proof) Assim, a estratégia para encontrar um primo é partir do número aleatório, descer até o antecessor de multiplo de 6 mais próximo e fazer saltos alternados de 2 e 4 posições, procurando somente números potencialmente primos. Essa estratégia reduz o número de valores investigados até o primo em 1/3.

Para cada número de bits será reportado:
- O tempo de geração para cada algoritmo (i5-13420H - Sim eu um notebook entre o experimento de rng e esse, tava insuportavel)
- O número gerado.

| Bits | Miller (s) | Solovay (s) | Acordo (s) | Primo |
|---|---|---|---|---|
|40|<0.01|<0.01|<0.01|598205539489|
|56|<0.01|<0.01|<0.01|48831810419249983|
|80|<0.01|<0.01|<0.01|928543277721233392399583|
|128|0.01|0.01|0.01|231605334013172780577480704758319382541|
|168|0.01|0.01|0.02|288111013610233365916819582242348628092597702873409|
|224|0.01|0.01|0.02|13497627121872141750512922227304410239929005502103684362541429233715|
|256|0.01|0.02|0.03|57896044618678045486287319818188597543260997141016627580992189820593446069569|
|512|0.13|0.15|0.28|6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937188979000717499643618380476277436493353887076907164553935074257637|
|1024|0.30|0.32|0.62|89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270493409679682564504237332494948466838957602693266399656603023338923|
|2048|8.12|8.11|16.22|16158503035655503650357438344334975980222051334857742016065172713762327569433945446598600705761456731844358980460949009747059779575245460547544076193224141560315438683650498045875098875194826053398028819192033784138396109321309878080919047169238085235290822926018152521443787945770532904303776199561965192760957166694834171210342487393282284747428088017663161029038902829665513096354230157075129296432088558362971801859230928678799175576150822952201848806616643615613562842355410104862578550863465661734839271290328348967522998634176499319107762583194878249967839462924548000966344244783347382049321933888224677078873|
|4096|31.17|30.17|61.22|522194440706576253345876355358312191289982124523691890192116741641976953985778728424413405967498779170445053357219631418993786719092896803631618043925682638972978488271854999170180795067191859157214035005927973113188159419698856372836167342172293308748403954352901852035642024370059304557233988891799014503343469488440893892973452815095130470299789726716411734651513348221529512507986199933857107770846917779942645743159118957217248367043905936319748237550094520674504208530837546834166925275516486044134775384991808184705966507606898412918594045916828375610659246423184062775112999150206172392431297837246097308511903252956622805412865917690043804311051417135098849101156584508839003337597742539960818209685142687562392007453579567729991395256699805775897135553415567045292136442139895777424891477161767258532611634530697452993846501061481697843891439474220308003706472837459911525285821188577408160690315522951458068463354171428220365223949985950890732881736611925133626529949897998045399734600887312408859224933727829625089164535236559716582775403784110923285873186648442456409760158728501220463308455437074192539205964902261490928669488824051563042951500651206733914027728710345550252614403329931891765775615422669382736962432553|

## Complexidade de Randint:
Surpreendentemente, a complexidade de randint pode ser mais cara que apenas a geração de números pseudoaleatórios.

A geração de número pseudoaleatório para ambos algoritmos tem complexidade [**O(1)|O(b)**](https://github.com/bnmfw/Seguranca/blob/main/rng/README.md), ou seja, independente do algoritmo usado a geração tem a mesma complexidade.

A diferaça é que o algoritmo para geração do randint usa as operações aritiméticas de divisão inteira e multiplicação que é **O(1)|O(b²)**.

Assim a complexidade do randint é **O(1)|O(b²)** como um todo.

## Análise de Complexidade Miller Rabin:

O Algoritmo foi implementado de acordo com o [material apresentado em sala de aula](https://presencial.moodle.ufsc.br/pluginfile.php/625534/mod_resource/content/5/Matem%C3%A1tica%20para%20Criptografia%20e%20RSA.pdf).

Algoritmos de verificação de primalidade geralmente partem de uma premissa simples. Parte-se de alguma propriedade que os números primos seguem, testa-se a propriedade para o número em questão. Se a propriedade se mantém, o número provavelmente é primo, se não, com certeza não é.

O Algoritmo de Miller Rabbin é baseado na seguinte propriedade de número primos:

Parte-se do pequeno teorema de Fermat, onde `a^(p-1) ≡ 1 (mod p)` para qualquer primo e qualquer `a` não divisivel por `p`. O algoritmo de Miller Rabin decompõe `p-1` em `2^k*m`

Todo primo maior que 3 tem um antecessor `p-1` não primo, portanto pode ser fatorado. Fatorando a parte par do número, ele passa a ser representado como `2^k*m` onde `m` é a parte ímpar do número.

Tem-se então, que se para qualquer primo, com `1 < a < p-1` é verdade que:
- `a^m ≡ 1 (mod p)`.
- `a^(2^i*m) ≡ -1 (mod p)` para um `i` entre `0` e `k-1`.

O algoritmo gera um `a` aleatório e realiza todos os testes, caso algum deles seja verdadeiro, o número provavelmente é primo, se nenhuma é verdadeira, o número é com certeza composto.

O algoritmo é dividido em 4 partes. Primeiro separa-se a parte impar do número:
#### 1
```
while not m % 2:
  k += 1
  m >>= 1
```
O laço é executado **O(b)** vezes, uma vez que a cada iteração m é bitshiftado uma vez, porém a operação de bitshift em si tem custo **O(1)** para inteiros pequenos e **O(b)** para inteiros com mais de 64 bits, fazendo o bloco como um todo ter complexidade **O(b)|O(b²)**.
#### 2
```
a = self.randint(1, value - 1)
```
O Randint tem complexidade **O(1)|O(b)**.
#### 3 
```
checked = modexp(a, m, value) 
if checked == 1:
  return True
```
Exponenciação modular rápida tem complexidade [**O(b)|O(b³)**](https://github.com/bnmfw/Seguranca/blob/main/utils/README.md).
#### 4
```
for i in range(k):
  if checked == value - 1:
    return True
  checked *= checked
  checked %= value
```
De acordo com o passo **1**, **k** tem tamanho **b**.
Note que a cada iteração o número em análise é elevado ao quadrado (a o i em 2^i aumenta) portanto não é necessario fazer a exponenicação rapida do 0, apenas multiplicar o número checado por ele mesmo.

O multiplicação tem complexidade **O(1)|O(b²)**. 
O mod tem complexidade **O(1)|O(b²)**

Assim, o bloco 4 tem complexidade **O(b)|O(b³)**.
#### Total
A complexidade final do Miller-Rabin, é portanto **O(b)|O(b³)**.

## Análise de Complexidade Solovay–Strassen:

Assim como o teste de Miller Rabin, o teste de [Solovay-Strassen](https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test) também parte de uma propriedade de números primos para realizar o teste. Dentre as milhares de coisas que Euler provou, uma é que:

`a^((p-1)/2) ≡ jacobi(a,p) (mod p)` para todos os números primos, onde `a` é um inteiro qualquer e `jacobi()` é o símbolo de jacobi. 

O [simbolo de jacobi](https://en.wikipedia.org/wiki/Jacobi_symbol) por sua ver é um operador ternário, que retorna: 
- `0` para números multiplos de `p`.
- `1` se o houver um `x²` que congruente a `a`.
- `-1` caso contrário.

A implementação do algoritmo é literalmente a checagem de congruência.

O grosso do algoritmo é divido em 3 blocos.
#### 1
```
a = self.randint(2, value - 1)
```
O Randint tem complexidade **O(1)|O(b)**.
#### 2
```
j = jacobi(a, value)
```
O simbolo de jacobi tem complexidade [**O(b)|O(b³)**](https://github.com/bnmfw/Seguranca/blob/main/utils/README.md)
#### 3
```
if j == 0: return False
return modexp(a, (value - 1) // 2, value) == j % value
```
A exponenciação modular tem a maior complexidade na sua linha, assim o bloco é **O(b)|O(b³)**.
#### Total
Desta forma a complexidade do Solovay–Strassen é **O(b)|O(b³)**, a mesma de Miller Rabin
