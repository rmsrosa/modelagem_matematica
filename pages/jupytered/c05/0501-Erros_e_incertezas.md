
@def title = "Erros e incertezas"

# {{ get_title }}

* Na prática, qualquer medição está sujeita a erros e incertezas.

* Como podemos estimar esses fatores?

* Qual a consequência desses fatores numa modelagem?

* Qual o grau de incerteza que isso acarreta nas previsões do modelo?

```julia
using Distributions
using Plots
using Random
```



### Os conceitos de erro e incerteza

* É importante deixar clara a diferença entre esses dois conceitos.

* O **erro** é a diferença entre o valor de uma medição e o valor exato da quantidade que queremos medir.

* A **incerteza** é uma quantificação da dúvida que temos sobre a medida feita.

* Podemos saber, por exemplo, que um determinado termômetro está descalibrado e mede sempre dois grau acima do padrão e podemos corrigir esse *erro*.

* Mas qualquer erro sobre o qual não sabemos a medida é uma fonte de *incerteza*.

* Erros e incertezas podem se referir a medições experimentais de quantidades físicas ou a resultados de qualquer tipo de cálculo feito.


### Representando incertezas em medições

* É comum representarmos a incerteza na medição de uma quantidade $q$ na forma
$$ q = \bar q \pm \Delta q.
$$

* Isso é, por exemplo, resultado de uma série de medidas, de onde obtemos o **valor médio** $\bar q$ e uma **margem de confiança** $\Delta q$.

* A margem de confiança nos dá um **intervalo de confiança**
$$ [\bar q - \Delta q, \bar q + \Delta q].
$$

* Associado a isso, temos, ainda, o **nível de confiança** associado a esse intervalo.

* Dependendo da distribuição de probabilidade que consideramos em relação à incerteza nas medições, o intervalo de incerteza pode não ser simétrico em relação à média.

* Mais geralmente, podemos considerar $\Delta q$ como uma variável aleatória, com média zero, representando a incerteza em relação ao valor médio $\bar q$.

* Em geral, a margem de confiança é determinada pelo *erro padrão* da amostra, mas vale ressaltar que, em alguns casos, essa margem é dada, simplesmente, em termos do *desvio padrão*.


### Informações das medições

* Essas informações são obtidas através de uma série de $N$ medições
$$ q_1, q_2, \ldots, q_N.
$$

* Delas, podemos tirar o valor médio
$$ \bar q = \frac{q_1 + \ldots + q_N}{N}.
$$

* Assim como a variância e o desvio padrão, mas, nesse caso, costumamos considerar o **desvio padrão corrigido** (observe a divisão por $N-1$, ao invés de $N$)
$$ s_q = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (q_i - \bar q)^2}.
$$

* O desvio padrão corrigido é importante para a estimativa do intervalo e do nível de confiança, que veremos mais pra frente.


### A probabilidade por detrás da incerteza

* A distribuição de probabilidades da incerteza é desconhecida.

* Os dados $q_i, \ldots, q_N$ nos dão apenas uma visão parcial desta distribuição.

* Quanto mais dados, melhor, mas nunca saberemos exatamente essa distribuição.

* De qualquer forma, dada uma distribuição de probabilidades $\mathcal{P}$ e interpretando $q$ como variável aleatória associada a $\mathcal{P}$, podemos falar da **média**, ou **valor esperado**, de $q$ e denotá-la por
$$ E(q).
$$

* A **variância** e o **desvio padrão** são denotados por $\operatorname{Var}(q)$ e $\sigma$.

* Não custa ressaltar que a média $\mu$ da distribuição de probabilidades desconhecida pode ser, e geralmente é, diferente da média $\bar q$ da "pequena" amostra que temos.


### Média, variância e desvio padrão

* Se, mais precisamente, o espaço da distribuição é $X$ e a medidade de probabilidade é $\rho$, então a *média*, a *variância* e o *desvio padrão* são dados por
$$ \mu = E(q) = \int_X q\;d\rho(q), \quad \operatorname{Var}(q) = E((q-\mu)^2) = \int_X (q - \mu))^2 \;d\rho(q), \quad \sigma = \sqrt{\operatorname{Var}(q)}.
$$

