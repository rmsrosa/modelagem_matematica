
@def title = "Qualidade do ajuste"

# {{ get_title }}

- Erros absolutos SS e RMS
- Erros relativos baseados em SS e RMS
- R-quadrado
- R-quadrado ajustado

```julia
using Random
using Statistics
using LinearAlgebra
using Plots
theme(:ggplot2)
```



## Amostra e modelo

Consideramos 

- Uma **amostra** $ (x_i, y_i), i=1, \ldots, N$. 

- Um **modelo** $y = f_\beta(x),$ com **parâmetros** $\beta=(\beta_1, \ldots, \beta_m)$.

- **Valores calculados pelo modelo:** $\hat y_i = f_\beta(x_i).$

- **Dados amostrais:** $ (x_i, \hat y_i), i = 1, \ldots, N.$


## Resíduos

Os resíduos são dados pelas diferenças entre os dados da amostra e os do modelo:

$$ r_i = y_i - f_\beta(x_i).
$$

ou, com a notação $\hat y_i = f(x_i)$,

$$ r_i = y_i - \hat{y}_i.
$$


## Erros absolutos SS e RMS

Duas maneiras naturais, e relacionadas, de calcular o erro de um modelo são:

- **SS dos resíduos** ou **soma dos quadrados dos resíduos** (sum of squares of residuals):

$$ \mathrm{SS}(\mathbf{r}) = \sum_{i=1}^N r_i^2 = \sum_i (y_i - \hat{y}_i)^2.
$$

- **RMS dos resíduos**  ou **raiz quadrada da média dos quadrados dos resíduos** (root-mean-square of the residuals):

$$ \mathrm{RMS}(\mathbf{r}) = \sqrt{\frac{1}{N} \sum_{i=1}^N r_i^2} = \sqrt{\frac{1}{N} \sum_{i=1}^N(y_i - \hat{y}_i}).
$$


**Observações:**

* Estes são erros **absolutos** do modelo.

* $\mathrm{SS}(\mathbf{r})$ depende "fortemente" do número de dados e pode crescer significativamente à medida em que os dados aumentam em número.

* Temos 

$$  \mathrm{RMS}(\mathbf{r}) = \sqrt{\frac{\mathrm{SS(\mathbf{r})}}{N}}.
$$

* $\mathrm{RMS}(\mathbf{r})$ tem a mesma grandeza que $y_i$.


## Erros relativos

Erros relativos podem ser obtidos dividindo os erros absolutos por alguma quantidade de mesma grandeza dos dados. No caso, podemos considerar

- **SS relativo:**

$$ \mathrm{SS}_\textrm{rel} = \frac{\mathrm{SS}(\mathbf{r})}{\mathrm{SS}(\mathbf{y})},
$$

onde $\mathrm{SS}(\mathbf{y}) = \sum_i y_i^2$.

- **RMS relativo dos resíduos**:

$$ \mathrm{RMS}_\mathrm{rel} = \frac{\mathrm{RMS}(\mathbf{r})}{\mathrm{RMS}(\mathbf{y})},
$$

onde $\mathrm{RMS}(\mathbf{y}) = \sqrt{(1/N)\sum_i y_i^2}$.


**Observações:**

- É claro que os denominadores não podem se anular, mas eles so se anulam quando todos $y_i=0$, sendo que, nesse caso, não há muito o que modelar.

- $\mathrm{SS}_\textrm{rel}$ não depende "tão fortemente" do número de amostras. 

- A relação entre $\mathrm{SS}_\textrm{rel}$ e  $\mathrm{RMS}_\textrm{rel}$ não depende explicitamente do número de amostras:

$$ \mathrm{SS}_\textrm{rel} = \mathrm{RMS}_\textrm{rel}^2.
$$

- Como $\mathrm{RMS}$ tem a mesma grandeza que os valores (e.g. comprimento, velocidade, massa, população, moeda), então $\mathrm{RMS}_{\text{rel}}$ é mais natural para expressar o erro relativo.

