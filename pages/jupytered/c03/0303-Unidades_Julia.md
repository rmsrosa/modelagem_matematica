
@def title = "Trabalhando com unidades e dimensões em Julia"

# {{ get_title }}

* [PainterQubits/Unitful.jl](https://github.com/PainterQubits/Unitful.jl): pacote para se trabalhar com quantidades, unidades e dimensões

* [jw3126/UnitfulRecipes.jl](https://github.com/jw3126/UnitfulRecipes.jl): pacote com "receitas"  para se traçar gráficos vai [JuliaPlots/Plots.jl]](https://github.com/JuliaPlots/Plots.jl).

* [rmsrosa/UnitfulBuckinghamPi.jl](https://github.com/rmsrosa/UnitfulBuckinghamPi.jl): pacote para se obter os grupos adimensionais garantidos pelo Teorema de Buckingham-Pi.

```julia
using Unitful
using UnitfulBuckinghamPi
using Plots
using UnitfulRecipes
```



## Quantidades, unidades e dimensão via Unitful.jl

* É bastante simple definir e operar com quantidades, unidades e dimensões através do pacote [PainterQubits/Unitful.jl](https://github.com/PainterQubits/Unitful.jl).

* Basta adicionarmos uma *strings prefixada com `u`*, com a unidade desejada na string. Por exemplo:


### Comprimento

```julia
h0 = 10.0u"m" # quantidade em metros
```

```
10.0 m
```



```julia
h0.val # valor da quantidade
```

```
10.0
```



```julia
unit(h0) # unidade da quantidade
```

```
m
```



```julia
dimension(h0) # dimensão da quantidade
```

```
𝐋
```



```julia
typeof(h0) # tipo
```

```
Unitful.Quantity{Float64, 𝐋, Unitful.FreeUnits{(m,), 𝐋, nothing}}
```



```julia
uconvert(u"cm", h0) # convertendo para outras unidades (de mesma dimensão)
```

```
1000.0 cm
```




### Velocidade

```julia
v0 = 3u"m/s"
```

```
3 m s⁻¹
```



```julia
deslocamento = 198u"km"; tempo = 1.8u"hr"; velocidade = deslocamento / tempo
```

```
110.0 km hr⁻¹
```




### Aceleração

```julia
g = -9.8u"m/s^2"
```

```
-9.8 m s⁻²
```




### Altura de um corpo em queda livre

```julia
h(t, h0, v0) = h0 + v0 * t + g * t^2/2
```

```
h (generic function with 1 method)
```



```julia
t = (0:0.02:2.0)u"s" # iterador com unidade
```

```
(0.0:0.02:2.0) s
```



```julia
h.(t, h0, v0)
```

```
101-element Vector{Unitful.Quantity{Float64, 𝐋, Unitful.FreeUnits{(m,), 𝐋, 
nothing}}}:
                10.0 m
            10.05804 m
            10.11216 m
            10.16236 m
            10.20864 m
  10.251000000000001 m
  10.289439999999999 m
            10.32396 m
  10.354560000000001 m
  10.381239999999998 m
                     ⋮
 -1.0694400000000037 m
 -1.3720400000000037 m
  -1.678560000000001 m
 -1.9890000000000008 m
 -2.3033599999999996 m
 -2.6216399999999993 m
 -2.9438400000000016 m
  -3.269960000000003 m
 -3.6000000000000014 m
```




### Traçando o gráfico da função sobre o intervalo dado

```julia
plot(t, t -> h(t, h0, v0))
```

\fig{images/0303-Unidades_Julia_14_1.png}


### Traçando o gráfico com os vetores/iteradores de quantidades

* Aqui, usamos o próprio `t`, assim como o vetor `h.(t, h_0, v_0)` obtido através da função.

```julia
plot(t, h.(t, h0, v0))
```

\fig{images/0303-Unidades_Julia_15_1.png}


### Embelezando o gráfico

* Observe, acima, que as unidades são automaticamente denotadas nos eixos, mas podemos fazer isso e acrescentar mais informações no compando `plot`.

* Novamente, observe que, mesmo qualificando os eixos, as unidades são automaticamente incluídas.

```julia
plot(t, h.(t, h0, v0), title="lançamento vertical de um objeto", titlefont=10,
    xlims = (0.0, 4.0), ylims=(0.0, 12.0), label = "altura do objeto", 
    xlabel = "tempo", ylabel="altura")
```

\fig{images/0303-Unidades_Julia_16_1.png}


### Operações permitidas

* Podemos somar quantidades de mesma dimensão, independente das unidades.

* Podos multiplicar quantidades, unidades quaisquer, inclusive entre si.

* Podemos multiplicar dimensões entre si.

* Podemos converter uma quantidade entre unidades diferentes de mesma dimensão.

* Oberve que dimensões são em negrito e que negrito pode ser obtida com barra invertida, seguida de "bf" (de boldface), seguida da letra desejada e, finalmente, apertando ESC. Por exemplo, a dimensão de tempo **T** se obtém, em células de código, com `\bfT` + `ESC`

```julia
1u"km" + 100u"m" + 10u"ft" + 2u"inch"
```

```
2757747//2500 m
```




* Observe que como só usamos inteiros, a conversão resultou em um número racional.

* Para obtermos um ponto flutuante, podemos ter multiplicar as unidades pelos números correspondente em ponto flutuante (ou pelo menos um deles, pois a conversão dos outros será forçada automaticamente).

```julia
1.0u"km" + 13u"inch"
```

```
1000.3302 m
```



```julia
3.0u"m" * 2.0u"1/s"
```

```
6.0 m s⁻¹
```



```julia
3.0u"m" * u"m/s^2"
```

```
3.0 m² s⁻²
```



```julia
u"𝐋" * u"𝐓"
```

```
𝐋 𝐓
```



```julia
uconvert(u"hr", 4352.0u"s")
```

```
1.208888888888889 hr
```




### Operações proibidas

* Não podemos somar quantidades com unidades diferentes.

* Não podemos somar unidades entre si, nem dimensões entre si, muito menos entre elas.

* Não podemos multiplicar uma dimensão por uma quantidade ou unidade.

* Não podemos converter uma quantidade em uma unidade de outra dimensão.

```julia
1.0u"m" + 2.0u"s"
```

```
Error: DimensionError: 1.0 m and 2.0 s are not dimensionally compatible.
```



```julia
u"m" + u"m"
```

```
Error: MethodError: no method matching +(::Unitful.FreeUnits{(m,), 𝐋, nothi
ng}, ::Unitful.FreeUnits{(m,), 𝐋, nothing})
Closest candidates are:
  +(::Any, ::Any, !Matched::Any, !Matched::Any...) at /Applications/Julia-1
.7.app/Contents/Resources/julia/share/julia/base/operators.jl:655
  +(!Matched::ChainRulesCore.Tangent{P}, ::P) where P at ~/.julia/packages/
ChainRulesCore/RbX5a/src/tangent_arithmetic.jl:146
  +(!Matched::ChainRulesCore.AbstractThunk, ::Any) at ~/.julia/packages/Cha
inRulesCore/RbX5a/src/tangent_arithmetic.jl:122
  ...
```



```julia
1u"m" * u"s" * u"𝐓"
```

```
Error: MethodError: no method matching *(::Unitful.Quantity{Int64, 𝐋 𝐓, Uni
tful.FreeUnits{(m, s), 𝐋 𝐓, nothing}}, ::Unitful.Dimensions{(Unitful.Dimens
ion{:Time}(1//1),)})
Closest candidates are:
  *(::Any, ::Any, !Matched::Any, !Matched::Any...) at /Applications/Julia-1
.7.app/Contents/Resources/julia/share/julia/base/operators.jl:655
  *(!Matched::ChainRulesCore.AbstractThunk, ::Any) at ~/.julia/packages/Cha
inRulesCore/RbX5a/src/tangent_arithmetic.jl:125
  *(::Number, !Matched::Union{SparseArrays.SparseVector{Tv, Ti}, SubArray{T
v, 1, <:SparseArrays.AbstractSparseMatrixCSC{Tv, Ti}, Tuple{Base.Slice{Base
.OneTo{Int64}}, Int64}, false}, SubArray{Tv, 1, <:SparseArrays.AbstractSpar
seVector{Tv, Ti}, Tuple{Base.Slice{Base.OneTo{Int64}}}, false}} where {Tv, 
Ti}) at /Applications/Julia-1.7.app/Contents/Resources/julia/share/julia/st
dlib/v1.7/SparseArrays/src/sparsevector.jl:1475
  ...
```



```julia
uconvert(u"g", 10u"m")
```

```
Error: DimensionError: g and m are not dimensionally compatible.
```




## Buckingham-Pi

* Podemos aproveitar a estrutura do pacote `Unitful.jl` e explorar a capacidade de metaprogramação do Julia para montar um pacote que resolva os grupos adimensionais garantidos pelo Teorema de Buckingham-Pi.

* Isso foi feito no pacote [rmsrosa/UnitfulBuckinghamPi.jl](https://github.com/rmsrosa/UnitfulBuckinghamPi.jl).

* Tudo o que precisamos fazer é registrar as quantidades, unidades, dimensões como *parâmetros* do pacote, através das macros `@setparameters` e `@addparameters`.

* Em seguida, encontramos os grupos adimensionais com a função `pi_groups()`.

* Esse pacote foi inspirado no pacote em python desenvolvido [Ian Rose](https://ian-r-rose.github.io/pages/about.html) e descrito em [Automated dimensional analysis](https://ian-r-rose.github.io/automated-dimensional-analysis.html).


### Resolvendo o período do pêndulo via UnitfulBuckinghamPi.jl

* Primeiramente, definimos os parâmetros.

* Em seguida, os registramos no pacote.

* Finalmente, obtemos os grupos adimensionais.

```julia
# parâmetros
ℓ = 2u"m" # quantidade
g = 9.8u"m/s^2" # quantidade
m = u"g" # unidade
T = u"𝐓" # dimensão
θ = u"NoDims" # "dimensão" adimensional
nothing
```


```julia
# registro
@setparameters ℓ g m T θ
```


```julia
# grupos adimensionais na forma de string
pi_groups(:String)
```

```
2-element Vector{String}:
 "g^(1//2)*ℓ^(-1//2)*T^(1//1)"
 "θ^(1//1)"
```



```julia
# grupos adimensionais na forma de expressão do Julia
Π = pi_groups(:Expr)
```

```
2-element Vector{Expr}:
 :(g ^ (1 // 2) * ℓ ^ (-1 // 2) * T ^ (1 // 1))
 :(θ ^ (1 // 1))
```




* Como $T$ é uma dimensão e os outros parâmetros em $\Pi[1]$ são quantidades, não podemos "avaliar" ("evaluate") $\Pi[1]$, pois não podemos multipicar uma dimensão por uma unidade ou quantidade. 

* Mas como $\Pi[2]$ não envolve tal multiplicação, então nesse caso não temos problema.

```julia
eval(Π[2])
```

```
NoDims
```



```julia
eval(Π[1])
```

```
Error: MethodError: no method matching *(::Unitful.Quantity{Float64, 𝐓⁻¹, U
nitful.FreeUnits{(s⁻¹,), 𝐓⁻¹, nothing}}, ::Unitful.Dimensions{(Unitful.Dime
nsion{:Time}(1//1),)})
Closest candidates are:
  *(::Any, ::Any, !Matched::Any, !Matched::Any...) at /Applications/Julia-1
.7.app/Contents/Resources/julia/share/julia/base/operators.jl:655
  *(!Matched::ChainRulesCore.AbstractThunk, ::Any) at ~/.julia/packages/Cha
inRulesCore/RbX5a/src/tangent_arithmetic.jl:125
  *(::Number, !Matched::Union{SparseArrays.SparseVector{Tv, Ti}, SubArray{T
v, 1, <:SparseArrays.AbstractSparseMatrixCSC{Tv, Ti}, Tuple{Base.Slice{Base
.OneTo{Int64}}, Int64}, false}, SubArray{Tv, 1, <:SparseArrays.AbstractSpar
seVector{Tv, Ti}, Tuple{Base.Slice{Base.OneTo{Int64}}}, false}} where {Tv, 
Ti}) at /Applications/Julia-1.7.app/Contents/Resources/julia/share/julia/st
dlib/v1.7/SparseArrays/src/sparsevector.jl:1475
  ...
```




* Para resolver esse problema com $\Pi[1]$, podemos substituir a dimensão `T=u"𝐓"` por uma unidade, que denotamos por $\tau$.

```julia
τ = u"s"
```

```
s
```



```julia
@setparameters ℓ g m τ θ
```


```julia
Π = pi_groups()
```

```
2-element Vector{Expr}:
 :(g ^ (1 // 2) * ℓ ^ (-1 // 2) * τ ^ (1 // 1))
 :(θ ^ (1 // 1))
```



```julia
eval(Π[1])
```

```
2.2135943621178655
```



```julia
eval(Π[2])
```

```
NoDims
```



```julia
dimension(eval(Π[1]))
```

```
NoDims
```




## Exercícios

1. Considere a equação $\tau = 2\pi\sqrt{\ell/g}$ para o período de pêndulo:
    1. Defina a função $\tau(\ell, g) = 2\pi \sqrt{\ell/g}$ em julia.
    1. Defina um vetor $\ell$ com unidades de comprimento variando de $10\,\texttt{cm}$ a $2\,\texttt{m}$, espaçados de um centímetro.
    1. Defina a constante $g$ como uma quantidade dimensional apropriada.
    1. Obtenha os valores correspondentes de $\tau=\tau(\ell,g)$.
    1. Trace o gráfico de $\tau$ no intervalo considerado de $\ell$.
1. Obtenha o grupo adimensional $T\ell/mv^2$ do exercício da caderno anterior através do pacote `UnitfulBuckinghamPi.jl`.
