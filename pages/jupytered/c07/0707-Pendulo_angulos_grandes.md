
@def title = "Experimentos com pêndulos"

# {{ get_title }}

```julia
using Base64
using StatsBase
using CSV
using DataFrames
```


```julia
using Images
using ImageDraw
using VideoIO
```


```julia
using Plots
```


```julia
using Optim
```


```julia
using DifferentialEquations.OrdinaryDiffEq
using DifferentialEquations.RecursiveArrayTools
```


```julia
include("../../../_assets/attachments/scripts/DisplayMovie.jl")
include("../../../_assets/attachments/scripts/VideoTracking.jl")
```

```
Main.##WeaveSandBox#293.VideoTracking
```




## Filmando um pêndulo caseiro


![pendulo](/assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4)


<video src="../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4" controls="controls" style="max-width: 730px;">
</video>

```julia
html"""<video src="../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4" controls="controls" style="max-width: 730px;">
</video>"""
```

```
HTML{String}("<video src=\"../../../_assets/attachments/img/pendulo_70cm_1_
reduzido_curto.mp4\" controls=\"controls\" style=\"max-width: 730px;\">\n</
video>")
```



```julia
filename = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4"
vd = VideoIO.load(filename)
```

```
150-element Vector{PermutedDimsArray{ColorTypes.RGB{FixedPointNumbers.N0f8}
, 2, (2, 1), (2, 1), Matrix{ColorTypes.RGB{FixedPointNumbers.N0f8}}}}:
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.584,0.541,0.502)
 RGB{N0f8}(0.584,0.541,0.502)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.584,0.541,0.502)
 RGB{N0f8}(0.584,0.541,0.502)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.584,0.541,0.502)
 RGB{N0f8}(0.584,0.541,0.502)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.584,0.541,0.502)
 RGB{N0f8}(0.584,0.541,0.502)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.584,0.541,0.502)
 RGB{N0f8}(0.584,0.541,0.502)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239
) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.58,0.537,0.498); RGB{N0f8}(0.3
02,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.58,0.537,0.498) 
RGB{N0f8}(0.58,0.537,0.498)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
1,0.11,0.102) RGB{N0f8}(0.11,0.11,0.102); RGB{N0f8}(0.227,0.184,0.184) RGB{
N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.11,0.11,0.102) RGB{N0f8}(0.11,0.11,0
.102); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{
N0f8}(0.576,0.533,0.494) RGB{N0f8}(0.576,0.533,0.494); RGB{N0f8}(0.302,0.26
3,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0
f8}(0.576,0.533,0.494)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
1,0.11,0.102) RGB{N0f8}(0.11,0.11,0.102); RGB{N0f8}(0.227,0.184,0.184) RGB{
N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.11,0.11,0.102) RGB{N0f8}(0.11,0.11,0
.102); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{
N0f8}(0.573,0.529,0.49) RGB{N0f8}(0.576,0.533,0.494); RGB{N0f8}(0.302,0.263
,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.576,0.533,0.494) RGB{N0f
8}(0.576,0.533,0.494)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
1,0.11,0.102) RGB{N0f8}(0.11,0.11,0.102); RGB{N0f8}(0.227,0.184,0.184) RGB{
N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.11,0.11,0.102) RGB{N0f8}(0.11,0.11,0
.102); … ; RGB{N0f8}(0.302,0.263,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{
N0f8}(0.569,0.525,0.486) RGB{N0f8}(0.573,0.529,0.49); RGB{N0f8}(0.302,0.263
,0.239) RGB{N0f8}(0.302,0.263,0.239) … RGB{N0f8}(0.573,0.529,0.49) RGB{N0f8
}(0.573,0.529,0.49)]
 [RGB{N0f8}(0.227,0.184,0.184) RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.1
14,0.114,0.106) RGB{N0f8}(0.114,0.114,0.106); RGB{N0f8}(0.227,0.184,0.184) 
RGB{N0f8}(0.227,0.184,0.184) … RGB{N0f8}(0.114,0.114,0.106) RGB{N0f8}(0.114
,0.114,0.106); … ; RGB{N0f8}(0.298,0.271,0.243) RGB{N0f8}(0.302,0.275,0.247
) … RGB{N0f8}(0.573,0.529,0.49) RGB{N0f8}(0.576,0.533,0.494); RGB{N0f8}(0.2
98,0.271,0.243) RGB{N0f8}(0.302,0.275,0.247) … RGB{N0f8}(0.576,0.533,0.494)
 RGB{N0f8}(0.576,0.533,0.494)]
 ⋮
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0
f8}(0.573,0.537,0.494) RGB{N0f8}(0.573,0.537,0.494); RGB{N0f8}(0.31,0.282,0
.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0f8}(0.573,0.537,0.494) RGB{N0f8}(
0.573,0.537,0.494)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0
f8}(0.573,0.537,0.494) RGB{N0f8}(0.573,0.537,0.494); RGB{N0f8}(0.31,0.282,0
.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0f8}(0.573,0.537,0.494) RGB{N0f8}(
0.573,0.537,0.494)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0
f8}(0.576,0.541,0.498) RGB{N0f8}(0.576,0.541,0.498); RGB{N0f8}(0.31,0.282,0
.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0f8}(0.576,0.541,0.498) RGB{N0f8}(
0.576,0.541,0.498)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0
f8}(0.576,0.541,0.498) RGB{N0f8}(0.576,0.541,0.498); RGB{N0f8}(0.31,0.282,0
.255) RGB{N0f8}(0.31,0.282,0.255) … RGB{N0f8}(0.576,0.541,0.498) RGB{N0f8}(
0.576,0.541,0.498)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N
0f8}(0.576,0.541,0.498) RGB{N0f8}(0.576,0.541,0.498); RGB{N0f8}(0.31,0.282,
0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N0f8}(0.576,0.541,0.498) RGB{N0f8
}(0.576,0.541,0.498)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N
0f8}(0.576,0.541,0.498) RGB{N0f8}(0.576,0.541,0.498); RGB{N0f8}(0.31,0.282,
0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N0f8}(0.576,0.541,0.498) RGB{N0f8
}(0.576,0.541,0.498)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N
0f8}(0.576,0.533,0.486) RGB{N0f8}(0.576,0.533,0.486); RGB{N0f8}(0.31,0.282,
0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N0f8}(0.576,0.533,0.486) RGB{N0f8
}(0.576,0.533,0.486)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.31,0.282,0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N
0f8}(0.576,0.533,0.486) RGB{N0f8}(0.576,0.533,0.486); RGB{N0f8}(0.31,0.282,
0.255) RGB{N0f8}(0.314,0.286,0.259) … RGB{N0f8}(0.576,0.533,0.486) RGB{N0f8
}(0.576,0.533,0.486)]
 [RGB{N0f8}(0.231,0.2,0.196) RGB{N0f8}(0.231,0.2,0.196) … RGB{N0f8}(0.133,0
.118,0.118) RGB{N0f8}(0.133,0.118,0.118); RGB{N0f8}(0.235,0.204,0.2) RGB{N0
f8}(0.235,0.204,0.2) … RGB{N0f8}(0.133,0.118,0.118) RGB{N0f8}(0.133,0.118,0
.118); … ; RGB{N0f8}(0.306,0.278,0.251) RGB{N0f8}(0.306,0.278,0.251) … RGB{
N0f8}(0.592,0.549,0.502) RGB{N0f8}(0.592,0.549,0.502); RGB{N0f8}(0.306,0.27
8,0.251) RGB{N0f8}(0.306,0.278,0.251) … RGB{N0f8}(0.592,0.549,0.502) RGB{N0
f8}(0.592,0.549,0.502)]
```