- Por exemplo, se $\mathrm{RMS}_\textrm{rel} \approx 0.1$, podemos dizer que o modelo nos dá uma aproximação, dos dados da amostra, da ordem de 10%.


## R-quadrado

Uma outra quantidade relativa usada para medir a qualidade de um modelo é o chamado **R quadrado**, ou $R^2$, comparando relativamente o modelo e os dados da amostra em relação ao valor médio dos dados. Considera-se

- A **média dos valores dos dados** da amostra:

$$ \bar y = \frac{1}{N} \sum_{i=1}^N y_i.
$$

- **Soma dos quadrados total em relação à média** (que é proporcional à variância total), medindo, de certa forma, o erro em se aproximar a amostragem por um valor constante igual à média dos dados:

$$ \mathrm{SS}_\mathrm{tot} = \sum_{i=1}^N (y_i - \bar y)^2 = N \mathrm{Var}(y_i).
$$

- **Soma dos quadrados da regressão em relação à media**,  medindo, de certa forma, a diferença entre o modelo ajustado e a média dos dados:

$$ \mathrm{SS}_\mathrm{reg} = \sum_{i=1}^N (\hat y_i - \bar y)^2.
$$

- **R-quadrado,** comparando 

$$ R^2 = \frac{\mathrm{SS}_\mathrm{reg}}{\mathrm{SS}_\mathrm{tot}}.
$$


## R-quadrado em regressão via mínimos quadrados

* Suponha que
  1. O modelo $f_\beta = f_\beta(x)$ seja linear nos parâmetros $\beta$;
  1. A média $\bar y$ possa ser descrita pelo modelo com uma escolha apropriada $\bar\beta$ dos parâmetros, com $\bar y = f_{\bar\beta}(x)$ independente de $x$; e
  1. O ajuste seja feito minimizando-se o erro quadrático dos resíduos,

* Nesse caso, vale a relação 

$$ \mathrm{SS}_\mathrm{reg} = \mathrm{SS}_\mathrm{tot} - \mathrm{SS}_\mathrm{res},
$$
onde $\mathrm{SS}_\mathrm{res} = \mathrm{SS}(\mathbf{r}) = \sum_{i=1}^N (y_i - \hat{y}_i)^2$.

* Isso nos leva à formula mais conhecida

$$ R^2 = 1 - \frac{\mathrm{SS}_\mathrm{res}}{\mathrm{SS}_\mathrm{tot}},
$$

* Como $0 \leq \mathrm{SS}_\mathrm{res} \leq \mathrm{SS}_\mathrm{tot}$, então $0 \leq R^2 \leq 1$.

* Quanto mais próximo $R^2$ estiver de 1, melhor será o ajuste.

* $R^2$ é uma medida da qualidade do ajuste.


## R-quadrado ajustado

- Para compensar um pouco a influência do número de parâmetros, um **R-quadrado ajustado** $R_\textrm{aj}^2$ é usado.

- Temos, mais precisamente, o seguinte ajuste em relação ao número de parâmetros do modelo:

$$ R_\mathrm{aj}^2 = 1 - (1-R^2)\frac{N-1}{N-m},
$$

onde $N$ é o número de dados e $m$ é o número de parâmetros.


## Comparando diferentes modelos

- Uma primeira medida de comparação entre diferentes modelos é comparar os valores correspondentes de algumas das quantidade vistas acima:

    - RMS absoluto
    
    - RMS relativo
    
    - SS relativo
    
    - R-quadrado
    
    - R-quadrado ajustado
    
- A medida SS absoluta não é apropriada porque depende fortemente do número de dados.

- A dependência dessas medidas em relação ao número de parâmetros também é um ponto delicado.


## Exemplo sintético

Neste exemplo, vamos 

- Construir dados sintéticos a partir de perturbações aleatórias em torno de uma determinada função.

- Perturbações uniformemente distribuídas entre $\pm 0.3$ na abscissa.

- Perturbações uniformemente distribuídas entre $\pm 1$ na ordenada.

- Em seguida, usaremos mínimos quadrados para ajustar um polinômio de grau três.

