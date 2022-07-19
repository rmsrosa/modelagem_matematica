
@def title = "Modelagem matemática e simulação numérica do resfriamento rápido de morangos com o ar forçado"

# {{ get_title }}

```julia
using LsqFit
using Plots
using DifferentialEquations
using Random
```



* O trabalho de DANIELA C. Z. PIROZZI e MARIÂNGELA AMENDOLA abordou o resfriamento rápido de morangos com ar forçado via simulação numérica.




## Introdução

O resfriamento rápido de alimentos *in natura*, logo após a sua colheita, se faz cada vez mais necessário conforme a demanda por determinados produtos perecíveis aumenta em todo o mundo. Com isso também surge a necessidade de entender esse processo de resfriamento, a fim de torná-lo cada vez mais eficiente. Tal entendimento pode ser obtido a partir de meios experimentais e/ou numéricos, em conjunto com processos de análise teórica.

Como motivação, vamos considerar o resfriamento rápido de morangos através de ar forçado. A análilse feita aqui é inspirada no artigo de DANIELA C. Z. PIROZZI e MARIÂNGELA AMENDOLA, com os dados obtidos pelas autor

No artigo em questão, foram utilizados dados de um experimento real para a validação da simulação numérica. Ou seja, foram necessários medições experimentais de temperatura e o conhecimento de parâmetros físicos. Dentre esses, um é limitante e sensivel a todos os outros, o coeficiente de transferência de calor por convenção, denotado por $h$.

**Objetivo:** Simular o resfriamento dos morangos e obter uma estimativa para $h$. 


## Dados e métodos utilizados:


* Para simular numericamente este processo vamos utilizar o mesmo modelo matemático escolhido no artigo, com base na lei da difusão térmica de Fourier. 

$$ \frac{\partial T}{\partial t}(r,t) = \alpha(\frac{2}{r}\frac{\partial T}{\partial r}(r,t)+\frac{\partial^2 T}{\partial r^2}(r,t))$$ $t>0, r \in [0,R]$

* $T(r,t) = $ temperatura no interior do morango ao longo do tempo, $C°$.
* $t = $ tempo, $s$.
* $r = $ distância até o centro do morango, $m$.
* $\alpha = $ difusividade térmica do morango, $m^2s^{-1}$.
* $K_p = $ condutividade térmica do morango, $W\deg m^{-1}°C^{-1}$.
* $C_p = $ calor específico do morango, $JKg^{-1}°C{-1}$
* $\rho = $ densidade do morango, $Kgm^{-3}$.
* $R = $ raio do morango, $m$.

Como condição inicial, temos que: $$T(r,0) = T_0,  r \in \mathbb{R} $$

As condições de contorno são: $$\frac{\partial T}{\partial r}(0,t) = 0; t \geq 0$$


$$-K_p\frac{\partial T}{\partial r}(R,t) = h[T_s(t)-T_a(t)]; t \geq 0$$


* $h=$ coeficiente de transferência de calor por convenção, $Wm^{-2}°C^{-1}$.
* $T_s(t)=$ temperatura na superfície do morango, $C°$.
* $T_a(t)=$ temperatura na câmera de resfriamento, $C°$.

Para o calculo dos resíduos, vamos utilizar a seguinte norma: $$|T_{exp} - T_{num}| = \sqrt{\sum_{i=1}^{n} (T_{exp}-T_{num})^2} $$

* $T_{exp}=$ temperatura no centro do morango, obtida experimentalmente, $°C$.
* $T_{num}=$ temperatura no centro do morango, obtida numericamente, $°C$.
* $n=$ número total de medidas.
* $t=$ tempo, $s$.

$K_p = 0,54 Wm^{-1}°C^{-1}$

$\alpha = 1,72.10^{-7}m^2s^{-1}$

$R = 0,025m$