```julia
typeof(copy(vd[1]))
```

```
Matrix{RGB{N0f8}} (alias for Array{ColorTypes.RGB{FixedPointNumbers.Normed{
UInt8, 8}}, 2})
```



```julia
println("Duração do vídeo: $(VideoIO.get_duration(filename)) s")
println("Número de quadros: $(length(vd))")
println("Número médio de quadros por segundo: $(length(vd)/VideoIO.get_duration(filename))")
```

```
Duração do vídeo: 5.086 s
Número de quadros: 150
Número médio de quadros por segundo: 29.49272512780181
```



```julia
# video completo
filename_completo = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido.mov"
vd_completo = VideoIO.load(filename_completo)
println("""Duração do vídeo: $(VideoIO.get_duration(filename_completo)) s""")
println("Número de quadros: $(length(vd_completo))")
println("""Número médio de quadros por segundo: $(length(vd_completo)/VideoIO.get_duration(filename_completo))""")
```

```
Duração do vídeo: 16.45 s
Número de quadros: 493
Número médio de quadros por segundo: 29.969604863221885
```



```julia
vd[1]
```

\fig{images/0707-Pendulo_angulos_grandes_12_1.png}

```julia
DisplayMovie.display_movie("../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4", embed=false)
```

```
Error: MethodError: no method matching show(::IOContext{IOBuffer}, ::MIME{S
ymbol("text/html")}, ::String)
Closest candidates are:
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataf
rame/io.jl:268
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.AbstractData
Frame; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstract
dataframe/io.jl:130
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
s; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdata
frame/io.jl:275
  ...
```