- Posteriormente, mínimos quadrados para ajustar polinômios de diversos graus.


### Definição do modelos e da função geradora dos dados

```julia
# f = β₀ + β₁x + β₂x² + … + βᵢxⁱ
f_modelo(x, β) = β ⋅ [x^j for j in 0:length(β)-1]
f_dados(x,β) = exp(β[4]*x) * (β[1] + β[2]*x + β[3]*x^2 + β[4]*x^3)
β̲ = [5.2, 0.5, -0.45, 0.05]
x = -1.0:0.1:8.0
nothing
```


```julia
plot(x, x -> f_dados(x,β̲), label=nothing, xlim=(-1,8), ylim=(1,9), legend=false,
    titlefont=10, title="função para a geração da amostra")
```

\fig{images/0601-Qualidade_do_modelo_3_1.png}


### Gerando os dados sintéticos

```julia
dados_x = collect(0.0:8.0) .+ 0.3 * randn(MersenneTwister(14003), 9)
dados_y = f_dados.(dados_x, Ref(β̲)) .+ randn(MersenneTwister(14004), 9)
nothing
```


```julia
plot(xlim=(-1,8), ylim=(1,9), legend=:topleft,
    titlefont=10, title="função para a amostra e dados sintéticos")
plot!(dados_x, dados_y, seriestype=:scatter, label="amostra")
plot!(x, x -> f_dados(x,β̲), label="função para a amostra")
```

\fig{images/0601-Qualidade_do_modelo_5_1.png}


### Regressão linear via mínimos quadrados

```julia
A = [ones(length(dados_x)) dados_x dados_x.^2 dados_x.^3]
```

```
9×4 Matrix{Float64}:
 1.0  0.0851634   0.0072528    0.000617673
 1.0  0.684559    0.468621     0.320799
 1.0  2.31975     5.38123     12.4831
 1.0  3.23412    10.4595      33.8274
 1.0  3.99424    15.954       63.724
 1.0  4.93406    24.345      120.12
 1.0  6.2438     38.985      243.415
 1.0  6.9403     48.1677     334.298
 1.0  7.98801    63.8083     509.701
```



```julia
β̂ = A \ dados_y
```

```
4-element Vector{Float64}:
  5.58285349098757
  0.7068669251980298
 -0.5942506978954095
  0.07079991932172676
```




### Função para cálculo das medidas de qualidade do modelo

```julia
function info_ajuste(dados_x, dados_y, model_y, k)
    N = length(dados_x)
    y_mean = mean(dados_y)
    residuos = model_y - dados_y
    ss = norm(residuos)^2
    rms = sqrt(ss/N)
    ss_y = norm(dados_y)^ 2
    rms_y = sqrt(ss_y/N)
    ss_rel = ss/ss_y
    rms_rel = sqrt(ss_rel)
    ss_tot = N*var(dados_y)
    ss_reg = norm(model_y .- y_mean)^2
    r_sq = ss_reg/ss_tot
    r_sq_aj = 1 - (1 - r_sq)*(N-1)/(N-k)
    
    return (
        residuos=residuos, rms=rms, rms_rel=rms_rel, ss=ss, ss_rel=ss_rel,
        r_sq=r_sq, r_sq_aj=r_sq_aj
    )
end
```

```
info_ajuste (generic function with 1 method)
```




### Resultado

```julia
info = info_ajuste(dados_x, dados_y, f_modelo.(dados_x,Ref(β̂)), length(β̂))

println("RMS dos resíduos: $(info.rms)")
println("RMS relativo: $(info.rms_rel)")
println("Baseado no RMS relativo, o modelo nos dá uma aproximação de $(100*info.rms_rel)% dos dados")
println("SS dos resíduos: $(info.ss)")
println("SS relativo: $(info.ss_rel)}")
println("R-quadrado: $(info.r_sq)")
println("R-quadrado ajustado: $(info.r_sq_aj)")
```

