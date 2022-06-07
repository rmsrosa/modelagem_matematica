
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

```
Your GR installation is incomplete. Rerunning build step for GR package.
Error: Failed to precompile Plots [91a5bcdd-55d7-5caf-9e0b-520d859cae80] to
 /Users/rmsrosa/.julia/compiled/v1.7/Plots/jl_vGXhqI.
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
Main.##WeaveSandBox#292.VideoTracking
```



```julia
filename = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4"
vd = VideoIO.load(filename)
nothing
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
filename_completo = "img/pendulo_70cm_1_reduzido.mov"
vd_completo = VideoIO.load(filename_completo)
println("""Duração do vídeo: $(VideoIO.get_duration(filename_completo)) s""")
println("Número de quadros: $(length(vd_completo))")
println("""Número médio de quadros por segundo: $(length(vd_completo)/VideoIO.get_duration(filename_completo))""")
```

```
Error: Could not open img/pendulo_70cm_1_reduzido.mov. avformat_open_input 
error code -2
```



```julia
vd[1]
```

\fig{images/0707-Pendulo_angulos_grandes_11_1.png}

```julia
DisplayMovie.display_movie("../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4")
```

```
Error: MethodError: no method matching show(::IOContext{IOBuffer}, ::MIME{S
ymbol("text/html")}, ::String)
Closest candidates are:
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.GroupedDataF
rame) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataframe/io.jl:291
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataf
rame/io.jl:268
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.AbstractData
Frame; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstract
dataframe/io.jl:130
  ...
```



```julia
background = convert.(RGB{Float16}, vd[1])
```

\fig{images/0707-Pendulo_angulos_grandes_13_1.png}

```julia
convert.(RGB{Float16}, vd[54])
```

\fig{images/0707-Pendulo_angulos_grandes_14_1.png}

```julia
convert.(Gray{Float16}, abs.(convert.(RGB{Float16}, vd[54]) - background))
```

\fig{images/0707-Pendulo_angulos_grandes_15_1.png}

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

\fig{images/0707-Pendulo_angulos_grandes_17_1.png}

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
in expression starting at /Users/rmsrosa/Documents/git-repositories/modelag
em_matematica/src/jupyter/c07/0707-Pendulo_angulos_grandes.ipynb:2
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

\fig{images/0707-Pendulo_angulos_grandes_21_1.svg}

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

\fig{images/0707-Pendulo_angulos_grandes_23_1.png}

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

\fig{images/0707-Pendulo_angulos_grandes_27_1.png}

```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 100
filter!(p -> p.area ≥ min_area, components_location)
```

```
1-element Vector{Main.##WeaveSandBox#292.VideoTracking.Blob}:
 Blob Object
  Centroid coordinates: (x, y) = (670.0722713864307, 387.4906588003933)
  Span values: (xspan, yspan) = (644:697, 364:412)
  Occupied: area = 2034
```



```julia
vd54 = copy(vd[54])
for p in components_location
    draw!(vd54, Polygon(VideoTracking.RectanglePoints(p)), colorant"red")
end
vd54
```

\fig{images/0707-Pendulo_angulos_grandes_29_1.png}

```julia
components_location = VideoTracking.locate_components(labeled_components)
min_area = 200
filter!(p -> p.area ≥ min_area, components_location)
```

```
1-element Vector{Main.##WeaveSandBox#292.VideoTracking.Blob}:
 Blob Object
  Centroid coordinates: (x, y) = (670.0722713864307, 387.4906588003933)
  Span values: (xspan, yspan) = (644:697, 364:412)
  Occupied: area = 2034
```



```julia
p = components_location[1]
draw(vd[54], Polygon(VideoTracking.RectanglePoints(p)), colorant"red")
```

\fig{images/0707-Pendulo_angulos_grandes_31_1.png}

```julia
filename = "../../../_assets/attachments/img/pendulo_70cm_1_reduzido_curto.mp4"
tracks_70cm1 = VideoTracking.find_tracks(filename)
```

```
1-element Vector{Main.##WeaveSandBox#292.VideoTracking.Track}:
 Tracked blob with framespan nspan = 13:55
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
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.GroupedDataF
rame) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataframe/io.jl:291
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.DataFrameRow
; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstractdataf
rame/io.jl:268
  show(::IO, ::MIME{Symbol("text/html")}, !Matched::DataFrames.AbstractData
Frame; summary, eltypes) at ~/.julia/packages/DataFrames/zqFGs/src/abstract
dataframe/io.jl:130
  ...
```