```julia
background = convert.(RGB{Float16}, vd[1])
```

\fig{images/0707-Pendulo_angulos_grandes_14_1.png}

```julia
convert.(RGB{Float16}, vd[54])
```

\fig{images/0707-Pendulo_angulos_grandes_15_1.png}

```julia
convert.(Gray{Float16}, abs.(convert.(RGB{Float16}, vd[54]) - background))
```

\fig{images/0707-Pendulo_angulos_grandes_16_1.png}

```julia
threshold = 0.1
mask = convert.(
    Gray{Float16},
    abs.(
        convert.(RGB{Float16}, vd[54]) - 
        background
    )
) .> threshold
```

```
480×854 BitMatrix:
 0  0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0 
 1
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     1  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     1  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     1  0  0  0  0  0  0  0  0  0  0 
 0
 ⋮              ⋮              ⋮        ⋱           ⋮              ⋮       
 
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
 0  0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0 
 0
```



```julia
convert.(Gray{Float16}, mask)
```

\fig{images/0707-Pendulo_angulos_grandes_18_1.png}

```julia
labeled_components = label_components(mask)
```

```
480×854 Matrix{Int64}:
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0  18
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 ⋮              ⋮              ⋮     ⋱           ⋮              ⋮        
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
```



```julia
@which label_components(mask)
```

```
Error: LoadError: UndefVarError: @which not defined
in expression starting at /Users/rrosa/Documents/git_repositories/modelagem
_matematica/src/jupyter/c07/0707-Pendulo_angulos_grandes.ipynb:2
```



```julia
show(Docs.doc(label_components))
```

```
```
label = label_components(A; bkg = zero(eltype(A)), dims=coords_spatial(A))
label = label_components(A, connectivity; bkg = zero(eltype(A)))
```

Find the connected components in an array `A`. Components are defined as co
nnected voxels that all have the same value distinct from `bkg`, which corr
esponds to the "background" component.

Specify connectivity in one of three ways:

  * A list indicating which dimensions are used to determine connectivity. 
For example, `dims = (1,3)` would not test neighbors along dimension 2 for 
connectivity. This corresponds to just the nearest neighbors, i.e., default
 4-connectivity in 2d and 6-connectivity in 3d.
  * An iterable `connectivity` object with `CartesianIndex` elements encodi
ng the displacement of each checked neighbor.
  * A symmetric boolean array of the same dimensionality as `A`, of size 1 
or 3 along each dimension. Each entry in the array determines whether a giv
en neighbor is used for connectivity analyses. For example, in two dimensio
ns `connectivity = trues(3,3)` would include all pixels that touch the curr
ent one, even the corners.

The output `label` is an integer array, where `bkg` elements get a value of
 0.

# Examples

```jldoctest; setup=:(using ImageMorphology)
julia> A = [true false false true  false;
            true false true  true  true]
2×5 Matrix{Bool}:
 1  0  0  1  0
 1  0  1  1  1

julia> label_components(A)
2×5 Matrix{Int64}:
 1  0  0  2  0
 1  0  2  2  2

julia> label_components(A; dims=2)
2×5 Matrix{Int64}:
 1  0  0  4  0
 2  0  3  3  3
```

With `dims=2`, entries in `A` are connected if they are in the same row, bu
t not if they are in the same column.
```



```julia
colorset = distinguishable_colors(maximum(labeled_components)+1, colorant"black", dropseed = false)
```

\fig{images/0707-Pendulo_angulos_grandes_22_1.svg}

```julia
labeled_components
```

```
480×854 Matrix{Int64}:
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0  18
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     8  0  0  0  0  0  0  0  0  0  0   0
 ⋮              ⋮              ⋮     ⋱           ⋮              ⋮        
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0  …  0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
 0  0  0  0  0  0  0  0  0  0  0  0     0  0  0  0  0  0  0  0  0  0  0   0
```



```julia
coloredmask = map( n -> colorset[n+1], labeled_components)
```

\fig{images/0707-Pendulo_angulos_grandes_24_1.png}

```julia
maximum(labeled_components)
```

```
18
```



```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 1
filter!(p -> p.area ≥ min_area, components_location)
length(components_location)
```

```
18
```



```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 10
filter!(p -> p.area ≥ min_area, components_location)
length(components_location)
```

```
2
```



```julia
vd54 = copy(vd[54])
for p in components_location
    draw!(vd54, Polygon(VideoTracking.RectanglePoints(p)), colorant"red")
end
vd54
```

\fig{images/0707-Pendulo_angulos_grandes_28_1.png}