* Se o espaço de probabilidades $X$ é um subconjunto de $\mathbb{R^n}$ e $f=f(q)$ é a função densidade de probabilidades de $\mathcal{P}$, então também podemos escrever
$$ \mu = E(q) = \int_X q f(q)\;dq, \quad \operatorname{Var}(q) = E((q-\mu)^2) = \int_X (q - \mu)^2f(q) \;dq, \quad \sigma = \sqrt{\operatorname{Var}(q)}.
$$


### Intervalo de confiança

* A ideia é termos uma estimativa de um intervalo de confiança em torno da média $\bar q$ que nos dê, de acordo com um nível pré-definido de confiança, a probabilidade de que a média "real" $E(q)$ esteja nesse intervalo.

* Esse intervalo **não** é a probabilidade do conjunto de dados estar no intervalo. Ela diz respeito à localização da média $E(q)$. É muito importante ressaltar isso.

* Essa estimativa é dada pelo **erro padrão da amostra**
$$ \Delta q = \frac{s_q}{\sqrt{N}}.
$$

* A relação disso com a intervalo e nível de confiança é estabelecida pelo **Teorema Central do Limite**.


### Visualizando intervalos de confiança

```julia
Random.seed!(1100)
N = 10
M = 10
amostras = rand(Normal(), M, N)
vline([0.0], xlims=(-4,4), ylims=(0,M+1), yticks=1:M, label=false, titlefont=10,
    color=:black, title="Dados, média real e intervalos de 68% e 95% de cada amostra de $N dados")
for j = 1:M
    q̄ = mean(amostras[j,:])
    Δ_q = std(amostras[j,:])/√N
    plot!([q̄-Δ_q, q̄+Δ_q], [j+0.1, j+0.1], label=false, color=2)
    plot!([q̄-2Δ_q, q̄+2Δ_q], [j-0.1, j-0.1], label=false, color=3)
    scatter!(amostras[j,:], [j], markersize = 2, color = 5, label = false)
end
plot!()
```

\fig{images/0501-Erros_e_incertezas_2_1.png}


### O Teorema Central do Limite

* Considere uma distribuição de probabilidades qualquer, como na situação descrita anteriormente.

* Suponha que retiremos uma coleção de amostras a partir dessa distribuição, com cada amostra contendo $N$ dados cada, com as amostras e os dados escolhidos de forma aleatória e independente.

* Tome a média aritmética de cada uma dessas amostras, que denotamos, aqui, por $\bar q_N$, para explicitar a dependência em $N$.

* Então, o **Teorema Central do Limite** garante que 

> A distribuição de probabilidades dessas médias $\bar q_N$ se aproxima de uma normal, conforme $N$ aumenta.


### Mais precisamente

* Sejam $\mu$ e $\sigma$ a média e o desvio padrão da distribuição de probabilidades desconhecida $\mathcal{P}$.

* Seja $\mathcal{Q}_N$ a distribuição de probabilidades das médias das amostras.

* Então, temos a convergência (quase sempre e em probabilidade)
$$ \sqrt{N}(\mathcal{Q}_N - \mu) \rightarrow \mathcal{N}(0,\sigma^2).
$$

* Isso significa que a distribuição de probabilidades $\mathcal{S}_N$ das médias $\bar q_N$ está cada vez mais próxima de uma normal com média $\mu$ e desvio padrão $\sigma/\sqrt{N}$, i.e. 
$$ \mathcal{Q}_N \sim \mathcal{N}\left(\mu,\frac{\sigma^2}{N}\right).
$$

* Observe que esse desvio padrão $\sigma/\sqrt{N}$ é semelhante ao erro $\Delta q_N$ que mencionamos acima.


### Aproximação prática e a correção de Bessel

* No caso de $N$ ser "grande o suficiente", o desvio padrão $\sigma/\sqrt{N}$ é relativamente pequeno e há grandes chances de uma amostra arbitrária ter média $\bar q_N$ muito próxima de $\mu$ e desvio padrão (sem correção) $\sigma_N$ próximo de $\sigma$.

* Nesse caso, é natural pensarmos em usar a aproximação
$$ \mathcal{Q}_N \sim \mathcal{N}\left(\bar q_N,\frac{\sigma_N^2}{N}\right).
$$

