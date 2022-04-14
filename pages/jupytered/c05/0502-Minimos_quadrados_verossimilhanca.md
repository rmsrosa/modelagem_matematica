
@def title = "Mínimos quadrados, maximização da verossimilhança e quantificação de incertezas em regressões lineares"

# {{ get_title }}

* Continuando o assunto de probabilidade, vamos ver o problema de mínimos quadrados linear como um problema de maximização da verossimilhança.

* Os dois métodos são equivalentes, quando a distribuição de probabilidade do erro das amostras é normal.

* Mas a verossimilhança envolve uma interpretação diferente do problema, com aspectos probabilísticos.

* Como consequência, podemos quantificar as incertezas na escolha dos parâmetros e nas predições do modelo.

```julia
using Distributions
using Plots
using Random
using LinearAlgebra: ⋅
```



## Hipóteses probabilísticas

* Consideremos um modelo linear 
$$ y = \beta_0  + \beta_1 x
$$

* De um ponto de vista probabilístico, consideramos incertezas inerentes na obtenção dos dados $x$ e na definição do modelo.

* Com base nisso, interpretamos o modelo como uma relação para o **valor esperado** de $y$, **dado** $x$, i.e.
$$ E(y|x) = \beta_0  + \beta_1 x
$$

* Tanto $y$ como o erro $\epsilon = y - \beta_0  + \beta_1 x$ são vistos como variáveis aleatórias e assume-se que o erro segue uma normal, com o mesmo desvio padrão ao longo da variável $x$:
$$ \epsilon \sim \mathcal{N}(0,\sigma^2).
$$

* Assim, a probabilidade condicional de $y$ dado $x$ é
$$ \mathcal{P}(y|x) \sim \mathcal{N}(\beta_0 + \beta_1 x, \sigma^2).
$$

* Além disso, assumimos que os erros são independentes entre si. Ou seja, em quaisquer dois pontos $x_i, x_j$, os erros $\epsilon_i, \epsilon_j$ nesses pontos são independentes entre si, ou seja, não são correlacionados, o que pode ser expresso por $E(\epsilon_i\epsilon_j)=0$.


## Verossimilhança

* A função densidade de probabilidade da normal $\mathcal{N}(\mu, \sigma)$ é
$$ f_{\mu, \sigma^2}(s) = \frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}e^{\displaystyle -\frac{(s-\mu)^2}{2\sigma^2}}.
$$

* No caso de $\mathcal{P}(y|x) \sim \mathcal{N}(\beta_0 + \beta_1 x, \sigma^2)$, e considerando $\sigma$ fixo, a função densidade de probabilidade de $\mathcal{P}(y|x)$, que depende de $\boldsymbol\beta = (\beta_0, \beta_1)$, se torna
$$ f_\beta(y) = \frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}e^{\displaystyle -\frac{(y - \beta_0 - \beta_1 x)^2}{2\sigma^2}}.
$$

* Olhando essa função de maneira diferente, em um dado valor observado $y$ (para um certo $x$ fixo), e com o parâmetro $\boldsymbol\beta$ variável, temos a **função de verossimilhança**
$$ \mathcal{L}_y(\boldsymbol\beta) = f_{\boldsymbol\beta}(y) = \frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}e^{\displaystyle -\frac{(y - \beta_0 - \beta_1 x)^2}{2\sigma^2}}.
$$

* Observe que quanto mais perto $\beta_0 + \beta_1 x$ estiver de $y$, maior será a verossimilhança.

* Mas independentemente da forma da função de densidade de distribuição, maximizar a verossimilhança é aumentar a probabilidade do modelo resultar no dado observado.


## Função de verossimilhança em um conjunto de observações

* Dado um conjunto de observações $(\mathbf{x}, \mathbf{y}) = (x_i, y_i)_{i=1}^N$, a probabilidade conjunta é o produto das probabilidades, $\mathcal{P}(y_1|x_1)\mathcal{P}(y_2|x_2)\cdots\mathcal{P}(y_N|x_N)$.

* Em relação à função densidade de probabilidades, obtemos
$$ f_N(\mathbf{y},\boldsymbol\beta) = \frac{1}{\displaystyle (2\pi \sigma^2)^{N/2}}e^{\displaystyle -\frac{1}{2\sigma^2}\sum_{i=1}^N(y_i - \beta_0 - \beta_1 x_i)^2}.
$$

