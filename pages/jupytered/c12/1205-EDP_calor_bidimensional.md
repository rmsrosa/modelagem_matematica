
@def title = "Equação do calor em duas dimensões espaciais"

# {{ get_title }}

```julia
using DifferentialEquations
using Plots
```



## Aproximação em diferenças finitas do laplaciano

* Vamos considerar o caso de condições de contorno homogêneas do tipo Dirichlet, i.e. $u|_{\partial\Omega} = 0$.

* Usaremos uma malha $\{(x_i,y_j)\}_{i,j}$ de pontos em um domínio $\Omega = (0,L_x)\times(0,L_y)$.

* No interior, vamos aproximar
$$ \begin{align*}
  \Delta u(x,y) & = u_{xx}(x,y) + u_{yy}(x,y) \\
  & \approx \frac{u(x+h_x,y) - 2u(x,y) + u(x-h_x,y)}{h_x^2} + \frac{u(x, y+h_y) - 2u(x,y) + u(x,y-h_y)}{h_y^2}.
  \end{align*}
$$

* Julia, assim como o Fortran, guarda *arrays* na memória em formato *column-major*, o que significa que eles são guardados coluna a coluna, ou seja, a primeira coluna inteira, de forma contígua, seguida da segunda coluna, e assim por diante. 

* Nesse sentido, é diferente do Python, que guarda cada linha de maneira contígua, chamada *row-major*.

* Por esse motivo, é mais rápido fazer o *loop* duplo com o *loop* interior percorrendo as linhas e o *loop* exterior, as colunas.

```julia
function δ²(u::Matrix{Float64}, hx2::Float64, hy2::Float64, ::Val{:dir})
    n, m = size(u)
    ddu = zero(u)
    for j = 2:m-1
        for i = 2:n-1
            ddu[i,j] = (u[i,j+1] - 2u[i,j] + u[i,j-1])/hx2 + 
                (u[i+1,j] - 2u[i,j] + u[i-1,j])/hy2
        end
    end
    return ddu
end
```

```
δ² (generic function with 1 method)
```



```julia
function dudt_calor2d!(dudt::Matrix{Float64}, u::Matrix{Float64}, p::Vector{Float64}, t::Float64)
    κ, hx2, hy2 = p
    du = δ²(u, hx2, hy2, Val(:dir))
    dudt .= κ * du
    return nothing
end
```

```
dudt_calor2d! (generic function with 1 method)
```



```julia
κ = 0.01 # coeficiente de difusão térmica
Lx = 2π # comprimento na direção x do domínio [0,Lx]×[0,Ly]
Ly = π # comprimento na direção y do domínio [0,Lx]×[0,Ly]
Nx = 60 # número de pontos da malha na direção x
Ny = 40 # número de pontos da malha na direção x
hx = Lx/(Nx-1) # comprimento de cada partição da malha em x
hy = Ly/(Ny-1) # comprimento de cada partição da malha em y
x = range(0.0, Lx, length=Nx) # discretização espacial na direção x
y = range(0.0, Ly, length=Ny) # discretização espacial na direção y
σ = 0.5
u₀ = exp.(-(y .- Ly/2).^2/2/σ^2) * exp.(-(x .- Lx/2).^2/2/σ^2)' # condição inicial
u₀[1,:] .= u₀[end,:] .= 0 # zero nos bordos laterais
u₀[:,1] .= u₀[:,end] .= 0 # zero nos bordos inferior e superior
p = [κ, hx^2, hy^2] # parâmetros
Tf = 12 # tempo final
τ = 0.1 # intervalos de tempo
tspan = (0.0,Tf) # intervalo de tempo
prob = ODEProblem(dudt_calor2d!, u₀, tspan, p, saveat = τ)
nothing
```


```julia
surface(x, y, u₀, xlabel="x", ylabel="y", zlabel="temperatura", 
    title="Distribuição inicial de temperatura", titlefont=10)
```

\fig{images/1205-EDP_calor_bidimensional_5_1.png}

```julia
sol = solve(prob, Tsit5())
sol.retcode
```

```
:Success
```



```julia
anim = @animate for (t,u) in zip(sol.t, sol.u)
    surface(u, zlims=(-0.1, 1.1), label="t=$(round(t,digits=2))", clims=(0.0, 1.0),
        title="Evolução equação do calor bidimensional (κ=$κ)", titlefont=10)
end
gif(anim, "../../../_assets/attachments/img/anim_calor2D_a.gif", fps = 20)
nothing
```



![heat2d](/assets/attachments/img/anim_calor2D_a.gif)

```julia
anim = @animate for (t,u) in zip(sol.t, sol.u)
    contourf(u, label="t=$(round(t,digits=2))", clims=(-0.2, 1.0),
        title="Evolução equação do calor bidimensional (κ=$κ)", titlefont=10)
end
gif(anim, "../../../_assets/attachments/img/anim_calor2D_b.gif", fps = 20)
nothing
```



![heat2dcontour](/assets/attachments/img/anim_calor2D_b.gif)

```julia
anim = @animate for (t,u) in zip(sol.t, sol.u)
    heatmap(u, label="t=$(round(t,digits=2))", clims=(-0.2, 1.0),
        title="Evolução equação do calor bidimensional (κ=$κ)", titlefont=10)
end
gif(anim, "../../../_assets/attachments/img/anim_calor2D_c.gif", fps = 20)
nothing
```



![heat2dheatmap](/assets/attachments/img/anim_calor2D_c.gif)
