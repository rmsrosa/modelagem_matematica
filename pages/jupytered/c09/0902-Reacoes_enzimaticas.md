
@def title = "Modelagem de reações enzimática"

# {{ get_title }}

```julia
using Random
using Statistics
using LinearAlgebra
using LsqFit
using CSV
using Plots
theme(:ggplot2)
```


```julia
csv_data = CSV.File(joinpath("data", "reacao_enzimatica_figado_porco.csv"))
```

```
Error: ArgumentError: "data/reacao_enzimatica_figado_porco.csv" is not a va
lid file or doesn't exist
```



```julia
S = [csv_data[j][1] for j in 1:length(csv_data)]
v = [csv_data[j][2] for j in 1:length(csv_data)]
scatter(S,v, xlabel="S", ylabel="v", label=false,
    title = "Enzima vs velocidade", titlefont=10)
```

```
Error: UndefVarError: csv_data not defined
```



```julia
```