```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 100
filter!(p -> p.area ≥ min_area, components_location)
```

```
1-element Vector{Main.##WeaveSandBox#293.VideoTracking.Blob}:
 (xspan, yspan) = (644:697, 364:412)
```



```julia
vd54 = copy(vd[54])
for p in components_location
    draw!(vd54, Polygon(VideoTracking.RectanglePoints(p)), colorant"red")
end
vd54
```

\fig{images/0707-Pendulo_angulos_grandes_30_1.png}

```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 200
filter!(p -> p.area ≥ min_area, components_location)
```

```
1-element Vector{Main.##WeaveSandBox#293.VideoTracking.Blob}:
 (xspan, yspan) = (644:697, 364:412)
```



```julia
p = components_location[1]
draw(vd[54], Polygon(VideoTracking.RectanglePoints(p)), colorant"red")
```

\fig{images/0707-Pendulo_angulos_grandes_32_1.png}

```julia
filename = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4"
# filename = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido.mov"
tracks_70cm1 = VideoTracking.find_tracks(filename, lag = 10)
```

```
3-element Vector{Main.##WeaveSandBox#293.VideoTracking.Track}:
 Tracked blob with framespan nspan = 13:150

 Tracked blob with framespan nspan = 82:150

 Tracked blob with framespan nspan = 114:150
```



```julia
VideoTracking.tracks_on_video(filename, tracks_70cm1)
```


```julia
DisplayMovie.display_movie("../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto_tracked.mp4")
```

```
Error: MethodError: no method matching show(::IOContext{IOBuffer}, ::MIME{S
ymbol("text/html")}, ::String)
Closest candidates are:
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataf
rame/io.jl:268
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.AbstractData
Frame; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstract
dataframe/io.jl:130
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
s; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdata
frame/io.jl:275
  ...
```




<video src="../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto_tracked.mp4" controls="controls" style="max-width: 730px;">
</video>

```julia
isfile("../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto_tracked.mp4")
```

```
true
```




![pendulo_tracked](/assets/attachments/img/pendulo_70cm_1_reduzido_curto_tracked.mp4)

```julia
tracks_70cm1
```

```
3-element Vector{Main.##WeaveSandBox#293.VideoTracking.Track}:
 Tracked blob with framespan nspan = 13:150

 Tracked blob with framespan nspan = 82:150

 Tracked blob with framespan nspan = 114:150
```



```julia
tracks_70cm1[1].nspan
```

```
13:150
```



```julia
tracks_70cm1[1].path
```

```
138-element Vector{Main.##WeaveSandBox#293.VideoTracking.Blob}:
 (xspan, yspan) = (840:854, 177:240)
 (xspan, yspan) = (837:854, 183:247)
 (xspan, yspan) = (834:854, 183:253)
 (xspan, yspan) = (831:854, 183:256)
 (xspan, yspan) = (829:854, 179:257)
 (xspan, yspan) = (827:854, 179:258)
 (xspan, yspan) = (827:854, 179:258)
 (xspan, yspan) = (827:854, 179:258)
 (xspan, yspan) = (827:854, 180:258)
 (xspan, yspan) = (827:854, 180:257)
 ⋮
 (xspan, yspan) = (651:695, 367:410)
 (xspan, yspan) = (686:731, 350:392)
 (xspan, yspan) = (717:760, 332:373)
 (xspan, yspan) = (742:785, 314:355)
 (xspan, yspan) = (762:806, 299:337)
 (xspan, yspan) = (778:821, 284:323)
 (xspan, yspan) = (789:833, 271:310)
 (xspan, yspan) = (797:840, 262:300)
 (xspan, yspan) = (801:845, 256:294)
```



```julia
tracks_70cm1[1].path[1]
```

```
(xspan, yspan) = (840:854, 177:240)
```



```julia
plt = plot(title = "Paths of $(length(tracks_70cm1)) track(s)", titlefont = 10,
    xlims = (1,854), ylims = (1, 480),
    size = (854, 480), aspect = :equal, legend=:topright)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, getfield.(tr.path, :x), 481 .- getfield.(tr.path, :y), label="track $n")
end
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_41_1.png}

```julia
plt = plot(title = "Coordinate x of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topleft)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, getfield.(tr.path, :x), label="track $n")
end
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_42_1.png}

```julia
plt = plot(title = "Coordinate y of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topright)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, - getfield.(tr.path, :y), label="track $n")
end
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_43_1.png}

```julia
size(vd[1])
```

```
(480, 854)
```



```julia
data_x = getfield.(tracks_70cm1[1].path, :x)
data_y = size(vd[1], 1) + 1 .- getfield.(tracks_70cm1[1].path, :y)
nothing
```


```julia
n_minima = Int[]
for j in 40:length(data_x)-1
    if data_x[j-1] > data_x[j] < data_x[j+1]
        push!(n_minima, j + first(tracks_70cm1[1].nspan) - 1)
    end
