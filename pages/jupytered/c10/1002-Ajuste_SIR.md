
@def title = "Ajustando um modelo SIR a uma epidemia de Influenza"

# {{ get_title }}

```julia
using DifferentialEquations
using Random
using Distributions: Normal, MvNormal
using Statistics
using LsqFit
using Optim
using Plots
using Images
```



* Vamos, agora, ajustar os parâmetros $\beta$ e $\gamma$ do modelo SIR aos dados de uma epidemia de Influenza em um escola de meninos (internato) no norte da Inglaterra.

* Em um total de 763 residentes, em um período de duas semanas, o número de infectados a cada dia é dado pela lista
$$ \text{Infectados a partir do dia três} = [25, 75, 228, 297, 259, 235, 192, 126, 71, 28, 9, 7].
$$

* Fonte: Brauer & Castillo-Chavez (2012).

* Há uma lista um pouco diferente de infectados, que inclui desde, o dia da primeira ocorrência:
$$ \text{Infectados a partir do dia zero} = [1, 3, 7, 25, 72, 222, 282, 256, 233, 189, 123, 70, 25, 11, 4].
$$

* Fonte: Ledder(2013)

* Vamos usar, abaixo, os primeiros dados, de Brauer & Castillo-Chavez (2012).


## Ajuste

* Nesse caso, o modelo nos dá, a partir dos dados iniciais e dos parâmetros, uma solução $(S(t), I(t), R(t))$.

* Mas só temos dados dos números de infectados $I_j$, a cada dia $j=0, \ldots, 14$.

* Assim, a nossa função objetivo só pode ser construída em cima de $I(t)$ e dos dados $(t_j, I_j)$.

* Em algumas situações, as próprias condições iniciais também podem entrar como parâmetros a serem ajustados, mas no caso mais controlado acima, vamos fixar as seguinte condições iniciais:
  * $I(0) = I_j = 1$ residente;
  * $S(0) = 763 - 1 = 762$ residentes; e
  * $R(0) = 0$ residentes.

* Definimos a taxa de evolução do sistema $(S,I)$ do modelo SIR:

```julia
# Data from Brauer & Castillo-Chavez (2012)
N = 763
dias_amostra = [3:14...]
infectados_amostra = [25, 75, 228, 297, 259, 235, 192, 126, 71, 28, 9, 7]

# Data from Ledder
#dias_amostra = [1:15...]
#infectados_amostra = [1, 3, 7, 25, 72, 222, 282, 256, 233, 189, 123, 70, 25, 11, 4]

nothing
```


```julia
plot(dias_amostra, infectados_amostra, linestyle=:dash)
scatter!(dias_amostra, infectados_amostra, color=1)
plot!(xlabel="dias", ylabel="infectados",
    title="Número de infectados a cada dia na escola no Reino Unido", titlefont=10)
```

\fig{images/1002-Ajuste_SIR_3_1.png}


## Chute inicial dos parâmetros

* Observe que a epidemia cresce e decresce rapidamente, sugerindo uma alta taxa de transmissão e um curto tempo de recuperação.

* Por conta disso, vamos chutar, inicialmente, os seguintes valores dos parâmetros:
  * $\beta =  1.5$
  * $\gamma = 0.5$ (dois dias de recuperação)
  * $\mathcal{R} = \beta/\gamma = 3.0$

```julia
ρ₀ = [1.5, 0.5]
u₀ = [N-1, 1]
tspan = (0.0, 14.0)
```

```
(0.0, 14.0)
```



```julia
function dudt_SIR!(du, u, p, t)
    β, γ = p
    S, I = u
    R = N - S - I
    I_nov = β * I * S / N # novos infectados
    du[1] = - I_nov
    du[2] = I_nov - γ * I
end
```

```
dudt_SIR! (generic function with 1 method)
```



```julia
model(t, ρ) = solve(ODEProblem(dudt_SIR!, u₀, tspan, ρ), Tsit5())(t)[2]
```

```
model (generic function with 1 method)
```



```julia
plot(dias_amostra, infectados_amostra, linestyle=:dash, label=false)
scatter!(dias_amostra, infectados_amostra, color=1, label="Dados")
tempos = 1.0:0.25:14.0
plot!(tempos, model.(tempos, Ref(ρ₀)), label="Modelo β=$(ρ₀[1]), γ=$(ρ₀[2])")
plot!(xlabel="dias", ylabel="infectados", legend=:topright,
    title="Número de infectados a cada dia na escola no Reino Unido", titlefont=10)
```

\fig{images/1002-Ajuste_SIR_7_1.png}


### Melhorando o chute inicial

* Podemos ajustar um pouco mais aumentando a taxa de transmissão:
  * $\beta =  1.8$ (taxa de contágio)
  * $\gamma = 0.5$ (dois dias de recuperação)
  * $\mathcal{R} = \beta/\gamma = 3.6$

```julia
ρ₀ = [1.8, 0.5]
```

```
2-element Vector{Float64}:
 1.8
 0.5
```



```julia
plot(dias_amostra, infectados_amostra, linestyle=:dash, label=false)
scatter!(dias_amostra, infectados_amostra, color=1, label="dados")
tempos = 1.0:0.25:14.0
plot!(tempos, model.(tempos, Ref(ρ₀)), label="Modelo β=$(ρ₀[1]), γ=$(ρ₀[2])")
plot!(xlabel="dias", ylabel="infectados", legend=:topright,
    title="Número de infectados a cada dia na escola no Reino Unido", titlefont=10)
```