* A função de verossimilhança da amostra é
$$ \mathcal{L}_N(\boldsymbol\beta) = \Pi_i \mathcal{L}_{y_i}(\boldsymbol\beta) = f_N(\mathbf{y},\boldsymbol\beta) = \frac{1}{\displaystyle (2\pi \sigma^2)^{N/2}}e^{\displaystyle -\frac{1}{2\sigma^2}\sum_{i=1}^N(y_i - \beta_0 - \beta_1 x_i)^2}.
$$

* Maximizar $\mathcal{L}_N(\boldsymbol\beta)$ é aumentar a probabilidade do modelo resultar numa boa aproximação para o conjunto de dados observados.


## Função de log-verossimilhança

* Obtivemos a função de verossimilhança "pontual"
$$ \mathcal{L}_y(\boldsymbol\beta) = \frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}e^{\displaystyle -\frac{(y - \beta_0 - \beta_1 x)^2}{2\sigma^2}}.
$$

* Associada a ela, temos a **função de log-verossimilhança**
$$ \ell_y(\boldsymbol\beta) = \log(\mathcal{L}_y(\boldsymbol\beta) = \log\left(\frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}\right) - \frac{(y - \beta_0 - \beta_1 x)^2}{2\sigma^2}.
$$

* Como o logaritmo é monónoto crescente, maximizar a verossimilhança é equivalente a maximizar a log-verossimilhança.

* No caso da normal, vemos que a log-verossimilhança tem uma dependência bem mais amigável, no sentido de ser linear.

* No caso de um conjunto de dados, a função de log-verossimilhança toma a forma
$$ \ell_N(\boldsymbol\beta) = \log \mathcal{L}_N(\boldsymbol\beta) = N\log\left(\frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}\right) - \frac{1}{2\sigma^2}\sum_{i=1}^N (y_i - \beta_0 - \beta_1 x_i)^2.
$$


## Maximização da verossimilhança e minimização do erro quadrático

* Chegamos, então, a
$$ \ell_N(\boldsymbol\beta) = N\log\left(\frac{1}{\displaystyle \sqrt{2\pi \sigma^2}}\right) - \frac{1}{2\sigma^2}\sum_{i=1}^N (y - \beta_0 - \beta_1 x)^2.
$$

* O primeiro termo não depende de $\boldsymbol\beta$.

* E vemos, do segundo termo, que maximizar a verossimilhança é equivalente a minimizar o erro quadrático (i.e. a soma dos quadrados dos resíduos (RSS))
$$ \operatorname{RSS}(\boldsymbol\beta) = \sum_{i=1}^N (y - \beta_0 - \beta_1 x)^2.
$$

* Dessa forma, estabelecemos a equivalência entre os dois métodos (mas com interpretações diferentes):
$$ \hat{\boldsymbol\beta} = \operatorname{argmax}_{\boldsymbol\beta} \mathcal{L}_N(\boldsymbol\beta) = \operatorname{argmax}_{\boldsymbol\beta} \ell_N(\boldsymbol\beta) = \operatorname{argmin}_{\boldsymbol\beta} \operatorname{RSS}(\boldsymbol\beta).
$$

* Essa equivalência vale quando o erro é uma normal, com média zero, e desvio padrão uniforme ao longo de $x$.


## Estimativa sobre a determinação nos parâmetros

* Com esse arcabouço probabilístico, podemos extrair informações sobre a incerteza na determinação dos parâmetros $\boldsymbol\beta=(\beta_0, \beta_1)$. 

* Obtivemos, acima, o maximizador da verossimilhança $\hat{\boldsymbol\beta}$ dado exatamente pela forma normal da solução pelo método de mínimos quadrados:
$$ \hat{\boldsymbol\beta} = (X^TX)^{-1}X^T\mathbf{y}.
$$

* Nesta fórmula,  $X = [\mathbf{1}, \mathbf{x}]$ é a matrix de Vandermonde, que assumimos de posto máximo, e $\mathbf{y}$ é dado por $\mathbf{y} = (y_1, \ldots, y_N)$

* Agora, ao invés de olharmos estritamente para $\boldsymbol\beta$ que minimiza o erro entre as medições $y_i$ e o do resultado do modelo $\beta_0 + \beta_1 x_i$, vamos olhar para possíveis outras escolhas $\mathbf{y} = X\mathbf{\boldsymbol\beta} + \boldsymbol{\epsilon}$, que talvez extrapolassem melhor $y = \beta_0 + \beta_1 x$ para outros dados.