end
n_minima
```

```
2-element Vector{Int64}:
  72
 125
```



```julia
plt = plot(title = "Coordinate x of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topleft)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, getfield.(tr.path, :x), label="track $n")
end
vline!(plt, n_minima, label = "minima")
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_47_1.png}

```julia
(n_minima[2:end] - n_minima[1:end-1]) / 29.5
```

```
1-element Vector{Float64}:
 1.7966101694915255
```



```julia
g = 9.8 # m/s
l = 0.7 # m
T_p = 2π * √(l / g)
```

```
1.679251908362714
```



```julia
function medias(a::Real, b::Real)
    (a ≥ 0 && b ≥ 0) || throw(ArgumentError("arguments must be nonnegative"))
    ma = (a + b)/2
    mg = sqrt(a * b)
    return ma, mg
end

function agm(a::Real, b::Real; tol::Real = 1e-10, maxiter::Int = 100)
    tol > 0 || throw(ArgumentError("tolerance must be positive"))
    maxiter > 0 || throw(ArgumentError("maximum number of iterations must be positive"))
    y1, y2 = a, b
    n = 0
    while abs(y1 - y2) > tol && n < maxiter
        y1, y2 = medias(y1, y2)
        n += 1
    end
    return (y1 + y2)/2, abs(y1 - y2), n
end
```

```
agm (generic function with 1 method)
```



```julia
θ₀ = π / 4
T_p / agm(1, cos(θ₀ / 2))[1]
```

```
1.7463772212095845
```




### Escala

* Vamos fazer ajustar um circunferência ao movimento do pêndulo, para descobrir a escala espacial.

```julia
error(u) = sum(
    abs2,
    (data_x[50:end] .- u[1]).^2 + (data_y[50:end] .- u[2]).^2 .- u[3]^2
    ) / length(data_x)
```

```
error (generic function with 1 method)
```



```julia
center_point = Optim.optimize(error, [400.0, 800.0, 500])
```

```
* Status: success

 * Candidate solution
    Final objective value:     4.747098e+06

 * Found with
    Algorithm:     Nelder-Mead

 * Convergence measures
    √(Σ(yᵢ-ȳ)²)/n ≤ 1.0e-08

 * Work counters
    Seconds run:   0  (vs limit Inf)
    Iterations:    151
    f(x) calls:    280
```



```julia
Optim.minimum(center_point)
```

```
4.74709830356046e6
```



```julia
center_nx, center_ny, radius_n = Optim.minimizer(center_point)
```

```
3-element Vector{Float64}:
 466.4527735778014
 556.9310990759983
 504.68671280430794
```



```julia
plt = plot(title = "Paths of $(length(tracks_70cm1)) track(s)", titlefont = 10,
    xlims = (1,854), ylims = (1, 600),
    size = (854, 600), aspect = :equal, legend=:topright)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, data_x, data_y, label="track $n")
end
scatter!(plt, (center_nx, center_ny), markersize = 10)
plot!(plt, 1:854, nx -> center_ny - √(radius_n^2 - (nx - center_nx)^2), linestyle = :dash)
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_56_1.png}

```julia
scale = radius_n / l # points per meter
```

```
720.9810182918685
```



```julia
data_scaled_x = (data_x .- center_nx) / scale
data_scaled_y = (data_y .- center_ny) / scale
```

```
138-element Vector{Float64}:
 -0.3949146560688051
 -0.4024818434260268
 -0.40748882991738683
 -0.4107050162655377
 -0.41378595046604316
 -0.4149888351305877
 -0.41368762932867925
 -0.4131424780860513
 -0.4137538003360941
 -0.4146578357821777
  ⋮
 -0.6432782364647945
 -0.6194322054302688
 -0.5943266060424751
 -0.5693437498002181
 -0.5457688568949555
 -0.5250531928206692
 -0.5073704469891157
 -0.4948678346300161
 -0.4867289226758497
```



```julia
function dudt_pendulum!(du, u, p, t)
    θ, ω = u
    l, g, α = p
    du[1] = ω
    du[2] = - (g / l) * sin(θ) - α * ω