\fig{images/1002-Ajuste_SIR_9_1.png}


* Assim parece mais próximo, mas vamos fazer o ajuste usando `LsqFit`, com esse novo chute inicial.


## Ajuste com LsqFit

```julia
fit = curve_fit((t,ρ) -> model.(t, Ref(ρ)), dias_amostra, infectados_amostra, ρ₀)
```

```
LsqFit.LsqFitResult{Vector{Float64}, Vector{Float64}, Matrix{Float64}, Vect
or{Int64}}([1.6682491395946721, 0.44168556986258944], [11.300158076906051, 
26.713035784328596, -16.76828047337159, -9.563924212963059, 18.957607286142
775, -11.591611941519062, -27.387005722741605, -9.670669111835466, 9.454353
054971762, 26.983336226454668, 28.314904151597133, 18.215012626217053], [10
0.56002432271706 -104.13885253850472; 313.99606007189016 -345.1498581600921
5; … ; -75.41290593639617 -143.58093947773298; -53.65106603063737 -111.8684
258497654], true, Int64[])
```



```julia
ρ = fit.param
```

```
2-element Vector{Float64}:
 1.6682491395946721
 0.44168556986258944
```



```julia
plot(dias_amostra, infectados_amostra, linestyle=:dash, label=false)
scatter!(dias_amostra, infectados_amostra, color=1, label="Dados")
tempos = 1.0:0.25:14.0
plot!(tempos, model.(tempos, Ref(ρ)), label="Modelo ajustado")
plot!(xlabel="dias", ylabel="infectados", legend=:topright,
    title="Número de infectados a cada dia na escola no Reino Unido", titlefont=10)
```

\fig{images/1002-Ajuste_SIR_12_1.png}

```julia
covar = estimate_covar(fit)
```

```
2×2 Matrix{Float64}:
 0.000861757  0.000194578
 0.000194578  0.000313972
```




## Outro chute inicial

* A escolha de um bom chute inicial é importante, como podemos ver na tentativa de ajuste abaixo, com outro chute inicial.

* Acabou achando os mesmos parâmetros, mas com mais dificuldade.

* Em outros casos, pode nem funcionar.

```julia
curve_fit((t,ρ) -> model.(t, Ref(ρ)), dias_amostra, infectados_amostra, [0.5, 0.2]).param
```

```
2-element Vector{Float64}:
 1.6682492617500464
 0.4416855505070483
```




## Ajuste com o Optim

* Também podemos usar o `Optim`.

* Ele é mais flexível (mais liberdade na escolha e na construção da função custo).

* E costuma funcionar melhor.

* Ele só não nos dá, automaticamente, a matrix de covariância.

```julia
custo(ρ) = sum(abs2, infectados_amostra - model.(dias_amostra, Ref(ρ)))
```

```
custo (generic function with 1 method)
```



```julia
ρ₀ = [1.5, 0.5]
result = optimize(custo, ρ₀)
```

```
* Status: success

 * Candidate solution
    Final objective value:     4.502256e+03

 * Found with
    Algorithm:     Nelder-Mead

 * Convergence measures
    √(Σ(yᵢ-ȳ)²)/n ≤ 1.0e-08

 * Work counters
    Seconds run:   0  (vs limit Inf)
    Iterations:    68
    f(x) calls:    145
```



```julia
Optim.minimizer(result)
```

```
2-element Vector{Float64}:
 1.6682492852905042
 0.44168581226548664
```




## Propagação de incertezas

* Usando a matrix de covariância obtida com o `LsqFit`.

* E usando o método de Monte-Carlo.

* Podemos calcular os intervalos de confiança ao longo do tempo.

```julia
num_amostras = 200
parameters = rand(MersenneTwister(21001), MvNormal(ρ, covar), num_amostras)
```

```
2×200 Matrix{Float64}:
 1.65479  1.64094   1.64311   1.64178   …  1.65732   1.6368    1.64749
 0.46985  0.435592  0.429651  0.403384     0.418683  0.469833  0.456223
```



```julia
scatter(parameters[1,:], parameters[2,:])
```

\fig{images/1002-Ajuste_SIR_19_1.png}


### Incerteza

```julia
plot(dias_amostra, infectados_amostra, linestyle=:dash, label=false)
scatter!(dias_amostra, infectados_amostra, color=1, label="Dados")
tempos = 1.0:0.25:14.0
simulations = fill(0.0, length(tempos), num_amostras)
for n in 1:num_amostras
    ρ̃ = parameters[:,n]
    simulations[:,n] = model.(tempos, Ref(ρ̃))
    plot!(tempos, simulations[:,n], label=false, alpha=0.1, color=2)
end
plot!(tempos, mean(simulations, dims=2), color=6, label="média simulações")
plot!(xlabel="dias", ylabel="infectados", legend=:topright,
    title="Número de infectados a cada dia na escola no Reino Unido", titlefont=10)
```

\fig{images/1002-Ajuste_SIR_20_1.png}


## Exercícios


1. Considere o modelo SEIR e ajuste os seus parâmetros aos dados da escola do Reino Unido considerados no texto.

2. Idem para o modelo SIAR.

3. Idem para o modelo SEIAR.