* Considerando, então, $\mathbf{y} = X\mathbf{\boldsymbol\beta} + \boldsymbol{\epsilon}$, obtemos
$$ \hat{\boldsymbol\beta} = (X^TX)^{-1}X^T(X\boldsymbol\beta + \boldsymbol{\epsilon}) = \boldsymbol\beta + (X^TX)^{-1}X^T\boldsymbol{\epsilon}.
$$

* Logo, $\boldsymbol\beta$ é uma variável aleatória cuja diferença para o maximizador $\hat{\boldsymbol\beta}$ é dada por
$$ \boldsymbol\beta - \hat{\boldsymbol\beta} = - (X^TX)^{-1}X^T\boldsymbol{\epsilon}.
$$


## Variância na determinação dos parâmetros

* Como $\hat{\boldsymbol\beta}$ está fixo (constante), temos $E(\hat{\boldsymbol\beta}) = \hat{\boldsymbol\beta}$, de modo que $\operatorname{Var}(\boldsymbol\beta) = \operatorname{Var}(\boldsymbol\beta - \hat{\boldsymbol\beta}) = \operatorname{Var}(\hat{\boldsymbol\beta}-\boldsymbol\beta)$ (verifique!). Portanto,
$$ \operatorname{Var}(\boldsymbol\beta) = \operatorname{Var}\left((X^TX)^{-1}X^T\boldsymbol{\epsilon}\right).
$$

* Se $X$ e $\epsilon$ fossem escalares, seria fácil deduzir que $\operatorname{Var}(\beta) = (X^TX)^{-1}X^T\operatorname{Var}(\epsilon)X(X^TX)^{-1}$. Mas não é o caso.

* No caso multidimensional, em que $X$ é de fato uma matriz e $\boldsymbol\epsilon$ e $\boldsymbol\beta$ são vetores, temos o valor esperado nos dando um vetor com os valores esperados de cada coordenada e temos a variância sendo estendida a uma **matrix de variância-covariância**, nos dando não apenas a variação de cada coordenada, mas também uma variação conjunto entre cada par de coordenadas. E a variância de $\boldsymbol\beta$ envolve tudo isso.


## Valor esperado e variância-covariância de variáveis aleatórias multidimensionais

* Por exemplo, se $\boldsymbol\beta=(\beta_1, \ldots, \beta_m)$ é uma variável aleatória multidimensional, então o **valor esperado** (ou média) é
$$ E(\boldsymbol\beta) = (E(\beta_1), \ldots, E(\beta_m)).
$$

* Também podemos considerar a **variância** de cada coordenada, $\operatorname{Var}(\beta_i) = E((\beta_i - E(\beta_i))^2)$, nos dando o vetor variância
$$ \operatorname{Var}(\boldsymbol\beta) = (\operatorname{Var}(\beta_1), \ldots, \operatorname{Var}(\beta_m)).
$$

* Mas também é relevante levarmos em consideração a **covariância** entre as coordenadas,
$$\operatorname{Cov}(\beta_j, \beta_k) = E((\beta_j - E(\beta_j))(\beta_k - E(\beta_k))).
$$

* Naturalmente, $\operatorname{Cov}(\beta_i, \beta_i) = \operatorname{Var}(\beta_i)$.

* Juntando os dois conceitos, temos a **matriz de variância-covariância**
$$ \operatorname{Cov}(\boldsymbol\beta) = \operatorname{Cov}.(\mathbf{\beta}, \mathbf{\beta}^T) = \left[ \begin{matrix} 
  \operatorname{Var}(\beta_1) & \operatorname{Cov}(\beta_1, \beta_2) & \ldots & \operatorname{Cov}(\beta_1, \beta_m) \\
  \operatorname{Cov}(\beta_2, \beta_1) & \operatorname{Var}(\beta_2)& \dots & \operatorname{Cov}(\beta_2, \beta_m) \\
  \vdots & \vdots & \vdots & \vdots \\
  \operatorname{Cov}(\beta_m, \beta_1) & \operatorname{Cov}(\beta_m, \beta_2) & \ldots & \operatorname{Var}(\beta_m)
\end{matrix}\right].
$$

* De forma mais compacta,
$$ \operatorname{Cov}(\boldsymbol\beta) = E((\boldsymbol\beta - E(\boldsymbol\beta))(\boldsymbol\beta - E(\boldsymbol\beta))^T).
$$


