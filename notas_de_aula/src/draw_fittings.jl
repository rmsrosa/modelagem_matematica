using Plots
gr()
theme(:ggplot2)

axes_color = :gray30

# Ajuste de reta a dois pontos
plot([(2, 1), (3, 4)], xlim=(-1,4), ylim=(-1,5),
    seriestype = :scatter, framestyle = :origin,
    xticks=-1:4, yticks=-1:5, markershape=:circle, markersize=6, 
    xaxis="x", yaxis = "y", label="dados", legend=:topleft,
    title="Dados da amostra e o modelo ajustado", 
    legendfont=8, titlefont=12, size=(660,440))
plot!([(-1,-8), (4,7)], color=:tomato, label="modelo y=3x-5")
plot!([(-1,0), (4,0)], color=axes_color, label=nothing)
display(plot!([(0,-1), (0,5)], color=axes_color, label=nothing))
savefig(joinpath("notas_de_aula", "img", "ajuste_reta_a_dois_pontos.png"))

# Ajustes de reta a um ponto
plot([(1, 2)], xlim=(-1,3), ylim=(-1,3),
    seriestype = :scatter, framestyle = :origin,
    xticks=-1:3, yticks=-1:3, markershape=:circle, markersize=6, 
    xaxis="x", yaxis = "y", label="dados", legend=:right,
    title="Dados da amostra e dois modelos ajustados",
    legendfont=8, titlefont=12, size=(660,440))
plot!([(-1,2), (3,2)], color=:tomato, label="modelo y=2 (m=0, b=2)")
plot!([(-1,-2), (3,6)], color=:seagreen, label="modelo y=2x (m=2, b=0)")
plot!([(-1,0), (3,4)], color=:sandybrown, label="modelo y=x+1 (m=1, b=1)")
plot!([(-1,0), (3,0)], color=axes_color, label=nothing)
display(plot!([(0,-1), (0,3)], color=axes_color, label=nothing))
savefig(joinpath("notas_de_aula", "img", "ajuste_reta_a_um_ponto.png"))

# Ajuste de reta a três ponto
plot([(1, 2), (2, 1), (3, 4)], xlim=(-1,4), ylim=(-1,5),
    seriestype = :scatter, framestyle = :origin,
    xticks=-1:4, yticks=-1:5, markershape=:circle, markersize=6, 
    xaxis="x", yaxis = "y", label="dados", legend=:topleft,
    title="Dados da amostra e o modelo ajustado", 
    legendfont=8, titlefont=12, size=(660,440))
plot!([(-1,-2/3), (4,13/3)], color=:tomato, label="modelo y=x+1/3")
plot!([(-1,0), (4,0)], color=axes_color, label=nothing)
display(plot!([(0,-1), (0,5)], color=axes_color, label=nothing))
savefig(joinpath("notas_de_aula", "img", "ajuste_reta_a_tres_pontos.png"))