* Porém, o desvio padrão não corrigido $\sigma_N$ tende a estimar por baixo o desvio padrão $\sigma$, a menos que $\bar q_N$ coincida com $\mu$.

* Por esse motivo, usa-se a o desvio padrão corrigido da amostra:
$$ s_q = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (q_i - \bar q_N)^2}.
$$

* Esta correção é conhecida como **correção de Bessel**. Veja mais informações sobre isso em [Bessel's correction](https://en.wikipedia.org/wiki/Bessel%27s_correction).

* A correção de Bessel evita essa distorção tendenciosa, o que nos leva a uma aproximação melhor pela normal com desvio padrão dado pelo erro padrão $\Delta q = s_q/\sqrt{N}$ da amostra:
$$ \mathcal{Q}_N \sim \mathcal{N}\left(\bar q_N, \Delta q_N \right).
$$

* Associado a isso, temos, também, uma certa redundância no uso do desvio padrão não corrigido da amostra, já que podemos encontrar o valor de uma das amostras a partir da média e das $N-1$ amostras restantes.

* Ou seja, conhecendo-se $\bar q_N$, o conjunto $q_1 - \bar q_N, \ldots, q_N-\bar q_N$ possui apenas $N-1$ graus de liberdade.


### Interlúdio sobre a distribuição normal

* Uma normal $\mathcal{N}(\mu, \sigma^2)$ é uma distribuição caracterizada por uma média $\mu$ e um desvio padrão $\sigma$ e associada à função densidade de probabilidades
$$ f_{\mu, \sigma^2}(q) = \frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}e^{\displaystyle -\frac{(q-\mu)^2}{2\sigma^2}}.
$$

* O desvio padrão nos dá uma ideia da "dispersão" dos dados retirados aleatoriamente a partir dessa distribuição.

* O intervalo $I_{68\%} = [\mu - \sigma, \mu + \sigma]$ tem medida de probabilidade de 68\% *(aproximadamente)*. Ou seja, esperamos que 68\% dos dados da amostra estejam dentro desse intervalo.

* E o intervalo $I_{95\%} = [\mu - 2\sigma, \mu + 2\sigma]$ corresponde a 95\% de probabilidade *(aproximadamente)*.

* São esses intervalos de probabilidade que nos darão os intervalos de confiança, quando devidamente interpretados e aplicados nas informações retiradas dos dados.

```julia
intervalos = Dict("68%" => [0.16, 0.84], "95%" => [0.025, 0.975], "99%" => [0.005, 0.995])
for (k, int) in intervalos
    println("Normal IC $k: ", round.(quantile.(Normal(), int), digits=3))
end
println()
for α in (1,2,3)
    println("Nível de confiança em [μ-$(α)σ, μ+$(α)σ]: ", round(100*(cdf(Normal(), α) - cdf(Normal(), -α)), digits=2), "%")
end
```

```
Normal IC 68%: [-0.994, 0.994]
Normal IC 95%: [-1.96, 1.96]
Normal IC 99%: [-2.576, 2.576]

Nível de confiança em [μ-1σ, μ+1σ]: 68.27%
Nível de confiança em [μ-2σ, μ+2σ]: 95.45%
Nível de confiança em [μ-3σ, μ+3σ]: 99.73%
```



```julia
plot(-3.0:0.1:3.0, x -> pdf(Normal(), x), fill=true, color=3, label="99%")
plot!(-2.0:0.1:2.0, x -> pdf(Normal(), x), fill=true, color=2, label="95%")
plot!(-1.0:0.1:1.0, x -> pdf(Normal(), x), fill=true, color=1, label="68%")
plot!([(0.0, 0.0), (0.0, 0.4)], color=7, label="valor médio")
plot!(-4.0:0.1:4.0, x -> pdf(Normal(), x), color=1, ylims = (0,0.5),
    label = "Gaussiana", title="Distribuição normal", titlefont=10, size=(600,300))
```

\fig{images/0501-Erros_e_incertezas_4_1.png}


### Supondo distribuição das médias amostrais como sendo uma normal

* Supondo, então, que $\mathcal{Q}_N$, que converge para $\mathcal{N}(\mu,\sigma^2/N)$, seja bem aproximado pela normal $\mathcal{N}(\bar q_N, \Delta q_N)$, como indicado acima, temos os intervalos de $68\%$ e $95\%$ de probabilidade dados por
$$ I_{68\%} = \left[\bar q_N - \Delta q_N, \bar q_N + \Delta q_N\right], \qquad I_{95\%} = \left[\bar q_N - 2\Delta q_N, \;\bar q_N + 2\Delta q_N\right]
$$