## Variância-covariância na determinação dos parâmetros

* Estamos interessados, então, na matriz $\operatorname{Cov}(\boldsymbol\beta)$, sabendo que $\boldsymbol\beta - \hat{\boldsymbol\beta} = - (X^TX)^{-1}X^T\boldsymbol{\epsilon}$.

* Nesse caso, usamos que
$$ \operatorname{Cov}(\boldsymbol\beta) = \operatorname{Cov}(\boldsymbol\beta - \hat{\boldsymbol\beta}) = \operatorname{Cov}((X^TX)^{-1}X^T\boldsymbol{\epsilon}).
$$

* É possível mostrar, com alguns cálculos algébricos, que
$$ \operatorname{Cov}(\boldsymbol\beta) = (X^TX)^{-1}X^TE(\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T)X(X^TX)^{-1} - (X^TX)^{-1}X^TE(\boldsymbol{\epsilon})E(\boldsymbol{\epsilon})^TX(X^TX)^{-1}.
$$

* Como $E(\boldsymbol\epsilon)=0$, sobra
$$ \operatorname{Cov}(\boldsymbol\beta) = (X^TX)^{-1}X^TE(\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T)X(X^TX)^{-1}.
$$

* Finalmente, da hipótese de que os erros são independentes entre si, têm média zero, e têm o mesmo desvio padrão $\sigma$, então $E(\epsilon_j\epsilon_k) = 0$, para $j\neq k$, e $E(\epsilon_j\epsilon_j) = \sigma^2$, ou seja
$$ E(\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T) = \sigma^2 I,
$$
onde $I$ é a matriz identidade.

* Logo,
$$ \operatorname{Cov}(\boldsymbol\beta) = \sigma^2(X^TX)^{-1}.
$$

* Em particular, o vetor variância é a diagonal da matriz:
$$ \operatorname{Var}(\boldsymbol\beta) = \sigma^2\operatorname{diag}((X^TX)^{-1}).
$$


### Incerteza do modelo

* Com a incerteza nos parâmetros caracterizada pela matriz de variância-covariância $\operatorname{Cov}(\boldsymbol\beta)$, podemos estimar a incerteza do modelo

* Considerando $y = \beta_0 + \beta_1 x$, temos
$$ \operatorname{Var}(y) = \operatorname{Var}(\beta_0 + \beta_1 x).
$$

* A questão é como calcular essa variância do lado direito da expressão.

* Explicitando a expressão e usando que $E(\beta_0 + \beta_1 x) = \hat\beta_0 + \hat\beta_1 x$, temos
$$ \operatorname{Var}(y)
= E\left( (\beta_0 + \beta_1 x - \hat\beta_0 - \hat\beta_1 x)^2\right)
= E\left( (\beta_0 - \hat\beta_0)^2 + 2(\beta_0 - \hat\beta_0)(\beta_1 - \hat\beta_1)x + (\beta_1 - \hat\beta_1)^2x^2)\right) \\
= \operatorname{Var}(\beta_0) + 2\operatorname{Cov}(\beta_0,\beta_1)x + \operatorname{Var}(\beta_1)x^2.
$$

* Em forma matricial, e fazendo $\mathbf{x} = (1,x)$, isso pode ser escrito como
$$ \operatorname{Var}(y) = \mathbf{x} \cdot \operatorname{Cov}(\boldsymbol \beta) \mathbf{x} = \sigma^2 \mathbf{x} \cdot (X^TX)^{-1}\mathbf{x}.
$$

* Isso nos dá a variância de $y = \beta_0 + \beta_1 x = \boldsymbol\beta \mathbf{x}$, em cada ponto $x$.


### Intervalo de confiança

* O processo de determinação dos parâmetros envolve uma média que faz com que variância calculada acima seja, de fato, uma medida da incerteza no parâmetro.

* De fato, observemos o caso mais simples em que queremos modelar apenas os erros $\epsilon = N(0,\sigma)$ por uma constante.

* Fazemos uma série de amostras $(\epsilon_i)_{i=1}^N$ e buscamos encontrar o valor médio $\hat\beta_0$ pelo método de mínimos quadrados.

* Nesse caso, a matrix $X$ é uma matrix $N\times 1$ com todos os elementos iguais a 1:
$$ X = \left[ \begin{matrix} 1 \\ \vdots \\ 1 \end{matrix} \right]
$$