end
```

```
dudt_pendulum! (generic function with 1 method)
```



```julia
g = 9.8 # 9,8 m/s^2
l = 0.7 # 70 cm
α = 0
p = [l, g, α]
θ₀ = π/6
ω₀ = 0.0
u₀ = [θ₀, ω₀]
tspan = (0.0, 5.0) # até 5 segundos
prob_pendulum = ODEProblem(dudt_pendulum!, u₀, tspan, p)
```

```
ODEProblem with uType Vector{Float64} and tType Float64. In-place: true
timespan: (0.0, 5.0)
u0: 2-element Vector{Float64}:
 0.5235987755982988
 0.0
```



```julia
sol = solve(prob_pendulum, Tsit5())
```

```
retcode: Success
Interpolation: specialized 4th order "free" interpolation
t: 32-element Vector{Float64}:
 0.0
 0.00014258482589892232
 0.0015684330848881453
 0.015826915674780374
 0.05520287578278107
 0.1186994834079412
 0.20021318382712075
 0.30591484896808435
 0.4289016061113905
 0.5569186555915231
 ⋮
 3.3360855745835023
 3.5798106962143854
 3.7899430036121617
 4.033677409516851
 4.248776802620724
 4.489724053643603
 4.712942542004417
 4.948793974730231
 5.0
u: 32-element Vector{Vector{Float64}}:
 [0.5235987755982988, 0.0]
 [0.5235987044417862, -0.0009980937402885351]
 [0.5235901656815024, -0.010978977017998427]
 [0.52272227807514, -0.11073233149660491]
 [0.5129658631370241, -0.38404064259966264]
 [0.4749871723737738, -0.8072478724104674]
 [0.3889746842716092, -1.2882714483013231]
 [0.22681173631479296, -1.7418840903686386]
 [-0.0034488642665777836, -1.9367813923292037]
 [-0.24165886108376364, -1.7139643340721666]
 ⋮
 [0.5009790261865464, 0.5577274667872847]
 [0.43312663917777644, -1.0800606609666108]
 [0.10381008615004722, -1.8977485458829486]
 [-0.33772109481584195, -1.4733220488166103]
 [-0.5219373201122955, -0.15523840887687057]
 [-0.3642267037960671, 1.384042971093617]
 [0.028819909227411733, 1.9341613541835863]
 [0.4182216594902942, 1.1572042219330516]
 [0.46971508519163835, 0.8484644252456572]
```



```julia
display(plot(sol, label = ["θ(t)" "ω(t)"]))
display(plot(sol, vars = 1, label = "θ(t)"))
```

\fig{images/0707-Pendulo_angulos_grandes_62_1.png}
\fig{images/0707-Pendulo_angulos_grandes_62_2.png}

```julia
n0 = 34
plt = plot(sol, vars = 1, label = "θ(t)")
scatter!(plt, (0:length(data_x)-n0) ./ 29.5, data_scaled_x[n0:end], label="tracked")
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_63_1.png}

```julia
df = CSV.read("../../../_assets/attachments/data/pendulo_70cm_reduzido.csv", DataFrame)
```

```
481×3 DataFrame
 Row │ nf     nx       ny
     │ Int64  Float64  Float64
─────┼─────────────────────────
   1 │    13  848.727  209.073
   2 │    14  847.362  212.843
   3 │    15  846.127  216.006
   4 │    16  844.89   218.281
   5 │    17  843.577  220.369
   6 │    18  842.701  221.178
   7 │    19  842.682  220.634
   8 │    20  842.833  220.468
  ⋮  │   ⋮       ⋮        ⋮
 475 │   487  236.224  348.115
 476 │   488  211.528  329.685
 477 │   489  190.97   312.452
 478 │   490  174.485  297.065
 479 │   491  162.013  283.93
 480 │   492  154.255  274.632
 481 │   493  150.403  268.847
               466 rows omitted
```



```julia
plt = plot(title = "Coordinate x", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, df.nx, label = nothing)
display(plt)

plt = plot(title = "Coordinate y", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, size(vd[1], 1) .+ 1 .- df.ny, label = nothing)
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_65_1.png}
\fig{images/0707-Pendulo_angulos_grandes_65_2.png}

```julia
data2_scaled_t = (df.nf[n0:end] .- df.nf[n0]) / 29.97
data2_scaled_x = (df.nx[n0:end] .- center_nx) / scale
data2_scaled_y = (size(vd[1], 1) .+ 1 .- df.ny[n0:end] .- center_ny ) / scale
display(scatter(data2_scaled_t, data2_scaled_x))
display(scatter(data2_scaled_t, data2_scaled_y))
```

\fig{images/0707-Pendulo_angulos_grandes_66_1.png}
\fig{images/0707-Pendulo_angulos_grandes_66_2.png}

```julia
n_minima2 = Int[]
for j in 40:length(df.nx)-1
    if df.nx[j-1] > df.nx[j] < df.nx[j+1]
        push!(n_minima2, j + df.nf[1] - 1)
    end
