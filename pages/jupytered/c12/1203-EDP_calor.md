
@def title = "Equação do calor unidimensional"

# {{ get_title }}

* Vamos considerar, agora, a equação do calor
$$  u_t = \kappa u_{xx}
$$

```julia
using DifferentialEquations
using Plots
```



## Equação do calor

* A solução fundamental da equação do calor unidimensional é
$$ K(t,x) = \frac{1}{\sqrt{4\kappa\pi t}} e^{x^2/(4\kappa t)}.
$$

* Observe que, para cada $t>0$, a função $x\mapsto K(t,x)$ é uma Gaussiana, com desvio padrão aumentando com $t$, ou seja, a solução se espalha, correspondendo a uma difusão na distribuição de $u$.

* A solução com condição inicial $u(0,x) = u_0(x)$ é dada pela convolução
$$ u(t,x) = \int_{-\infty}^\infty K(t,x-\xi)u_0(\xi)\;d\xi = \frac{1}{\sqrt{4\kappa\pi t}} \int_{-\infty}^\infty e^{(x-\xi)^2/(4\kappa t)}u_0(\xi)\;d\xi.
$$


## Simulação

* Vamos simular numericamente a evolução em um intervalo $I=[0,L]$, com condições de contorno de Dirichlet homogêneas, i.e. $u(0)=u(L)=0$.

* Na interpretação de $u$ como temperatura, e assumindo uma escala em graus Celsius, isso corresponde a mantermos a temperatura nos extremos a zero grau.

```julia
function Δ(u, h2, ::Val{:dir})
    ddu = zero(u)
    for j = 2:length(u)-1
        ddu[j] = (u[j+1] - 2u[j] + u[j-1])/h2
    end
    return ddu
end
```

```
Δ (generic function with 1 method)
```



```julia
function dudt_calor!(dudt, u, p, t)
    ν, h2 = p
    ddu = Δ(u, h2, Val(:dir))
    dudt .= ν * ddu
    return nothing
end
```

```
dudt_calor! (generic function with 1 method)
```



```julia
κ = 0.5 # coeficiente de difusão térmica
L = 2π # comprimento do intervalo [0,L]
N = 60 # número de pontos da malha
h = L/(N-1) # comprimento de cada partição na malha
x = range(0.0, L, length=N) # discretização do intervalo [0,L] com N pontos, incluindo os extremos
u₀ = exp.(-(x.-L/2).^2) .- exp(-L^2/4) # condição inicial
p = [κ, h^2] # parâmetros
Tf = 12 # tempo final
τ = 0.1 # intervalos de tempo
tspan = (0.0,Tf) # intervalo de tempo
prob = ODEProblem(dudt_calor!, u₀, tspan, p, saveat = τ)
nothing
```


```julia
plot(x, u₀, title="Condição inicial", titlefont=10, xlabel="x", ylabel="u")
```

\fig{images/1203-EDP_calor_5_1.png}

```julia
sol = solve(prob, Tsit5())
sol.retcode
```

```
:Success
```



```julia
anim = @animate for (t,u) in zip(sol.t, sol.u)
    plot(x, u, ylims=(-0.1, 1.1), label="t=$(round(t,digits=2))",
        title="Evolução equação do calor unidimensional (κ=$κ)", titlefont=10,
        xlabel="x", ylabel="u")
end
gif(anim, "../../../_assets/attachments/img/anim_calor1D_a.gif", fps = 20)
nothing
```



![heat1d](/assets/attachments/img/anim_calor1D_a.gif)


### Outra simulação

* Aumentando o coeficiente de difusão térmica.

```julia
κ = 2.0
p = [κ, h^2] # parâmetros
prob = ODEProblem(dudt_calor!, u₀, tspan, p, saveat = τ)
sol = solve(prob, Tsit5())
sol.retcode
```

```
:Success
```



```julia
anim = @animate for (t,u) in zip(sol.t, sol.u)
    plot(x, u, ylims=(-0.1, 1.1), label="t=$(round(t,digits=2))",
        title="Evolução equação do calor unidimensional (κ=$κ)", titlefont=10,
        xlabel="x", ylabel="u")
end
gif(anim, "../../../_assets/attachments/img/anim_calor1D_b.gif", fps = 20)
nothing
```



![heat1dB](/assets/attachments/img/anim_calor1D_b.gif)


## Exercicios:

1. Simular a equação de difusão com condições de contorno Neumann.