* Esses intervalos estão associados à porcentagem de amostras baseadas nessa normal estaram em cada intervalo.

* Mas, baseado no Teorema Central do Limite, vamos interpretá-los como intervalos de confiança para a localização da média "real" da probabilidade desconhecida.


* De fato, se 
$$\bar q_N \in \left[\mu - \sigma/\sqrt{N}, \mu + \sigma/\sqrt{N}\right],
$$
com 68\% de probabilidade e 
$$\sigma/\sqrt{N} \approx \Delta q_N,
$$
então, equivalentemente,
$$\mu \in  I_{68\%} = \left[\bar q_N - \Delta q_N, \bar q_N + \Delta q_N\right]
$$
com 68\% de probabilidade.

* Analogamente para o intervalo de 95\% e outros de diferentes níveis.


### Visualizando essa convergência

* Vamos visualizar tanto a convergência dos parâmetros, através dos intervalos de confiança de determinadas amostras.

* Como do histograma das amostras.

```julia
Random.seed!(1100)
N = 10 # tamanho da amostra
amostra = rand(Normal(), N)
q̄ = mean(amostra)
Δ_q = std(amostra)/√N
nothing
```


```julia
plot(-4.0:0.1:4.0, x -> pdf(Normal(), x), color=1, ylims=(0.0,0.5),
    label = "normal", title="Distribuição normal, amostra com $N dados e intervalos de confiança",
    titlefont=10, size=(600,300))
scatter!(amostra, fill(0.01, length(amostra)), label="amostra", color=2)
plot!([(0.0, 0.0), (0.0, 0.4)], color=:black, label="média da normal")
plot!([(mean(amostra), 0.0), (mean(amostra), 0.4)], color=3, label="média da amostra")
plot!([q̄ - Δ_q, q̄ + Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(amostra, nbins=div(N,4), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_6_1.png}

```julia
Random.seed!(1101)
N = 30 # tamanho da amostra
amostra = rand(Normal(), N)
q̄ = mean(amostra)
Δ_q = std(amostra)/√N
nothing
```


```julia
plot(-4.0:0.1:4.0, x -> pdf(Normal(), x), color=1, ylims=(0.0,0.5),
    label = "normal", title="Distribuição normal, amostra com $N dados e intervalos de confiança",
    titlefont=10, size=(600,300))