O método numérico utizado para resolver a equação é o método explícito das diferenças finitas. Para isso temos que discretizar nossa equação. 

 O primeiro passo é criar uma partição com n pontos dos intervalos $(0,R)$ $e$ $(0,T_{final})$

 Daí definimos nosso $T$ discretizado como: $T_i^n = T(i\Delta r,n\Delta t)$   ;    para   $i = [1,nx], n = [1,nt]$
 
 * $i$ é a posição dos pontos de resolução na direção radial.
 
 * $nx$ último ponto na direção radial.
 * $n$ numéros de passoa na direção do tempo.
 * $nt$ último passo na direção do tempo.
 * $\Delta r$ distância entre os pontos de resolução na direção radial.
 * $\Delta t$ distância entre os pontos de resolução na direção do tempo.
 
 Podemos aproximar a derivada parcial de T em relação ao tempo, com erro local $\Delta t$:
$$ \frac{\partial T}{\partial t}(r,t) \approx \frac{T(r,t+\Delta t) - T(r,t)}{\Delta t}$$

Fazendo o mesmo para a derivada em relação ao eixo radial, com erro local $\Delta r$, também temos que:

$$ \frac{\partial T}{\partial r}(r,t) \approx \frac{T(r+\Delta r,t) - T(r,t)}{\Delta r}$$

A ideia do método das diferenças finitas aqui é usar a série de Taylor para ter uma aproximação da segunda derivada de $T(r,t)$ em relação ao raio da seguinte forma:

Sabemos que a série de Taylor de uma função $f$ no ponto $x+h$ é dada por: $$f(x+h) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x)h^n}{n!} $$

Como vamos derivar em relação ao raio, tomamos $T(r,t) = T(r)$ para facilitar as contas:

$$T(r+\Delta r) = T(r) +  \frac{\partial T}{\partial r}(r)\Delta r +  \frac{\partial ^2 T}{ \partial r^2}(r)\frac{\Delta t}{2} ^2 $$

$$T(r-\Delta r) = T(r) -  \frac{\partial T}{\partial r}(r)\Delta r + \frac{\partial ^2 T}{ \partial r^2}(r)\frac{\Delta r}{2} ^2 $$

Com erro da ordem $\Delta r ^2$. Somando as equações, ficamos com:

$$ T(r+\Delta r) + T(r - \Delta r) = 2T(r) + \frac{\partial ^2 T}{ \partial r^2}(r)\Delta r ^2 $$

$$ \frac{\partial ^2 T}{ \partial r^2}(r) = \frac{T(r+\Delta r) + T(r - \Delta r) - 2T(r)}{\Delta r^2}$$

Com erro da ordem $\Delta r^2$, ficamos com a equação discretizada da forma:

$$ \frac{\partial ^2 T_i}{ \partial r^2} = \frac{T_{i+1} + T_{i-1} - 2T_i}{\Delta r^2}$$

E também obtemos acima que: 

$$ \frac{\partial  T_i}{ \partial r} = \frac{T_{i+1} - T_i}{\Delta r}$$

$$ \frac{\partial  T^n}{ \partial t} = \frac{T^{n+1} - T^n}{\Delta t}$$

Com seus respectivos erros locais. Agora que já discretizamos todas as derivadas envolvidas na fórmula do nosso modelo, podemos discretizá-lo:


Denotando, $F = \alpha \frac{\Delta t}{\Delta r^2}$, obtemos a equação inicial discretizada, da forma:


$$ T_i^{n+1} = FT_{i-1} + (1-2F - \frac{2F}{i})T_i^n + (F+\frac{2F}{i})T_{i+1}^n$$


Discretizando a condição inicial, ficamos com:

$T_i^1 = T_1$     $\forall i \geq 1$


Discretizando as condições de contorno, temos: 


$\frac{T_{i+1}^n - T_i^n}{\Delta r} = 0$      $\forall n \geq 1$  e  $ i = 1$

ou,