```julia
tracks_70cm1
```

```
1-element Vector{Main.##WeaveSandBox#292.VideoTracking.Track}:
 Tracked blob with framespan nspan = 13:55
```



```julia
tracks_70cm1[1].nspan
```

```
13:55
```



```julia
tracks_70cm1[1].path
```

```
43-element Vector{Main.##WeaveSandBox#292.VideoTracking.Blob}:
 Blob Object
  Centroid coordinates: (x, y) = (849.1062271062272, 208.7948717948718)
  Span values: (xspan, yspan) = (840:854, 177:240)
  Occupied: area = 546

 Blob Object
  Centroid coordinates: (x, y) = (847.6581769436997, 214.25067024128685)
  Span values: (xspan, yspan) = (837:854, 183:247)
  Occupied: area = 746

 Blob Object
  Centroid coordinates: (x, y) = (846.3590285110877, 217.86061246040126)
  Span values: (xspan, yspan) = (834:854, 183:253)
  Occupied: area = 947

 Blob Object
  Centroid coordinates: (x, y) = (845.1462585034013, 220.17942176870747)
  Span values: (xspan, yspan) = (831:854, 183:256)
  Occupied: area = 1176

 Blob Object
  Centroid coordinates: (x, y) = (843.8523297491039, 222.40071684587812)
  Span values: (xspan, yspan) = (829:854, 179:257)
  Occupied: area = 1395

 Blob Object
  Centroid coordinates: (x, y) = (843.0366013071896, 223.26797385620915)
  Span values: (xspan, yspan) = (827:854, 179:258)
  Occupied: area = 1530

 Blob Object
  Centroid coordinates: (x, y) = (843.1176084099868, 222.32982917214193)
  Span values: (xspan, yspan) = (827:854, 179:258)
  Occupied: area = 1522

 Blob Object
  Centroid coordinates: (x, y) = (843.275722932078, 221.93678547410894)
  Span values: (xspan, yspan) = (827:854, 179:258)
  Occupied: area = 1487

 Blob Object
  Centroid coordinates: (x, y) = (843.2882273342354, 222.37753721244925)
  Span values: (xspan, yspan) = (827:854, 180:258)
  Occupied: area = 1478

 Blob Object
  Centroid coordinates: (x, y) = (843.3896648044692, 223.02932960893855)
  Span values: (xspan, yspan) = (827:854, 180:257)
  Occupied: area = 1432

 ⋮
 Blob Object
  Centroid coordinates: (x, y) = (837.734181689643, 233.8221986567692)
  Span values: (xspan, yspan) = (813:854, 176:276)
  Occupied: area = 2829

 Blob Object
  Centroid coordinates: (x, y) = (836.0925600468659, 241.8945518453427)
  Span values: (xspan, yspan) = (807:854, 178:289)
  Occupied: area = 3414

 Blob Object
  Centroid coordinates: (x, y) = (832.6118686868687, 255.65984848484848)
  Span values: (xspan, yspan) = (802:854, 184:306)
  Occupied: area = 3960

 Blob Object
  Centroid coordinates: (x, y) = (804.2969808995687, 302.09303758471964)
  Span values: (xspan, yspan) = (782:827, 281:325)
  Occupied: area = 1623

 Blob Object
  Centroid coordinates: (x, y) = (778.301724137931, 322.82635467980293)
  Span values: (xspan, yspan) = (756:802, 301:345)
  Occupied: area = 1624

 Blob Object
  Centroid coordinates: (x, y) = (747.879472693032, 345.85310734463275)
  Span values: (xspan, yspan) = (726:771, 324:367)
  Occupied: area = 1593

 Blob Object
  Centroid coordinates: (x, y) = (711.4871007371007, 367.28132678132675)
  Span values: (xspan, yspan) = (690:735, 345:390)
  Occupied: area = 1628

 Blob Object
  Centroid coordinates: (x, y) = (670.0882352941177, 387.8469387755102)
  Span values: (xspan, yspan) = (648:693, 366:411)
  Occupied: area = 1666

 Blob Object
  Centroid coordinates: (x, y) = (624.7634730538922, 405.8550898203593)
  Span values: (xspan, yspan) = (603:648, 384:428)
  Occupied: area = 1670
```



```julia
tracks_70cm1[1].path[1]
```