* E o valor médio é dado por $\hat\beta_0 = (X^TX)^{-1}(X^T\epsilon_i).$


* Observe que $X^TX = N$ e $X_T\epsilon_i = \sum_{i=1}^N \epsilon_i$, de modo que $\hat\beta_0$ é, conforme esperado, o valor médio da amostra:
$$ \hat\beta_0 = \frac{1}{N}\sum_{i=1}^N \epsilon_i.
$$

* Quanto à variância, obtemos, de fato, o erro padrão
$$ \operatorname{Var}(\beta) = \sigma^2 \operatorname{diag}((X^TX)^{-1}) = \frac{\sigma^2}{N}.
$$

* Assim, os intervalos de confiânça para $E(\beta)$ são dados em função de $\operatorname{Var}(\beta)$, e.g.
$$ \operatorname{IC}_{68\%} = [\hat\beta_0 - \operatorname{Var}(\beta), \hat\beta_0 + \operatorname{Var}(\beta)], \qquad \operatorname{IC}_{95\%} = [\hat\beta_0 - 2\operatorname{Var}(\beta), \hat\beta_0 + 2\operatorname{Var}(\beta)].
$$

* Caso sejam poucas amostras, devemos considerar a função t de Student no cálculo do fator multiplicativo de $\operatorname{Var}(\beta)$ na obtenção dos intervalos de confiança.


### Desvio padrão corrigido da amostra

* Observe que essas medidas dependem do desvio padrão $\sigma$ da incerteza na coleta dos dados.

* Em certos casos, essa medida pode ser obtida dos instrumentos de medição e do próprio processo de coleta.

* Na falta de maiores informações, uma alternativa é utilizar o desvio padrão corrigido da amostra. No caso, no entanto, não estamos fazendo um conjunto $(x_j,y_j)$ de medições na mesma situação. Estamos medindo em pontos diversos. 

* Por conta disso, usamos o próprio modelo para compensar isso e devemos considerar que agora o grau de liberdade disponível é $N-m$, onde $m=2$.

* No caso de dados nas "mesmas" condições, temos $m=1$, como feito antes. Mas agora, temos dois parâmetros, $\beta_0$ e $\beta_1$, logo $m=2$. Em outros modelos, $m$ pode ser maior.

* Assim, o *desvio padrão corrigido da amostra* é
$$ s_q^2 = \frac{1}{N-m}\sum_{i=1}^N (y_i - \hat{\boldsymbol\beta}\mathbf{x}_i)^2 = \frac{1}{N-2}\sum_{i=1}^N (y_i - \hat\beta_0 - \hat\beta_1x_i)^2.
$$



## Exemplo sintético

* Vamos construir um exemplo sintético.

* Vamos "perturbar" uma determinada reta com erros aleatórios segundo uma determinada normal com desvio padrão pré-definido.

```julia
b = 1.0
m = 0.2
σ = 1.0
N = 20
```

```
20
```



```julia
Random.seed!(1200)
x_org = [0.0, 10.0]
y_org = b .+ m * x_org
data_x = collect(range(0.0,10.0, length=N)) + rand(N)/N
data_y = b .+ m * data_x .+ rand(Normal(0,σ), N)
plot(x_org, y_org)
scatter!(data_x, data_y, markersize=3, label="amostra")
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_3_1.png}


### Determinando os parâmetros

```julia
X = [ones(N) data_x]
β = X \ data_y
```

```
2-element Vector{Float64}:
 1.1988117103655653
 0.1431233525841148
```




### Visualizando o resultado

```julia
plot(x_org, y_org, label="original", legend=:topleft)
scatter!(data_x, data_y, markersize=3, label="amostra")
plot!(x_org, β[1] .+ β[2] * x_org, label="modelo")
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_5_1.png}


### Intervalos de confiança dos parâmetros

```julia
Cov_β = σ^2 * inv(X' * X)
```

```
2×2 Matrix{Float64}:
  0.187317   -0.0273258
 -0.0273258   0.0054378
```