$T_2^n = T_1^n$      $ \forall n \geq 1$



Analogamente, quando $ i = nx$, temos:

$\frac{T_{nx}^n - T_{nx - 1}^n}{\Delta r}= \frac{-h}{kp}[ T_{nx}^n - T_a]$


$ T_{nx}^n = \frac{T_{nx-1}^n + \frac{h}{kp} \Delta r T_a}{1 + \frac{h}{kp}\Delta r}$


## Via equações diferenciais

* A parte mais delicada na resolução via equações diferenciais ([Method of Lines](https://en.wikipedia.org/wiki/Method_of_lines)) são as condições de contorno.

* Para manter o método de segunda ordem no espaço, ao invés da aproximação de diferenças finitas pra frente feita acima, que é de primeira ordem, vamos usar aproximações de segunda ordem.


### No interior

* No interior, podemos usar diferenças centradas:
$$ \frac{\partial T_i}{\partial r} \approx \frac{T_{i+1} - T_{i-1}}{2\Delta r}, \quad i=2, \ldots, nr-1.
$$

* Assim, como $r = i\Delta r$ nos ponto da malha, obtemos
$$ \frac{2}{r}\frac{\partial T_i}{\partial r} \approx \frac{1}{i}\frac{T_{i+1} - T_{i-1}}{\Delta r^2}, \quad i=2, \ldots, nr-1
$$

* Para a segunda derivada, fazemos o clássico
$$ \frac{\partial^2 T_i}{\partial r^2} \approx \frac{T_{i+1} - 2T_i + T_{i-1}}{\Delta r^2}, \quad i=2, \ldots, nr-1.
$$


### Condição de contorno no centro do morango

* Na condição de contorno em $r=0$, associada ao índice $i$, vamos usar **diferenças para frente de segunda ordem**:
$$ \frac{\partial T_i}{\partial r} \approx \frac{-T_{i+2} + 4T_{i+1} - 3T_i}{2h}, \quad i=1.
$$

* Como queremos que $\partial_r T(r)|_{r=0} = 0$, então
$$ T_1 = \frac{4T_2 - T_3}{3}.
$$


### Condição de contorno na superfície

* Na superfície $r=R$, temos a condição de radiação
$$ -k_p \frac{\partial T(R)}{\partial r} = h (T(R) - T_a).
$$

* Agora, usamos **diferenças para trás de segunda ordem**:
$$ \frac{\partial T_i}{\partial r} \approx \frac{3T_i - 4T_{i-1} + T_{i-2}}{2\Delta r}, \quad i=nr.
$$

* Juntando, 
$$  -k_p \frac{3T_{nr} - 4T_{nr-1} + T_{nr-2}}{2\Delta r} = h (T_{nr} - T_a).
$$

* Isso nos dá
$$  -k_p (3T_{nr} - 4T_{nr-1} + T_{nr-2}) = 2h\Delta r (T_{nr} - T_a).
$$

* Resolvendo para $T_{nr}$,
$$  (2h\Delta r + 3k_p)T_{nr} = 4k_p T_{nr-1} - k_p T_{nr-2} + 2h\Delta r T_a.
$$

* Logo,
$$  T_{nr} = \frac{k_p (4T_{nr-1} - T_{nr-2}) + 2h\Delta r T_a}{2h\Delta r + 3k_p}.
$$

```julia
function resfriamento!(dTdt, T, p, t)
    α, h, kp, Ta, Δr = p 
    nr = length(T)
    T[1] = (4T[2] - T[3])/3
    T[nr] = (kp * (4T[nr-1] - T[nr-2]) + 2h * Δr * Ta)/(2h*Δr + 3kp)
    for i = 2:nr-1
        dTdt[i] = α * ((T[i+1] - T[i-1])/(i-1) + (T[i+1] - 2T[i] + T[i-1]))/Δr^2
    end
    # we don't bother to set dTdt[1] and dTdt[nr] since the values of T[1] and T[nr] are
    # defined from T[2:nr-1] and p at every step
    return nothing
end
```

```
resfriamento! (generic function with 1 method)
```



```julia
Tinit = 14.0 # temperatura inicial (uniforme) do morango em Celsius
Ta = 0.0 # temperatura ambiente em Celsius
α = 1.72*10^(-7) # difusividade térmica
h = 11 #
kp = 0.54 # 𝑊 /(𝑚 °𝐶)
R = 0.025 # raio do morango 2,5cm
nr = 45 # número de pontos da malha (i=1 corresponde a r=0, i=nr a r=R, e r=(i-1)Δr em geral
Δr = R/(nr-1) # distância entre pontos consecutivos da malha - resolução da malha
t0 = 0.0 # segundos
tfinal = 85*60.0 # segundos
dtsave = 60.0 # salvar a cada (múltiplo de) segundo
r_range = range(0.0, R, length=nr)
t_range = t0:dtsave:tfinal # minutos
nothing
```


```julia
tspan = (t0, tfinal)
p = [α, h, kp, Ta, Δr]
T0 = Tinit*ones(nr)
prob = ODEProblem(resfriamento!, T0, tspan, p, saveat=dtsave)
nothing
```


```julia
#sol = solve(prob, AutoTsit5(Rosenbrock23()))
sol = solve(prob, Tsit5())
```

```
retcode: Success
Interpolation: 1st order linear
t: 86-element Vector{Float64}:
    0.0
   60.0
  120.0
  180.0
  240.0
  300.0
  360.0
  420.0
  480.0
  540.0
    ⋮
 4620.0
 4680.0
 4740.0
 4800.0
 4860.0
 4920.0
 4980.0
 5040.0
 5100.0
u: 86-element Vector{Vector{Float64}}:
 [14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0  …  14.0, 14.0
, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0]
 [14.000258388496663, 13.999981904324619, 14.00001628873838, 13.99997966281
8605, 14.000017402927941, 13.999974533670828, 14.000017943075092, 13.999964
66132326, 14.000014621755632, 13.99994536870223  …  13.775371378641822, 13.
721151968207733, 13.658096749057831, 13.58424848911232, 13.499980512130874,
 13.403830940221376, 13.296186055058639, 13.176306516672243, 13.04459377960
1257, 12.904567279834266]
 [14.003460430197228, 13.996709496594375, 13.999895629197393, 13.9964057098
82412, 13.999512725992204, 13.99573911890841, 13.998768418459573, 13.994581
943003435, 13.997486247021532, 13.992717856907829  …  13.401630070650311, 1
3.324347252477818, 13.234414773228904, 13.141550639739645, 13.0372098573371
2, 12.928298459840086, 12.809383205310647, 12.68451769160205, 12.5513700533
83604, 12.418735646086406]
 [13.985009923097016, 13.98053049011925, 13.972536418365253, 13.97877665255
5958, 13.969852152742394, 13.975113449558641, 13.965121924031964, 13.969224
768064947, 13.957952145016526, 13.960624553397583  …  13.048390700712577, 1
2.954406952141325, 12.85950348226467, 12.75463382671921, 12.647426614495139
, 12.531690366808277, 12.4123598351457, 12.286030914485666, 12.155046258916
5, 12.019189256437869]
 [13.919071525804021, 13.903871622376512, 13.91182190776285, 13.89987573862
6562, 13.905710334784743, 13.891710334125415, 13.895234177406477, 13.879029
119988951, 13.879960102142551, 13.861315513225033  …  12.711864154304234, 1
2.617466761302607, 12.51385373941725, 12.409342666965465, 12.29698914882098
, 12.182541012431692, 12.061654736803716, 11.93761914506446, 11.80855713176
4205, 11.679961049620808]
 [13.799312976784492, 13.791423209307206, 13.778204220815871, 13.7852029114
63879, 13.768926406464937, 13.772615022238178, 13.753218340404487, 13.75336
8191027233, 13.73071809720631, 13.727033558863637  …  12.399478875693182, 1
2.29768720757054, 12.196450197941775, 12.087344844655888, 11.97752030481411
9, 11.861260529861358, 11.743124525558601, 11.619966966788676, 11.493906396
601366, 11.371626679371436]
 [13.62791403322686, 13.612571299116707, 13.617140680180507, 13.60469096334
1708, 13.605210663588196, 13.588820232466176, 13.585145653986064, 13.564742
293305752, 13.556678953892312, 13.532140150271447  …  12.097674674036053, 1
1.999070956448133, 11.89396258863859, 11.787932908280302, 11.67637894147266
3, 11.563139827303223, 11.445348458962936, 11.325193694173162, 11.201439136
23311, 11.07738117273467]
 [13.425750190057121, 13.412512372886317, 13.406779403056817, 13.4033666657
89113, 13.3930608821668, 13.384999541009956, 13.370070986787505, 13.3572622
97282332, 13.33762592032451, 13.319938616535444  …  11.811829413164995, 11.
711258346470068, 11.608450710335067, 11.501780524654828, 11.392694627930661
, 11.280111178970952, 11.164973071383182, 11.046712635837432, 10.9257997347
68978, 10.807625290649627]
 [13.192757775031586, 13.18256861452402, 13.177326399352213, 13.17259946391
6178, 13.162373018232337, 13.152612155578193, 13.137369426382302, 13.122510
730692357, 13.102197271513944, 13.082156328756954  …  11.535421814783172, 1
1.435803705418666, 11.333904796392632, 11.228686750490107, 11.1211024564044
54, 11.010467418295836, 10.897409064609358, 10.7815770558344, 10.6632934468
0971, 10.543703529211037]
 [12.95008049782331, 12.932952022615055, 12.935707409497345, 12.92249464410
556, 12.919941952227191, 12.901550307749051, 12.893618300474047, 12.8700613
52173614, 12.856667211955196, 12.827944980293514  …  11.267379820594778, 11
.170674011391982, 11.068729471845705, 10.966359198021415, 10.85960721220222
8, 10.751773607141752, 10.640389074449878, 10.527325342232585, 10.411507270
239586, 10.297491034410728]
 ⋮
 [2.77489432299625, 2.7737768086253367, 2.7706964724330954, 2.7711329030309
46, 2.76675406396979, 2.7658496975678646, 2.760190747059642, 2.757936393092
004, 2.75101755385411, 2.747406764441788  …  2.3867089090380738, 2.36490586
8401654, 2.343422114137421, 2.320777268148669, 2.2982298762839526, 2.274774
6071422372, 2.251208437578492, 2.2269744669921345, 2.202436862380082, 2.177
4716462383648]
 [2.7130474698079055, 2.709239155215498, 2.7102344657571598, 2.706668944578
8628, 2.706359854244027, 2.7015328470148874, 2.6999096624320518, 2.69383950
22679353, 2.690895113370202, 2.6836018507673973  …  2.332458049614666, 2.31
197700324449, 2.2902649192365505, 2.268728053026914, 2.2462037612436294, 2.
223653397423862, 2.2003479954665526, 2.176828937354056, 2.1527739190827497,
 2.128940139745919]
 [2.65257905971959, 2.649967867859492, 2.6473341343787022, 2.64744291456911
85, 2.6435658498061074, 2.642397394636235, 2.6372924339680894, 2.6348400714
40494, 2.6285244611442167, 2.6247840652992007  …  2.280275824514073, 2.2595
088693378265, 2.238927836222339, 2.217338615924251, 2.19575892126265, 2.173
378318231012, 2.150841837698092, 2.127701224617538, 2.104252049199367, 2.08
1490303849773]
 [2.591835076467605, 2.588932549650635, 2.5889438873467143, 2.5864736133676
987, 2.58524694895482, 2.5815599135524936, 2.5790924754616134, 2.5741997877
45119, 2.5704910864923267, 2.564405722361426  …  2.2285821731834146, 2.2088
19390222702, 2.1882423687368884, 2.1675254792765934, 2.146119112299364, 2.1
24485820087698, 2.102282809473273, 2.0797726846661613, 2.0568065870939427, 
2.033824223580246]
 [2.5340682486807196, 2.530899553285331, 2.5302479335243913, 2.528493720261
8325, 2.5266378258734337, 2.5236861623703786, 2.5206278614382827, 2.5164850
876965783, 2.5122283477166754, 2.506902787821008  …  2.1784147224684633, 2.
1589600958232325, 2.138964849037702, 2.118616166530169, 2.0977726462489517,
 2.0765648349174053, 2.054907115018798, 2.03287657070925, 2.010439896511924
6, 1.9884943320156017]
 [2.476038159781942, 2.4744481860930923, 2.472602604045142, 2.4720923389211
515, 2.469080242403731, 2.467384713876329, 2.463216276818566, 2.46033344070
7413, 2.455020649788625, 2.450950691943072  …  2.1294388869672507, 2.110172
2965666707, 2.0908428274323887, 2.070772629324113, 2.0505453891970338, 2.02
97022090283607, 2.0086143505360874, 1.9870296012360644, 1.965120034635647, 
1.94295785734113]
 [2.420852214126399, 2.417399428570823, 2.418121922925611, 2.41510557776939
37, 2.4146656750382873, 2.410521741356935, 2.4089119362058304, 2.4036556427
560702, 2.400870702016694, 2.3945188497056735  …  2.0811522758246666, 2.062
8437560555666, 2.0435006191135563, 2.024259674144593, 2.004182445209716, 1.
9840463556421908, 1.9632633085049807, 1.942271479864354, 1.9208113257953492
, 1.899653196104453]
 [2.3668962543076506, 2.364678500831641, 2.3618357508328485, 2.362423879899
8194, 2.358476094965201, 2.357918573937881, 2.352882929980772, 2.3511704455
716833, 2.34506563669636, 2.3421912658354076  …  2.034629073872424, 2.01599
7618385202, 1.9977218717299456, 1.9783854111981747, 1.9591906307658125, 1.9
391752872157657, 1.9191004050434355, 1.8984324735906568, 1.8775186480995891
, 1.8573137093567222]
 [2.311101281044, 2.3106523736053335, 2.3093056512893337, 2.308453617260783
, 2.306014200525435, 2.3040598880537364, 2.3005346754238807, 2.297478744936
398, 2.2928764024494446, 2.2887215063300634  …  1.9886014276891015, 1.97068
68336317083, 1.9525683684605806, 1.933881384392183, 1.914945902188438, 1.89
55162244205699, 1.8757972219452907, 1.8556554841788293, 1.8351879086153293,
 1.8143656484854787]
```



```julia
p = plot(title="Evolução temporal em tempos selecionados", titlefont=10,
    xaxis="raio (m)", yaxis="temperatura (graus Celsius)", legend=:false)
for j in 1:5:length(sol.u)
    plot!(p, r_range, sol.u[j])
end
display(p)
```

\fig{images/1208-Resfriamento_rapido_morangos_6_1.png}

```julia
p = plot(title="Evolução temporal em raios selecionados", titlefont=10,
    xaxis="tempo (minutos)", yaxis="temperatura (graus Celsius)", legend=:bottomleft)
for i in (2, div(nr,3), 2*div(nr,3), nr-1)
    scatter!(p, t_range ./ 60, getindex.(sol.u, i), label="r=$(round((i-1)*Δr, digits=4))")
end
display(p)
```

\fig{images/1208-Resfriamento_rapido_morangos_7_1.png}
