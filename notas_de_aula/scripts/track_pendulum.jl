include("ImageTracking.jl")

using CSV
using DataFrames


filename = "../img/pendulo_40cm_reduzido.mov"
filename = "../img/pendulo_70cm_1_reduzido_curto.mp4"
filename = "../img/pendulo_70cm_1_reduzido.mov"
tracks = ImageTracking.find_tracks(filename)

df = DataFrame(
    nf = collect(getfield(tracks[1], :nspan)),
    nx = getfield.(tracks[1].path, :x),
    ny = getfield.(tracks[1].path, :y)
)

data_filename = "../data/pendulo_70cm_reduzido.csv"
CSV.write(data_filename, df)

df_back = CSV.read(data_filename, DataFrame)

@info df == df_back