```julia
println("Valores originais: β₀=$b, β₁=$m")
println("CI 68% para β₀: [$(round(β[1] - Cov_β[1,1],digits=2)), $(round(β[1] + Cov_β[1,1],digits=2))]")
println("CI 68% para β₁: [$(round(β[2] - Cov_β[2,2],digits=2)), $(round(β[2] + Cov_β[2,2],digits=2))]")
println("CI 95% para β₀: [$(round(β[1] - 2Cov_β[1,1],digits=2)), $(round(β[1] + 2Cov_β[1,1],digits=2))]")
println("CI 95% para β₁: [$(round(β[2] - 2Cov_β[2,2],digits=2)), $(round(β[2] + 2Cov_β[2,2],digits=2))]")
```

```
Valores originais: β₀=1.0, β₁=0.2
CI 68% para β₀: [1.01, 1.39]
CI 68% para β₁: [0.14, 0.15]
CI 95% para β₀: [0.82, 1.57]
CI 95% para β₁: [0.13, 0.15]
```




### Variância do modelo e intervalos de confiança

```julia
Var_y = [[1; x] ⋅ (Cov_β * [1; x]) for x in data_x]
```

```
20-element Vector{Float64}:
 0.1850690674998656
 0.15989728825520982
 0.13472605333885973
 0.11383670913058842
 0.09548818390233765
 0.08014032619999448
 0.06830466732393874
 0.05936414503671618
 0.05325748751001498
 0.05035707669772975
 0.050326457791429025
 0.05354621420722602
 0.059513423230789946
 0.0679696253583599
 0.08049659618144062
 0.09529307440702722
 0.11444701290418935
 0.13374704790809291
 0.15834618382131757
 0.18587335929487261
```



```julia
plot(x_org, y_org, label="original", size=(600,300), titlefont=10,
    title="Reta original, amostra, modelo, CI 68% (sombreado), CI 95% (barras de erro)", )
scatter!(data_x, data_y, markersize=3, label="amostra")
plot!(data_x,β[1] .+ β[2] * data_x, grid=false, yerror=2*sqrt.(Var_y),
    ribbon=sqrt.(Var_y), fillalpha=0.2, label="modelo", legend=:topleft)
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_9_1.png}


### Utilizando o desvio padrão corrigido da amostra

* Como a amostra foi obtida de maneira sintética, conhecemos o desvio padrão associado a distribuição dos erros.

* Mas em geral isso não está disponível.

* Nesse caso, podemos aproximá-lo com o desvio padrão corrigido $s_q$ da amostra.

* Observe que $s_q$ fica bem próximo do valor original de $\sigma$ e que o desvio padrão não-corrigido da amostra fica ligeiramente distante.

```julia
s_q = √(sum(abs2,  data_y .- β[1] .- β[2] * data_x)/(N-2))
println("Desvio padrão original: $σ")
println("Desvio padrão corrigido da amostra: $(round(s_q, digits=3))")
println("Desvio padrão não corrigido da amostra: $(round(s_q * √((N-2)/N),digits=3))")
```

```
Desvio padrão original: 1.0
Desvio padrão corrigido da amostra: 0.953
Desvio padrão não corrigido da amostra: 0.904
```



```julia
Cov_q = s_q^2 * inv(X' * X)
Var_q = [[1; x] ⋅ (Cov_q * [1; x]) for x in data_x]
```

```
20-element Vector{Float64}:
 0.1681389053725685
 0.1452698464549866
 0.1224012820704281
 0.10342290001783529
 0.08675290222319419
 0.07280907017850202
 0.062056140179626976
 0.05393349898874429
 0.04838547993890799
 0.04575039939467411
 0.04572258151317366
 0.04864779384947511
 0.054069121178268606
 0.061751747932411796
 0.07313274849766521
 0.08657564139072514
 0.10397737305768068
 0.12151183628833892
 0.14386063742207592
 0.1688696203636769
```



```julia
plot(x_org, y_org, label="original", size=(600,300), titlefont=10,
    title="Reta original, amostra, modelo, CI 68% (sombreado), CI 95% (barras de erro)\nusando o desvio padrão corrigido", )
scatter!(data_x, data_y, markersize=3, label="amostra")
plot!(data_x,β[1] .+ β[2] * data_x, grid=false, yerror=2*sqrt.(Var_q),
    ribbon=sqrt.(Var_q), fillalpha=0.2, label="modelo", legend=:topleft)
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_12_1.png}


## Exemplo salário e grau de instrução

* Vamos, agora, refazer o exemplo da relação entre o salário anual médio e o grau de instrução, dos EUA.

