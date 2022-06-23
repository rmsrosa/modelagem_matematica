include("VideoTracking.jl")

using CSV
using DataFrames

filename = "../img/pendulo_40cm_reduzido.mov"
filename = "../img/pendulo_70cm_1_reduzido_curto.mp4"
filename = "../img/pendulo_70cm_1_reduzido.mov"
tracks = VideoTracking.find_tracks("$(@__DIR__())/$filename", lag = 10)

df = DataFrame(
    nf = collect(getfield(tracks[1], :nspan)),
    nx = getfield.(tracks[1].path, :x),
    ny = getfield.(tracks[1].path, :y)
)

# data_filename = "../data/pendulo_70cm_reduzido.csv"
# CSV.write(data_filename, df)

# df_back = CSV.read(data_filename, DataFrame)

@info df == df_back