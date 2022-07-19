
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
 [14.000258388451641, 13.999981904226095, 14.000016288842643, 13.9999796627
04522, 14.000017403056342, 13.999974533523046, 14.00001794324806, 13.999964
661118414, 14.000014622000093, 13.99994536840923  …  13.775371375315927, 13
.721151971265225, 13.658096746324523, 13.584248491472367, 13.49998051018439
3, 13.40383094172422, 13.296186054017914, 13.17630651724449, 13.04459377949
1402, 12.904567281252325]
 [14.00346042454735, 13.996709500672281, 13.999895625090675, 13.99640571403
6761, 13.999512721771973, 13.995739123211973, 13.998768414056292, 13.994581
947521535, 13.997486242375055, 13.99271786169446  …  13.40163007439435, 13.
324347249165749, 13.234414776092235, 13.14155063733686, 13.037209859272634,
 12.928298458373238, 12.80938320631262, 12.684517691055863, 12.551370053487
942, 12.418735648698602]
 [13.98500991323561, 13.980530478836151, 13.972536429650457, 13.97877664126
7656, 13.969852164034174, 13.975113438263836, 13.96512193532826, 13.9692247
56769957, 13.957952156305947, 13.960624542119577  …  13.048390696458505, 12
.95440695586075, 12.859503479081805, 12.754633829366975, 12.647426612377542
, 12.531690368404007, 12.412359834060192, 12.286030915075767, 12.1550462588
03889, 12.019189258926277]
 [13.919071528354403, 13.903871621442741, 13.911821908695025, 13.8998757376
9705, 13.905710335710506, 13.891710333204479, 13.895234178321466, 13.879029
119081023, 13.879960103042274, 13.861315512334679  …  12.711864154051812, 1
2.617466761522097, 12.513853739230303, 12.409342667120344, 12.2969891486975
18, 12.182541012524476, 12.06165473674072, 11.937619145098658, 11.808557131
757688, 11.679961049814679]
 [13.799312975164277, 13.79142321229369, 13.778204217836162, 13.78520291443
23, 13.768926403512294, 13.77261502517055, 13.753218337496843, 13.753368193
905729, 13.730718094361343, 13.727033561670732  …  12.399478876412342, 12.2
97687206946538, 12.1964501984722, 12.08734484421713, 11.977520305163361, 11
.86126052959915, 11.743124525736459, 11.619966966692132, 11.493906396619751
, 11.37162668016533]
 [13.627914037333099, 13.612571297796256, 13.617140681497645, 13.6046909620
30066, 13.60521066489217, 13.588820231172033, 13.585145655268244, 13.564742
292037643, 13.55667895514429, 13.532140149037634  …  12.09767467373369, 11.
999070956710213, 11.893962588415995, 11.787932908464274, 11.676378941326309
, 11.563139827413027, 11.44534845888847, 11.32519369421355, 11.201439136225
392, 11.077381172698649]
 [13.425750190073698, 13.412512374089085, 13.406779401857143, 13.4033666669
8362, 13.39306088097949, 13.384999542188028, 13.370070985620657, 13.3572622
9843598, 13.33762591918598, 13.319938617656968  …  11.81182941343538, 11.71
1258346235775, 11.608450710533972, 11.501780524490467, 11.392694628061369, 
11.28011117887289, 11.164973071449667, 11.046712635801358, 10.9257997347758
58, 10.807625291161743]
 [13.192757777188538, 13.182568614626831, 13.177326399249674, 13.1725994640
18262, 13.16237301813087, 13.152612155678856, 13.137369426282605, 13.122510
730790905, 13.102197271416689, 13.082156328852733  …  11.53542181480611, 11
.435803705398795, 11.333904796409495, 11.228686750476186, 11.12110245641553
3, 11.010467418287528, 10.897409064615001, 10.781577055831352, 10.663293446
8103, 10.543703529421519]
 [12.950080499252385, 12.932952020832307, 12.935707411275393, 12.9224946423
35298, 12.919941953986566, 12.901550306003598, 12.893618302202556, 12.87006
1350464987, 12.856667213641028, 12.82794497863327  …  11.267379820198418, 1
1.170674011735343, 11.068729471554255, 10.966359198262198, 10.8596072120107
72, 10.751773607285376, 10.640389074352509, 10.527325342285405, 10.41150727
0229512, 10.297491034705622]
 ⋮
 [2.7748943235025165, 2.7737768087960335, 2.7706964722628515, 2.77113290320
04413, 2.7667540638013413, 2.76584969773498, 2.760190746894155, 2.757936393
255581, 2.751017553692723, 2.7474067646007176  …  2.3867089090759417, 2.364
9058683688473, 2.343422114165264, 2.320777268125665, 2.2982298763022415, 2.
274774607128516, 2.2512084375877897, 2.226974466987091, 2.202436862381041, 
2.177471646274145]
 [2.7130474707921994, 2.70923915523857, 2.7102344657341453, 2.7066689446017
73, 2.706359854221258, 2.7015328470374733, 2.6999096624096843, 2.6938395022
90044, 2.6908951133483865, 2.6836018507888766  …  2.3324580496197815, 2.311
9770032400533, 2.29026491924031, 2.268728053023801, 2.2462037612460968, 2.2
236533974220034, 2.2003479954678067, 2.17682893735337, 2.1527739190828763, 
2.1289401397183765]
 [2.6525790605437902, 2.6499678682864682, 2.6473341339528464, 2.64744291499
30967, 2.6435658493847356, 2.642397395054256, 2.6372924335541312, 2.6348400
71849666, 2.6285244607405125, 2.6247840656967476  …  2.2802758246087977, 2.
259508869255765, 2.238927836291984, 2.2173386158667086, 2.195758921308398, 
2.1733783181966877, 2.1508418377213525, 2.127701224604911, 2.10425204920176
7, 2.0814903038404977]
 [2.591835076464743, 2.588932549041229, 2.588943887954504, 2.58647361276257
4, 2.5852469495562067, 2.5815599129558775, 2.5790924760524128, 2.5741997871
611324, 2.5704910870684956, 2.56440572179403  …  2.228582173048213, 2.20881
93903398117, 2.188242368637477, 2.167525479358709, 2.1461191122340635, 2.12
44858201366723, 2.102282809440063, 2.0797726846841695, 2.056806587090507, 2
.033824223674462]
 [2.534068248545927, 2.5308995545450808, 2.530247932267954, 2.5284937215127
323, 2.526637824630236, 2.5236861636036902, 2.5206278602169663, 2.516485088
903785, 2.512228346525604, 2.5069027889939233  …  2.1784147227479473, 2.158
96009558112, 2.1389648492431927, 2.1186161663604013, 2.0977726463839295, 2.
076564834816145, 2.054907115087437, 2.032876570672006, 2.010439896519016, 1
.9884943321245807]
 [2.476038159453711, 2.4744481853622067, 2.4726026047740928, 2.472092338195
403, 2.469080243124999, 2.467384713160784, 2.463216277527139, 2.46033344000
7013, 2.455020650479649, 2.4509506912625687  …  2.1294388868050924, 2.11017
2296707132, 2.09084282731316, 2.0707726294225997, 2.0505453891187155, 2.029
7022090871013, 2.008614350496256, 1.9870296012576647, 1.9651200346315234, 1
.9429578574727175]
 [2.4208522148049574, 2.4173994287561893, 2.418121922740732, 2.415105577953
4554, 2.4146656748553568, 2.4105217415384077, 2.4089119360261204, 2.4036556
42933702, 2.4008707018414346, 2.3945188498782604  …  2.0811522758657888, 2.
06284375601994, 2.0435006191437903, 2.0242596741196106, 2.0041824452295756,
 1.9840463556272891, 1.9632633085150784, 1.942271479858872, 1.9208113257963
904, 1.8996531961053986]
 [2.366896253747342, 2.3646785007744215, 2.3618357508899157, 2.362423879842
997, 2.3584760950216688, 2.357918573881856, 2.352882930036247, 2.3511704455
16845, 2.3450656367504603, 2.3421912657821244  …  2.0346290738597235, 2.015
9976183962014, 1.997721871720605, 1.9783854112058852, 1.9591906307596783, 1
.9391752872203627, 1.9191004050403153, 1.8984324735923477, 1.87751864809926
63, 1.8573137095140153]
 [2.3111012805184696, 2.310652373289847, 2.3093056516039794, 2.308453616947
5127, 2.306014200836766, 2.304059887744871, 2.300534675729732, 2.2974787446
340685, 2.29287640274772, 2.2887215060363233  …  1.9886014276191049, 1.9706
868336923347, 1.952568368409114, 1.933881384434693, 1.9149459021546298, 1.8
955162244459234, 1.8757972219280952, 1.8556554841881496, 1.8351879086135485
, 1.8143656484800392]
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