scatter!(amostra, fill(0.01, length(amostra)), label="amostra", color=2)
plot!([(0.0, 0.0), (0.0, 0.4)], color=:black, label="média da normal")
plot!([(mean(amostra), 0.0), (mean(amostra), 0.4)], color=3, label="média da amostra")
plot!([q̄ - Δ_q, q̄ + Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(amostra, nbins=div(N,4), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_8_1.png}

```julia
Random.seed!(1102)
N = 80 # tamanho da amostra
amostra = rand(Normal(), N)
q̄ = mean(amostra)
Δ_q = std(amostra)/√N
nothing
```


```julia
plot(-4:0.1:4, x -> pdf(Normal(), x), color=1, ylims=(0.0,0.5),
    label = "normal", title="Distribuição normal, amostra com $N dados e intervalos de confiança",
    titlefont=10, size=(600,300))
scatter!(amostra, fill(0.01, length(amostra)), label="amostra", color=2)
plot!([(0.0, 0.0), (0.0, 0.4)], color=:black, label="média da normal")
plot!([(mean(amostra), 0.0), (mean(amostra), 0.4)], color=3, label="média da amostra")
plot!([q̄ - Δ_q, q̄ + Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], [0.4, 0.4], fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(amostra, nbins=div(N,4), normed=true, alpha=0.1, color=6)
```

\fig{images/0501-Erros_e_incertezas_10_1.png}


* Agora vamos ver a distribuição das médias.

* Vamos considerar $M$ amostras de tamanho $N$ cada uma.

```julia
N = 20 # tamanho da amostra
M = 60 # número de amostras
Random.seed!(1103)
amostras = rand(Normal(), M, N)
```

```
60×20 Matrix{Float64}:
  0.799348     0.20791    -0.170405   1.26359    …   0.964578      1.89379
 -1.39213      0.642281   -0.987824  -0.628011      -2.21208      -1.00836
  0.582623     0.415104    0.286626   0.114355      -0.785345     -0.52225
 -0.245211    -0.468066   -1.46418   -1.2937        -0.643979      0.085169
3
 -0.761368    -0.374904    0.110974  -1.30868       -0.782819      0.057579
8
 -0.210854    -0.0961505  -0.928848  -0.597348   …   0.362123      0.514072
  1.30296      0.132299    1.18508    1.2904        -0.586768      0.182874
 -1.77842      0.465431    0.939865   1.0112         0.974272      0.544624
 -2.38518      2.12399     0.747776  -0.321939      -0.446558     -0.016155
1
 -0.0112433   -1.66675     1.72668    0.718032      -2.10129      -0.413562
  ⋮                                              ⋱                
 -0.00487551  -0.222441   -1.07975    0.197995       0.674944     -0.759032
  1.23964      1.11783     0.588545  -0.0869135     -0.000264553  -0.644438
  0.499396     0.857094    1.25981   -0.982301      -0.659761     -1.35156
  0.935807    -1.43135    -0.84169    1.05412        0.779386      1.34203
 -1.3613      -0.826226   -1.48195    1.40269    …   1.33154       0.52888
 -1.40565     -1.85712    -2.02624   -1.1233         1.30034       0.205086
  1.11805     -1.72978    -1.11944   -0.229144      -0.830644     -0.471012
  0.820639    -1.78785     0.146873   0.0538482     -0.279972     -1.45809
  0.253882    -0.869198    1.23868    0.152523       0.00479686   -1.03374
```



```julia
medias = mean(amostras, dims=2)
```

```
60×1 Matrix{Float64}:
  0.2570352304601996
 -0.4499356254204473
  0.21741842451005358
  0.1503790225787346
 -0.4019443229638287
 -0.4175022524924229
  0.10567719967114722
  0.359596715466307
 -0.1035565169968442
 -0.11014719833425764
  ⋮
  0.2538253937369993
  0.05258785942216684
 -0.22618992267622037
  0.28835809844737026
  0.003351643225821721
 -0.40075591346438005
 -0.41950183044792116
 -0.13661263675668017
 -0.03738715575549284
```



```julia
plot(-4.0:0.01:4.0, x -> pdf(Normal(0.0, 1.0/N), x), color=1, ylims=(0.0,1.1*pdf(Normal(0.0, 1.0/N), 0)),
    label="normal limite", title="Distribuição normal limite das médias, média das amostra e intervalos de confiança",
    titlefont=8, size=(600,300))
scatter!(medias, fill(0.08, length(medias)), label="médias das amostra", color=2)
vline!([0.0], color=:black, label="média da normal")
vline!([mean(medias)], color=3, label="média das médias")
histogram!(medias, nbins=div(M,4), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_13_1.png}


Ampliando o eixo $x$ ("zoom...")

```julia
plot(-0.6:0.01:0.6, x -> pdf(Normal(0.0, 1.0/N), x), color=1, ylims=(0.0,1.1*pdf(Normal(0.0, 1.0/N), 0)),
    label="normal limite", title="Distribuição normal limite das médias, média das amostra e intervalos de confiança",
    titlefont=8, size=(600,300))
scatter!(medias, fill(0.08, length(medias)), label="médias das amostra", color=2)
vline!([0.0], color=:black, label="média da normal")
vline!([mean(medias)], color=3, label="média das médias")
histogram!(medias, nbins=div(M,4), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_14_1.png}


### Intervalos de confiança

```julia
vline([0.0], xlims=(-4,4), ylims=(0,M+1), yticks=1:M, label=false, titlefont=10,
    color=:black, title="Média real e intervalos de 68% e 95% de cada amostra")
acertos68 = 0
acertos95 = 0
for j = 1:M
    q̄ = mean(amostras[j,:])
    Δ_q = std(amostras[j,:])/√N
    acertos68 += q̄ - Δ_q ≤ 0 ≤ q̄ + Δ_q
    acertos95 += q̄ - 2Δ_q ≤ 0 ≤ q̄ + 2Δ_q
    plot!([q̄-Δ_q, q̄+Δ_q], [j+0.1, j+0.1], label=false, color=2)
    plot!([q̄-2Δ_q, q̄+2Δ_q], [j-0.1, j-0.1], label=false, color=3)
end
plot!()
```

```
Error: UndefVarError: acertos68 not defined
```



```julia
println("Acertos do intervalo de confiança de 68%: $acertos68 de $M ($(round(100*acertos68/M, digits=1))%)")
println("Acertos do intervalo de confiança de 95%: $acertos95 de $M ($(round(100*acertos95/M, digits=1))%)")
```

```
Acertos do intervalo de confiança de 68%: 0 de 60 (0.0%)
Acertos do intervalo de confiança de 95%: 0 de 60 (0.0%)
```



```julia
M̄ = div(M,3)
vline([0.0], xlims=(-4,4), ylims=(0,M̄+1), yticks=1:M̄, label=false, titlefont=10,
    color=:black, title="Média real e intervalos de 68% e 95% de cada amostra")
for j = 1:M̄
    q̄ = mean(amostras[j,:])
    Δ_q = std(amostras[j,:])/√N
    plot!([q̄-Δ_q, q̄+Δ_q], [j+0.1, j+0.1], label=false, color=2)
    plot!([q̄-2Δ_q, q̄+2Δ_q], [j-0.1, j-0.1], label=false, color=3)
end
plot!()
```

\fig{images/0501-Erros_e_incertezas_17_1.png}


## Exemplos com outras distribuições "desconhecidas"

* Como visto no Teorema Central do Limite, a distribuição das médias das amostras se aproxima de uma normal, independentemente da distribuição associada ao mecanismo de geração de dados.

* Vejamos, então, alguns exemplos com outras distribuições.


### Distribuição desconhecida beta

```julia
N = 10
M = 20
distribuicao = Beta(2,5)
intervalo = 0:0.01:1.5
Random.seed!(1102)
amostras = rand(distribuicao, M, N)
medias = mean(amostras, dims=2)
q̄ = mean(amostras[1,:])
Δ_q = std(amostras[1,:])/√N
nothing
```


```julia
plot(intervalo, x -> pdf(distribuicao, x), color=9, xlims=(minimum(intervalo), maximum(intervalo)),
    label="distribuição desconhecida",
    title="Distribuição desconhecida $distribuicao, normal limite,\nmédia das amostra e intervalos de confiança",
    titlefont=8, size=(600,300))
plot!(intervalo, x -> pdf(Normal(q̄, Δ_q), x), color=1, label="normal limite estimada")
scatter!(reshape(amostras,:,1), fill(pdf(distribuicao,q̄)/15, prod(size(amostras))), label="amostras", color=3, alpha=0.02)
scatter!(medias, fill(pdf(distribuicao,q̄)/15, length(medias)), label="médias das amostras", color=2)
plot!([q̄ - Δ_q, q̄ + Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(medias, nbins=div(M,2), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_19_1.png}


### Distribuição desconhecida Chi-square

```julia
N = 10
M = 20
distribuicao = Chisq(3)
intervalo = 0:0.01:10
Random.seed!(1102)
amostras = rand(distribuicao, M, N)
medias = mean(amostras, dims=2)
q̄ = mean(amostras[1,:])
Δ_q = std(amostras[1,:])/√N
nothing
```


```julia
plot(intervalo, x -> pdf(distribuicao, x), color=9, xlims=(minimum(intervalo), maximum(intervalo)),
    label="distribuição desconhecida",
    title="Distribuição desconhecida $distribuicao, normal limite,\nmédia das amostra e intervalos de confiança",
    titlefont=8, size=(600,300))
plot!(intervalo, x -> pdf(Normal(q̄, Δ_q), x), color=1, label="normal limite estimada")
scatter!(reshape(amostras,:,1), fill(pdf(distribuicao,q̄)/15, prod(size(amostras))), label="amostras", color=3, alpha=0.02)
scatter!(medias, fill(pdf(distribuicao,q̄)/15, length(medias)), label="médias das amostras", color=2)
plot!([q̄ - Δ_q, q̄ + Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(medias, nbins=div(M,2), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_21_1.png}


### Distribuição desconhecida Arcsine

```julia
N = 10
M = 20
distribuicao = Arcsine()
intervalo = 0:0.01:1
Random.seed!(1102)
amostras = rand(distribuicao, M, N)
medias = mean(amostras, dims=2)
q̄ = mean(amostras[1,:])
Δ_q = std(amostras[1,:])/√N
nothing
```


```julia
plot(intervalo, x -> pdf(distribuicao, x), color=9, xlims=(minimum(intervalo), maximum(intervalo)),
    label="distribuição desconhecida",
    title="Distribuição desconhecida $distribuicao, normal limite,\nmédia das amostra e intervalos de confiança",
    titlefont=8, size=(600,300))
plot!(intervalo, x -> pdf(Normal(q̄, Δ_q), x), color=1, label="normal limite estimada")
scatter!(reshape(amostras,:,1), fill(pdf(distribuicao,q̄)/15, prod(size(amostras))), label="amostras", color=3, alpha=0.02)
scatter!(medias, fill(pdf(distribuicao,q̄)/15, length(medias)), label="médias das amostras", color=2)
plot!([q̄ - Δ_q, q̄ + Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=5, label="Interv. conf. 68%")
plot!([q̄ - 2Δ_q, q̄ + 2Δ_q], pdf.(distribuicao,[q̄,q̄]), fill=true, alpha=0.2, color=4, label="Interv. conf. 95%")
histogram!(medias, nbins=div(M,2), normed=true, alpha=0.1, color=6, label="histograma dos dados")
```

\fig{images/0501-Erros_e_incertezas_23_1.png}


## Poucos dados e a distribuição t de Student

* No caso de amostras com poucos dados, a média $\bar q_N$ e o desvio padrão corrigido $s_N$ podem não estar muito próximos de $\mu$ e $\sigma$.

* Esse caso foi estudado por um estatístico que publicava com o pseudônimo de Student e que chegou até essa **distribuição-t** (também conhecida como **t de Student**) no caso em que a distribuição inicial, que gera essas amostras, é uma normal.

* A distribuição-t tem um parâmetro real $\nu>0$ que é chamado de **graus de liberdade**, motivado pela associação com o número $N-1$ que vem da amostra. 

* Denotamos essa distribuição por $t_\nu$. A sua função de densidade de probabilidades é dada por
$$ f_\nu(q) = \frac{\Gamma(\frac{\nu+1}{2})} {\sqrt{\nu\pi}\,\Gamma(\frac{\nu}{2})} \left(1+\frac{q^2}{\nu} \right)^{-(\frac{\nu+1}{2})},
$$
onde $\Gamma$ é a função gamma.

* A densidade $f_\nu$ é simétrica em relação a origem.

* A média da distribuição-t é zero, quando $\nu>1$, e é indefinida, caso $0<\nu\leq 1$.

* A sua variância é $\nu/(\nu-2)$, caso $\nu>2$, infinita, caso $1<\nu\leq 2$, e indefinida, caso $0<\nu\leq 1$.


### Gráfico da função de densidade de probabilidade de t

* A figura a seguir exibe o gráfico da função de densidade da distribuição t com vários graus de liberdade e em comparação com a normal.

* Observe que, quanto maior o grau de liberdade $\nu$ ($\sim N-1$), mais próxima a distribuição t fica da normal.

```julia
intervalo = -5:0.05:5
plot(intervalo, pdf.(Normal(), intervalo), label="Normal", size=(600,300),
    title="Distribuições normal e t de Student", titlefont=10)
for ν = (1, 2, 4, 20)
    plot!(intervalo, pdf.(TDist(ν), intervalo), label="t-dist ν=$ν")
end
plot!()
```

\fig{images/0501-Erros_e_incertezas_24_1.png}


### O resultado de Student

* O resultado de Student vale quando a distribuição desconhecida $\mathcal{P}$ é uma normal com média $\mu$.

* Nesse caso, temos que a distribuição $\mathcal{Q}_N$ das médias $\bar q_N$ satisfaz
$$ \frac{\sqrt{\nu}}{s_N} (\mathcal{Q}_N -\mu) = t_\nu,
$$
com o grau de liberdade dado por $\nu=N-1$.

* De outra forma, temos
$$ \mathcal{Q}_N = \mu + \frac{s_N}{\sqrt{N-1}}t_{N-1}.
$$

* Quando $N\geq 3$, temos $\nu = N-1\geq 2$, de forma que $\mathcal{Q}_N$ tem média $\mu$ e variância $\nu/(\nu-2)$.


### Intervalos de confiança baseados na distribuição t

* O formato da distribuição t parece bem próximo do da normal, mas a sua cauda é um tanto mais "grossa".

* E isso é significativo, podendo alterar bastante o intervalo de confiança, que pode ser três ou quatro ou mais vezes mais largo comparado com o da normal.

* Daí a sua maior confiabilidade quando temos poucos dados.

* Para $N$ grande, a distribuição-t se aproxima da normal e as duas aproximações são essencialmente indiferentes.


### Comparando os intervalos de confiança


```julia
intervalos = Dict("68%" => [0.16, 0.84], "95%" => [0.025, 0.975])
for (k, int) in intervalos
    println("Normal IC $k: ", round.(quantile.(Normal(), int), digits=2))
end
println()
for ν in (1, 2, 4, 10, 20, 50)
    for (k, int) in intervalos
        println("T-Dist(ν=$ν) IC $k: ", round.(quantile.(TDist(ν), int), digits=2))
    end
    println()
end
```

```
Normal IC 68%: [-0.99, 0.99]
Normal IC 95%: [-1.96, 1.96]

T-Dist(ν=1) IC 68%: [-1.82, 1.82]
T-Dist(ν=1) IC 95%: [-12.71, 12.71]

T-Dist(ν=2) IC 68%: [-1.31, 1.31]
T-Dist(ν=2) IC 95%: [-4.3, 4.3]

T-Dist(ν=4) IC 68%: [-1.13, 1.13]
T-Dist(ν=4) IC 95%: [-2.78, 2.78]

T-Dist(ν=10) IC 68%: [-1.05, 1.05]
T-Dist(ν=10) IC 95%: [-2.23, 2.23]

T-Dist(ν=20) IC 68%: [-1.02, 1.02]
T-Dist(ν=20) IC 95%: [-2.09, 2.09]

T-Dist(ν=50) IC 68%: [-1.0, 1.0]
T-Dist(ν=50) IC 95%: [-2.01, 2.01]
```




### Visualizando os intervalos de confiança

```julia
intervalo = -7.5:0.05:7.5
plot(intervalo, pdf.(Normal(), intervalo), label="Normal", xlims=(minimum(intervalo),maximum(intervalo)), size=(600,300),
    title="Distribuições normal e t de Student", titlefont=10)
for ν = (1, 2, 4)
    plot!(intervalo, pdf.(TDist(ν), intervalo), label="t-dist ν=$ν")
end
plot!(-2.0:0.1:2.0, x -> pdf(Normal(), x), fill=true, color=2, alpha=0.2,label="CI 95% normal")
for ν = (1, 2, 4)
    plot!(quantile(TDist(ν), 0.025):0.1:quantile(TDist(ν), 0.975), x -> pdf(TDist(ν), x), fill=true, alpha=0.2, label="CI 95% ν=$ν")
end
plot!()
```

\fig{images/0501-Erros_e_incertezas_26_1.png}


## Observações finais

* Uma espécie de resumo:

* Quando temos um número razoável de dados, podemos considerar $\Delta q$ e $2\Delta q$ como os meios-comprimentos dos intervalos de $68\%$ e $95\%$ de confiança, respectivamente. Isso é feito tendo como base o Teorema Central do Limite.

* Quando temos poucos dados, o mais garantido é usar um múltiplo apropriado de $\Delta q$ dado pelos intervalos de probabilidade da distribuição t.

* Nesse último caso, também é comum se usar $\Delta q$ e $2\Delta q$, mas explicitar que isso corresponde a outros níveis de confiança.

* Quanto à teoria, o Teorema Central do Limite vale para uma distribuição desconhecida qualquer, enquanto que o resultado de Student vale apenas no caso dessa distribuição desconhecida ser uma normal.


## Exercícios

1. Aumente e diminua o número $M$ de amostras e o número $N$ de dados em cada amostra e veja o efeito disso nos gráficos correspondentes.

1. Pesquisa sobre as demonstrações do Teorema Central do Limite e do resultado de Student.