```
RMS dos resíduos: 0.5796526627862785
RMS relativo: 0.10662332249595524
Baseado no RMS relativo, o modelo nos dá uma aproximação de 10.662332249595
524% dos dados
SS dos resíduos: 3.023974885277007
SS relativo: 0.011368532900076474}
R-quadrado: 0.803366892196622
R-quadrado ajustado: 0.6853870275145952
```



```julia
plot(titlefont=10, title="Modelo ajustado e dados sintéticos", legend=:topleft,
    xlim=(-1,8), ylim=(1,9))
plot!(dados_x, dados_y, seriestype=:scatter, label="amostra")
plot!(x,x->f_modelo(x,β̂), label="modelo ajustado 1 (R² = $(round(info.r_sq,digits=3)), " * 
    "R²_aj = $(round(info.r_sq_aj,digits=3)), RMS_rel = $(round(info.rms_rel,digits=3)))",
    linestyle=:dash)
```

\fig{images/0601-Qualidade_do_modelo_10_1.png}


## Aumentando o número de dados

```julia
dados_novos_x = collect(0.5:8.5) .+ 0.3 * randn(MersenneTwister(14005), 9)
dados_novos_y = f_dados.(dados_x, Ref(β̲)) .+ randn(MersenneTwister(14006), 9)
dados2_x = reshape([dados_x'; dados_novos_x'],:,1)
dados2_y = reshape([dados_y'; dados_novos_y'],:,1)
nothing
```


```julia
A2 = [ones(length(dados2_x)) dados2_x dados2_x.^2 dados2_x.^3]
β̂2 = A2 \ dados2_y
```

```
4×1 Matrix{Float64}:
  5.8277427790137155
  0.15311793108645264
 -0.35223469770266713
  0.04515333070990545
```




## Dados da análise

```julia
info2 = info_ajuste(dados2_x, dados2_y, f_modelo.(dados2_x,Ref(β̂2)), length(β̂2))

println("RMS dos resíduos: $(info2.rms)")
println("RMS relativo: $(info2.rms_rel)")
println("Baseado no RMS relativo, o modelo nos dá uma aproximação de $(100*info2.rms_rel)% dos dados")
println("SS dos resíduos: $(info2.ss)")
println("SS relativo: $(info2.ss_rel)}")
println("R-quadrado: $(info2.r_sq)")
println("R-quadrado ajustado: $(info2.r_sq_aj)")
```

```
RMS dos resíduos: 0.8522086357821341
RMS relativo: 0.1593346115310878
Baseado no RMS relativo, o modelo nos dá uma aproximação de 15.933461153108
78% dos dados
SS dos resíduos: 13.072672060229628
SS relativo: 0.02538751843176266}
R-quadrado: 0.7237391241568886
R-quadrado ajustado: 0.6645403650476505
```



```julia
plot(titlefont=10, title="Modelos ajustados e dados sintéticos", 
    xlim=(-1,8), ylim=(1,9), legend=:topleft)
plot!(dados2_x, dados2_y, seriestype=:scatter, label="amostra 2")
plot!(dados_x, dados_y, markersize=2, seriestype=:scatter, label="amostra 1", color=:orange)
plot!(x, x -> f_modelo(x, β̂), label="modelo ajustado 1 (R² = $(round(info.r_sq, digits=3)), " *
    "R²_aj = $(round(info.r_sq_aj, digits=3)), RMS_rel = $(round(info.rms_rel, digits=3)))",
    linestyle=:dash)  
plot!(x, x -> f_modelo(x, β̂2), label="modelo ajustado 2 (R² = $(round(info2.r_sq_aj, digits=3)), " *
    "R²_aj = $(round(info2.r_sq_aj,digits=3)), RMS_rel = $(round(info2.rms_rel, digits=3)))",
    linestyle=:dash)
```

\fig{images/0601-Qualidade_do_modelo_14_1.png}


## Ajuste com polinômios de grau mais alto

```julia
A3 = reduce(hcat, [dados_x.^j for j=0:8])
```