end
n_minima2
```

```
8-element Vector{Int64}:
  72
 125
 178
 231
 283
 336
 389
 441
```



```julia
(n_minima2[2:end] - n_minima2[1:end-1])/30
```

```
7-element Vector{Float64}:
 1.7666666666666666
 1.7666666666666666
 1.7666666666666666
 1.7333333333333334
 1.7666666666666666
 1.7666666666666666
 1.7333333333333334
```



```julia
sum(n_minima2[2:end] - n_minima2[1:end-1])/7/30
```

```
1.7571428571428571
```



```julia
plt = plot(title = "Coordinate x", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, df.nx, label = "data")
vline!(plt, n_minima2, label = "minima")
display(plt)
```

\fig{images/0707-Pendulo_angulos_grandes_70_1.png}

```julia
g = 9.8 # 9,8 m/s^2
l = 0.7 # 70 cm
α = 0
p = [l, g, α]
θ₀ = π/6
ω₀ = 0.0
u₀ = [θ₀, ω₀]
tspan2 = (0.0, 16.45)
prob_pendulum2 = ODEProblem(dudt_pendulum!, u₀, tspan2, p)
```

```
ODEProblem with uType Vector{Float64} and tType Float64. In-place: true
timespan: (0.0, 16.45)
u0: 2-element Vector{Float64}:
 0.5235987755982988
 0.0
```



```julia
VideoIO.get_duration("../../../_assets/attachments/img/pendulo_70cm_1_reduzido.mov")
```

```
16.45
```



```julia
θ₀ = π / 6
α = 0.0 #-0.1
remake(prob_pendulum2; u0 = [θ₀, 0.0], p = [l, g, α])
sol2 = solve(prob_pendulum2, Tsit5(); saveat = 1/29.87)
data2_scaled_x[1:10] .- sol2(data2_scaled_t)[1,1:10]
#length(sol[1,:])
#sol(data2_scaled_t)[1,:]
sol(data2_scaled_t)
```

```
t: 448-element Vector{Float64}:
  0.0
  0.033366700033366704
  0.06673340006673341
  0.1001001001001001
  0.13346680013346682
  0.16683350016683351
  0.2002002002002002
  0.2335669002335669
  0.26693360026693363
  0.3003003003003003
  ⋮
 14.647981314647982
 14.68134801468135
 14.714714714714715
 14.748081414748082
 14.78144811478145
 14.814814814814815
 14.848181514848182
 14.88154821488155
 14.914914914914915
u: 448-element Vector{Vector{Float64}}:
 [0.5235987755982988, 0.0]
 [0.5197064819391027, -0.23304144136133448]
 [0.5080822001687986, -0.46293026915798463]
 [0.4888836986777477, -0.6865155884298502]
 [0.4623737395236549, -0.9006563907399179]
 [0.4289196227578826, -1.102237149997166]
 [0.38899141026001216, -1.2882025121646739]
 [0.3431598607272918, -1.4556077279088206]
 [0.29209180679930413, -1.6016605695348598]
 [0.2365413522541491, -1.723835233508896]
 ⋮
 [28090.076115343432, 34867.02594964842]
 [28488.189596449276, 35312.03523725597]
 [28890.51197192504, 35761.24074459752]
 [29297.072746048078, 36214.66840753737]
 [29707.901529797746, 36672.34420745299]
 [30123.028031235135, 37134.294248783204]
 [30542.482064244345, 37600.54470140422]
 [30966.293547238365, 38071.1217838308]
 [31394.492499643053, 38546.05182533289]
```



```julia
plot(data2_scaled_t, sol2(data2_scaled_t)[1,:], label = "ODE", ylims=(-1,1))
scatter!(data2_scaled_t, data2_scaled_x, label = "data")
```

\fig{images/0707-Pendulo_angulos_grandes_74_1.png}

```julia
function ddu_pendulum!(ddu, du, u, p, t)
    θ = u[1]
    ω = du[1]
    l, g, α = p
    ddu[1] = - (g / l) * sin(θ) - α * ω