```
Blob Object
  Centroid coordinates: (x, y) = (849.1062271062272, 208.7948717948718)
  Span values: (xspan, yspan) = (840:854, 177:240)
  Occupied: area = 546
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

```
Error: UndefVarError: plot not defined
```



```julia
plt = plot(title = "Coordinate x of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topleft)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, getfield.(tr.path, :x), label="track $n")
end
display(plt)
```

```
Error: UndefVarError: plot not defined
```



```julia
plt = plot(title = "Coordinate y of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topright)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, - getfield.(tr.path, :y), label="track $n")
end
display(plt)
```

```
Error: UndefVarError: plot not defined
```



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
Int64[]
```



```julia
plt = plot(title = "Coordinate x of $(length(tracks_70cm1)) tracks", titlefont = 10, legend=:topleft)
for (n, tr) in enumerate(tracks_70cm1)
    scatter!(plt, tr.nspan, getfield.(tr.path, :x), label="track $n")
end
vline!(plt, n_minima, label = "minima")
display(plt)
```

```
Error: UndefVarError: plot not defined
```



```julia
(n_minima[2:end] - n_minima[1:end-1]) / 29.5
```

```
Float64[]
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
    Final objective value:     0.000000e+00

 * Found with
    Algorithm:     Nelder-Mead

 * Convergence measures
    √(Σ(yᵢ-ȳ)²)/n ≤ 1.0e-08

 * Work counters
    Seconds run:   0  (vs limit Inf)
    Iterations:    0
    f(x) calls:    5
```



```julia
Optim.minimum(center_point)
```

```
0.0
```



```julia
center_nx, center_ny, radius_n = Optim.minimizer(center_point)
```

```
3-element Vector{Float64}:
 400.0
 800.0
 500.0
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

```
Error: UndefVarError: plot not defined
```



```julia
scale = radius_n / l # points per meter
```

```
714.2857142857143
```



```julia
data_scaled_x = (data_x .- center_nx) / scale
data_scaled_y = (data_y .- center_ny) / scale
```

```
43-element Vector{Float64}:
 -0.7389128205128205
 -0.7465509383378015
 -0.7516048574445617
 -0.7548511904761904
 -0.7579610035842294
 -0.7591751633986928
 -0.7578617608409987
 -0.7573114996637526
 -0.7579285520974289
 -0.7588410614525138
  ⋮
 -0.7739510781194767
 -0.7852523725834797
 -0.8045237878787878
 -0.8695302526186075
 -0.8985568965517241
 -0.9307943502824857
 -0.9607938574938573
 -0.9895857142857141
 -1.0147971257485031
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
 0.3059148580456768
 0.4289016257510082
 0.556918677400161
 ⋮
 3.336085982741865
 3.5798111245515645
 3.789943545334064
 4.033677951692835
 4.248777445772274
 4.4897245954065665
 4.712943195270591
 4.948794481749135
 5.0
u: 32-element Vector{Vector{Float64}}:
 [0.5235987755982988, 0.0]
 [0.5235987044417862, -0.000998093740288535]
 [0.5235901656815024, -0.01097897701799843]
 [0.52272227807514, -0.1107323314966049]
 [0.5129658631370241, -0.3840406425996626]
 [0.4749871723737738, -0.8072478724104671]
 [0.38897468427160925, -1.2882714483013225]
 [0.22681172050256487, -1.7418841189469372]
 [-0.0034489023047863383, -1.936781391381158]
 [-0.24165889846355013, -1.7139642610036754]
 ⋮
 [0.5009792538381039, 0.5577247215218519]
 [0.43312617648070506, -1.0800631782759451]
 [0.10380905787269706, -1.8977493321783012]
 [-0.33772189369520583, -1.4733195325856954]
 [-0.5219374197998773, -0.15523391826013316]
 [-0.36422595366369465, 1.3840456727974355]
 [0.02882117308366698, 1.9341610901039223]
 [0.41822224613478143, 1.157201337942282]
 [0.4697150850563418, 0.8484644241876123]
```



```julia
```


```julia
display(plot(sol, label = ["θ(t)" "ω(t)"]))
display(plot(sol, vars = 1, label = "θ(t)"))
```

```
Error: UndefVarError: plot not defined
```



```julia
n0 = 34
plt = plot(sol, vars = 1, label = "θ(t)")
scatter!(plt, (0:length(data_x)-n0) ./ 29.5, data_scaled_x[n0:end], label="tracked")
display(plt)
```

```
Error: UndefVarError: plot not defined
```



```julia
df = CSV.read("data/pendulo_70cm_reduzido.csv", DataFrame)
```

```
Error: ArgumentError: "data/pendulo_70cm_reduzido.csv" is not a valid file 
or doesn't exist
```



```julia
plt = plot(title = "Coordinate x", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, df.nx, label = nothing)
display(plt)

plt = plot(title = "Coordinate y", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, size(vd[1], 1) .+ 1 .- df.ny, label = nothing)
display(plt)
```

```
Error: UndefVarError: plot not defined
```



```julia
data2_scaled_t = (df.nf[n0:end] .- df.nf[n0]) / 29.97
data2_scaled_x = (df.nx[n0:end] .- center_nx) / scale
data2_scaled_y = (size(vd[1], 1) .+ 1 .- df.ny[n0:end] .- center_ny ) / scale
display(scatter(data2_scaled_t, data2_scaled_x))
display(scatter(data2_scaled_t, data2_scaled_y))
```

```
Error: UndefVarError: df not defined
```



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
Error: UndefVarError: df not defined
```



```julia
(n_minima2[2:end] - n_minima2[1:end-1])/30
```

```
Float64[]
```



```julia
sum(n_minima2[2:end] - n_minima2[1:end-1])/7/30
```

```
0.0
```



```julia
plt = plot(title = "Coordinate x", titlefont = 10, legend=:topleft)
scatter!(plt, df.nf, df.nx, label = "data")
vline!(plt, n_minima2, label = "minima")
display(plt)
```

```
Error: UndefVarError: plot not defined
```



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
VideoIO.get_duration("img/pendulo_70cm_1_reduzido.mov")
```

```
Error: Could not open img/pendulo_70cm_1_reduzido.mov. avformat_open_input 
error code -2
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
Error: UndefVarError: data2_scaled_x not defined
```



```julia
plot(data2_scaled_t, sol2(data2_scaled_t)[1,:], label = "ODE", ylims=(-1,1))
scatter!(data2_scaled_t, data2_scaled_x, label = "data")
```

```
Error: UndefVarError: data2_scaled_t not defined
```



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

```
Error: UndefVarError: data2_scaled_t not defined
```



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
 14.757103758523856
 14.975837242139237
 15.220528172168207
 15.435739323889688
 15.681990504266405
 15.899891324886354
 16.144987068343934
 16.367029004899734
 16.45
u: 81-element Vector{RecursiveArrayTools.ArrayPartition{Float64, Tuple{Vect
or{Float64}, Vector{Float64}}}}:
 ([0.0], [0.5235987755982988])
 ([-0.0009980900796482302], [0.523598702408922])
 ([-0.010978532676025766], [0.5235899199226164])
 ([-0.11068567653652728], [0.5226974863498236])
 ([-0.3813143284771497], [0.5127947624143488])
 ([-0.7977890197442175], [0.4745408968992312])
 ([-1.268356249332695], [0.38830121752424207])
 ([-1.7078585641373931], [0.22627879083954483])
 ([-1.8891348315194079], [-0.0020668325633487585])
 ([-1.6627067086680587], [-0.23711503637629103])
 ⋮
 ([0.49103571221118436], [-0.3359401762753514])
 ([1.2181504266325172], [-0.13835450159398452])
 ([1.1421234168083245], [0.17172686806385645])
 ([0.35132874328089825], [0.3409458558094231])
 ([-0.7548617910520811], [0.28745266963945754])
 ([-1.2735027218362773], [0.053843944407130785])
 ([-0.93261168688129], [-0.2363744318904869])
 ([-0.008989184610849575], [-0.34667806040764854])
 ([0.36875503600834453], [-0.33163121749061913])
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
Error: UndefVarError: data2_scaled_t not defined
```



```julia
θ₀, l, α = Optim.minimizer(res)
```

```
Error: UndefVarError: res not defined
```



```julia
π / θ₀
```

```
6.0
```



```julia
θ₀ - π / 5.6529
```

```
-0.032150070761939875
```



```julia
prob_rmk = remake(prob_pendulum_2nd, u0 = ArrayPartition([0.0], [θ₀]), p = [l, g, α])
```

```
ODEProblem with uType RecursiveArrayTools.ArrayPartition{Float64, Tuple{Vec
tor{Float64}, Vector{Float64}}} and tType Float64. In-place: true
timespan: (0.0, 16.45)
u0: ([0.0], [0.5235987755982988])
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

```
Error: UndefVarError: data2_scaled_t not defined
```