```
9×9 Matrix{Float64}:
 1.0  0.0851634   0.0072528  …       3.24915e-8      2.76709e-9
 1.0  0.684559    0.468621           0.0704495       0.0482268
 1.0  2.31975     5.38123          361.481         838.544
 1.0  3.23412    10.4595          3700.78        11968.8
 1.0  3.99424    15.954          16219.6         64785.0
 1.0  4.93406    24.345      …   71192.4             3.51268e5
 1.0  6.2438     38.985         369950.0             2.30989e6
 1.0  6.9403     48.1677             7.75614e5       5.38299e6
 1.0  7.98801    63.8083             2.07525e6       1.65771e7
```



```julia
β̂3 = A3 \ dados_y
```

```
9-element Vector{Float64}:
   5.480089368087107
  -0.13193193809904286
   7.443460411397602
 -12.974325526375585
   8.319509808076305
  -2.613748308967248
   0.4320196312510229
  -0.036062570034203024
   0.001199219931939132
```




### Resultado

```julia
info3 = info_ajuste(dados_x, dados_y, f_modelo.(dados_x, Ref(β̂3)), length(β̂3))

println("RMS dos resíduos: $(info3.rms)")
println("RMS relativo: $(info3.rms_rel)")
println("SS dos resíduos: $(info3.ss)")
println("SS relativo: $(info3.ss_rel)}")
println("R-quadrado: $(info3.r_sq)")
println("R-quadrado ajustado: $(info3.r_sq_aj)")
```

```
RMS dos resíduos: 1.0864081316586043e-11
RMS relativo: 1.998376821513424e-12
SS dos resíduos: 1.0622543656805452e-21
SS relativo: 3.993509920762095e-24}
R-quadrado: 0.8888888888838526
R-quadrado ajustado: -Inf
```



```julia
plot(titlefont=10, title="Modelos ajustados e dados sintéticos", legend=:topleft,
    xlim=(-1,8), ylim=(1,9))
plot!(dados2_x, dados2_y, seriestype=:scatter, label="amostra 2")
plot!(dados_x, dados_y, markersize=2, seriestype=:scatter, label="amostra 1", color=:orange)
plot!(x, x -> f_modelo(x, β̂),
    label="modelo ajustado 1 (R² = $(round(info.r_sq, digits=3)), " * 
    "R²_aj = $(round(info.r_sq_aj, digits=3)), RMS_rel = $(round(info.rms_rel, digits=3)))",
    linestyle=:dash)
plot!(x, x -> f_modelo(x, β̂2),
    label="modelo ajustado 2 (R² = $(round(info2.r_sq, digits=3)), " * 
    "R²_aj = $(round(info2.r_sq_aj, digits=3)), RMS_rel = $(round(info2.rms_rel, digits=3)))",
    linestyle=:dash)
plot!(x, x -> f_modelo(x, β̂3),
    label="modelo ajustado 3 (R² = $(round(info3.r_sq, digits=3)), " * 
    "R²_aj = $(round(info3.r_sq_aj, digits=3)), RMS_rel = $(round(info3.rms_rel, digits=3)))",
    linestyle=:dash)
```

\fig{images/0601-Qualidade_do_modelo_18_1.png}


## Exercícios

1. Mostre a relação $\mathrm{SS}_\text{reg} = \mathrm{SS}_\text{tot} - \mathrm{SS}_\text{res}$ sob as condições mencionadas no texto, i.e:
    1. O modelo $f_\beta = f_\beta(x)$ é linear nos parâmetros $\beta$;
    1. A média $\bar y$ pode ser descrita pelo modelo com uma escolha apropriada $\bar\beta$ dos parâmetros, com $\bar y = f_{\bar\beta}(x)$ independente de $x$; e
    1. O ajuste é feito minimizando-se o erro quadrático dos resíduos,

1. Calcule os fatores de qualidade de ajuste, discutidos acima, das modelagens feitas nos exercícios do caderno 8, sobre **Modelos redutíveis ao caso linear nos parâmetros e aplicações**.

2. Sobre o problema de modelagem de reação enzimática em fígados de porcos, também discutido no caderno 8, considere ainda ajustes por modelos polinomiais de diferentes ordens e calcule os respectivos fatores de qualidade de ajuste.