end
```

```
ddu_pendulum! (generic function with 1 method)
```



```julia
θ₀ = π / 6
ω₀ = 0.0
α = 0.05
l = 0.72
p = [l, g, α]
prob_pendulum_2nd = SecondOrderODEProblem(ddu_pendulum!, [ω₀], [θ₀], tspan2, p)
sol_2nd = solve(prob_pendulum_2nd)
sol_2nd.retcode
```

```
:Success
```



```julia
plot(data2_scaled_t, sol_2nd(data2_scaled_t)[2,:], label = "ODE", ylims=(-1,1))
scatter!(data2_scaled_t, data2_scaled_x, label = "data")
```

\fig{images/0707-Pendulo_angulos_grandes_77_1.png}

```julia
prob_rmk = remake(prob_pendulum_2nd; u0 = ArrayPartition([0.0], [θ₀]), p = [l, g, α])
sol_rmk = solve(prob_rmk)
```

```
retcode: Success
Interpolation: specialized 4th order "free" interpolation
t: 81-element Vector{Float64}:
  0.0
  0.00014665867806746294
  0.0016132454587420922
  0.016279113265488386
  0.05646261671975408
  0.1210661584895972
  0.20394094443174465
  0.3114428714445593
  0.4361696895237713
  0.5660126318578794
  ⋮
 14.75710393351784
 14.975837376148979
 15.220528314715068
 15.4357394488737
 15.68199060915447
 15.899891437531256
 16.14498715319801
 16.367029104543224
 16.45
u: 81-element Vector{RecursiveArrayTools.ArrayPartition{Float64, Tuple{Vect
or{Float64}, Vector{Float64}}}}:
 ([0.0], [0.5235987755982988])
 ([-0.0009980900796482302], [0.523598702408922])
 ([-0.010978532676025766], [0.5235899199226164])
 ([-0.1106856765365273], [0.5226974863498236])
 ([-0.38131432847714974], [0.5127947624143487])
 ([-0.7977890197442177], [0.47454089689923107])
 ([-1.2683562493326956], [0.38830121752424207])
 ([-1.7078585641373936], [0.22627879083954466])
 ([-1.8891348315194052], [-0.0020668325633489415])
 ([-1.6627067086680574], [-0.2371150363762909])
 ⋮
 ([0.4910364935793956], [-0.3359400903659479])
 ([1.2181506703554332], [-0.13835433828158172])
 ([1.1421230770911266], [0.17172703098371234])
 ([0.3513281719783554], [0.34094589979533435])
 ([-0.7548621921063656], [0.2874525904670078])
 ([-1.2735027973864756], [0.053843800899205596])
 ([-0.9326114124256897], [-0.23637451107073632])
 ([-0.008988723570449997], [-0.34667806133206513])
 ([0.36875503620207184], [-0.3316312175041112])
```



```julia
function objective(β)
    g = 9.8
    ω₀ = 0.0
    θ₀, l, α = β
    p = [l, g, α]
    tspan2 = (0.0, 16.45)
    prob = remake(prob_pendulum_2nd, u0 = ArrayPartition([0.0], [θ₀]), p = [l, g, α])
    sol = solve(prob)
    #prob = SecondOrderODEProblem(ddu_pendulum!, [ω₀], [θ₀], tspan2, p)
    #sol = solve(prob)
    return mse(data2_scaled_x, sol(data2_scaled_t)[2,:])
end
```

```
objective (generic function with 1 method)
```



```julia
res = Optim.optimize(objective, [π / 3, 0.7, 0.0])
```

```
* Status: success

 * Candidate solution
    Final objective value:     1.323686e-03

 * Found with
    Algorithm:     Nelder-Mead

 * Convergence measures
    √(Σ(yᵢ-ȳ)²)/n ≤ 1.0e-08

 * Work counters
    Seconds run:   0  (vs limit Inf)
    Iterations:    71
    f(x) calls:    135
```



```julia
θ₀, l, α = Optim.minimizer(res)
```

```
3-element Vector{Float64}:
 0.5566387971294271
 0.7420963830767683
 0.03745649548388733
```



```julia
π / θ₀
```

```
5.6438621773956665
```



```julia
θ₀ - π / 5.6529
```

```
0.0008899507691884079
```



```julia
prob_rmk = remake(prob_pendulum_2nd, u0 = ArrayPartition([0.0], [θ₀]), p = [l, g, α])
```

```
ODEProblem with uType RecursiveArrayTools.ArrayPartition{Float64, Tuple{Vec
tor{Float64}, Vector{Float64}}} and tType Float64. In-place: true
timespan: (0.0, 16.45)
u0: ([0.0], [0.5566387971294271])
```



```julia
sol_2nd = solve(prob_rmk)
sol_2nd.retcode
```

```
:Success
```



```julia
plot(data2_scaled_t, sol_2nd(data2_scaled_t)[2,:], label = "ODE", ylims=(-1,1))
scatter!(data2_scaled_t, data2_scaled_x, label = "data")
```

\fig{images/0707-Pendulo_angulos_grandes_86_1.png}