* Dados obtidos de [US Bureau of Labor Statistics: Learn more, earn more: Education leads to higher wages, lower unemployment](https://www.bls.gov/careeroutlook/2020/data-on-display/education-pays.htm).

| Nível de instrução  | Média de salário semanal (USD) | Taxa de desemprego (%)|
| ---                  | ---  | --- |
| Doutorado            | 1883 | 1,1 |
| Profissional         | 1861 | 1,6 |
| Mestrado             | 1497 | 2,0 |
| Graduação            | 1248 | 2,2 |
| Associado*            |  887 | 2,7 |
| Graduação incompleta |  833 | 3.3 |
| Ensino Médio         |  746 | 3,7 |
| Ensino Fundamental   |  592 | 5,4 |

* *Associado* é um grau conferido em algumas instituições de nível superior, em cursos de dois a três anos.

```julia
data_y = [592, 746, 833, 887, 1248, 1497, 1861, 1883]
plot(data_y, seriestype = :scatter, xlims=(0,9), ylims=(0,2000),
    xticks=0:9, xaxis = "nível de instrução", yaxis="salário (USD)", 
    title="Média salarial semanal em função do grau de instrução", 
    titlefont=12, legend=false)
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_13_1.png}

```julia
N = 8
data_x = collect(1:N)
X = [ones(N) data_x]
β = X\data_y
s_q = √(sum(abs2,  data_y .- β[1] .- β[2] * data_x)/(N-2))
Cov_q = s_q^2 * inv(X' * X)
Var_q = [[1; x] ⋅ (Cov_q * [1; x]) for x in data_x]
```

```
8-element Vector{Float64}:
 6169.9875992063535
 4054.563279478461
 2644.280399659866
 1939.1389597505686
 1939.1389597505686
 2644.2803996598677
 4054.5632794784633
 6169.987599206355
```




* Observe que não há muita diferença ao usarmos o fator da distribuição de Student no caso do intervalo de confiança de 68\%, mas há uma diferença razoável no de 95\%.

```julia
fator = [quantile(TDist(N-2),q) for q = (0.84, 0.975)]
```

```
2-element Vector{Float64}:
 1.0839756791279644
 2.446911851144969
```



```julia
plot(data_y, seriestype = :scatter, xlims=(0,N+1), ylims=(0,2000), color=2,
    xticks=0:N+1, xaxis = "nível de instrução", yaxis="salário (USD)", 
    label="salário", title="Média salarial semanal em função do grau de instrução", 
    titlefont=12, legend=:topleft)
plot!(data_x,β[1] .+ β[2] * data_x, grid=false, yerror=fator[2]*sqrt.(Var_q),
    ribbon=fator[1]*sqrt.(Var_q), fillalpha=0.2, label="modelo", color=3, legend=:topleft)
```

\fig{images/0502-Minimos_quadrados_verossimilhanca_16_1.png}


* **Observação:** Devo ressaltar, novamente, que o eixo "nível de instrução" não está associado a uma unidade de medida relevante, sendo o posicioamento dos dados um tanto arbitrário. Portanto, o resultado acima deve ser visto com cautela, apenas para efeitos ilustrativos.


## Exercícios

1. Faça as contas de que 
$$ \operatorname{Cov}(\boldsymbol\beta) = \operatorname{Cov}(\boldsymbol\beta - \hat{\boldsymbol\beta}) = \operatorname{Cov}((X^TX)^{-1}X^T\boldsymbol{\epsilon}).
$$

2. Obtenha $\operatorname{Var}(\boldsymbol\beta)$ explicitamente em termos de $N$ e de $(x_i)_{i=1}^N$.

3. No caso de apenas duas amostras, com $x_2 - x_1 = d$ denotando a distância entre os dois pontos/momentos/condições de medição, escreva $\operatorname{Var}(\boldsymbol\beta)$ explicitamente em função de $d$ e $x_1$, observe a influência da distância $d$ na variância e encontre os limites dessa variância quanto $d\searrow 0$ e $d\nearrow \infty$.

4. Refaça os exercícios do caderno "Modelos redutíveis ao caso linear nos parâmetros e aplicações", calculando e exibindo os intervalos de confiança em relação às variáveis usadas para linearizar os problemas.


## Referências

* Morris H. DeGroot, Mark J Schervish, "Probability and Statistics", Pearson Education  2012.

* John R. Taylor, An Introduction to Error Analysis. The Study of Uncertainties in Physical Measurements. University Science Books, 1997.
