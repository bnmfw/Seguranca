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
|80|<0.01|<0.01|0.01|928543277721233392399583|
|128|0.01|0.01|0.02|231605334013172780577480704758319382541|
|168|0.02|0.01|0.03|288111013610233365916819582242348628092597702873409|
|224|0.04|0.01|0.05|13497627121872141750512922227304410239929005502103684362541429233715|
|256|0.03|0.02|0.05|57896044618678045486287319818188597543260997141016627580992189820593446069569|
|512|0.51|0.15|0.67|6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937188979000717499643618380476277436493353887076907164553935074257637|
|1024|0.55|0.33|0.87|89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270493409679682564504237332494948466838957602693266399656603023338923|
|2048|22.29|8.28|30.42|16158503035655503650357438344334975980222051334857742016065172713762327569433945446598600705761456731844358980460949009747059779575245460547544076193224141560315438683650498045875098875194826053398028819192033784138396109321309878080919047169238085235290822926018152521443787945770532904303776199561965192760957166694834171210342487393282284747428088017663161029038902829665513096354230157075129296432088558362971801859230928678799175576150822952201848806616643615613562842355410104862578550863465661734839271290328348967522998634176499319107762583194878249967839462924548000966344244783347382049321933888224677078873|
|4096|76.19|30.72|135.91|522194440706576253345876355358312191289982124523691890192116741641976953985778728424413405967498779170445053357219631418993786719092896803631618043925682638972978488271854999170180795067191859157214035005927973113188159419698856372836167342172293308748403954352901852035642024370059304557233988891799014503343469488440893892973452815095130470299789726716411734651513348221529512507986199933857107770846917779942645743159118957217248367043905936319748237550094520674504208530837546834166925275516486044134775384991808184705966507606898412918594045916828375610659246423184062775112999150206172392431297837246097308511903252956622805412865917690043804311051417135098849101156584508839003337597742539960818209685142687562392007453579567729991395256699805775897135553415567045292136442139895777424891477161767258532611634530697452993846501061481697843891439474220308003706472837459911525285821188577408160690315522951458068463354171428220365223949985950890732881736611925133626529949897998045399734600887312408859224933727829625089164535236559716582775403784110923285873186648442456409760158728501220463308455437074192539205964902261490928669488824051563042951500651206733914027728710345550252614403329931891765775615422669382736962432553|

## Análise de Complexidade Xorshift

## Alterar

## Análise de Miller Rabin:
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

