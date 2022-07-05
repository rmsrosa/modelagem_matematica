
@def title = "Ondas sonoras e elementos musicais"

# {{ get_title }}

```julia
using LinearAlgebra
using Plots
using WAV
using FFTW
using Random
```


```julia
include("scripts/AudioCaptionDisplay.jl")
using .AudioCaptionDisplay
```

```
Error: SystemError: opening file "/Users/rrosa/Documents/git_repositories/m
odelagem_matematica/src/jupyter/c11/scripts/AudioCaptionDisplay.jl": No suc
h file or directory
```




## Ondas sonoras e elementos musicais


### Tipos de ondas

* O som que ouvimos é resultado de ondas longitudinais do ar e que chegam até o nosso ouvido.

* Essas ondas são movimentos/vibrações coordenadas das moléculas do meio.

* Em sólidos e líquidos, as ondas podem ser tanto longitudinais como transversais, como vimos em ondas sísmicas, por exemplo. As ondas transversais dependem da rigidez do meio e, portanto, não ocorrem em gases.

* Ondas longitudinais, por sua vez, dependem da resistência do meio à compressão e podem se propagar em diversos meios.

* Vamos nos concentrar aqui em ondas longitudinais que se propagam no ar e geram o som que ouvimos, ou sejam, são ondas sonoras.


### Características de ondas sonoras

* Ondas sonoras podem ser caracterizadas pelas seguintes propriedades:
  1. **Direção de propagação**;
  1. **Velocidade de propagação**;
  1. **Frequência**, ou o seu recíproco multiplicativo, **comprimento de onda**;
  1. **Intensidade/Pressão/Amplitude**.
  1. **Forma**
* A velocidade é determinada pelo meio. Como estamos nos restringindo ao ar atmosférico em condições normais de temperatura e pressão, vamos considerar essa velocidade constante.
* E como não estamos interessados na propagação da onda em si, mas sim no seu efeito na audição, a direção de propagação também não é relevante.
* Vamos nos ater, então, às outras três características: **frequência**, **intensidade** e **forma**.


### Elementos musicais

* Os elementos musicais diretamente relacionados às características selecionadas acima são
  1. **Altura** *(pitch)*, determinada pela *frequência* da onda, que determina, no final das contas, as notas musicais.
  1. **Dinâmica**, que está relacionada à intensidade/amplitude da onda, ou ao que chamamos comumente de "volume".
  1. **Timbre**, que está relacionado com a forma da onda e caracteriza diferentes instrumentos musicais.
  
* Há diversos outros elementos musicais importantes em uma música mas que não vamos nos ater aqui: *tempo*, *duração* (de cada nota), *textura* (quantidade/complexidade de sons), *articulação* (suavidade ou não da combinação de notas)  


### Reproduzindo sons no Julia

* Vamos usar o pacote [dancasimiro/WAV.jl](https://github.com/dancasimiro/WAV.jl) para reproduzir sons digitais codificados na forma de uma vetor (ou matriz, de tiver mais canais)

* Os sons digitalizados, em forma de vetores ou arrays, podem ser reproduzidos pelo `WAV.jl` através das funções `wavplay`, `wavwrite`, ou da exibição do struct `WAVArray`. A vantagem do `WAVArray` no caderno Jupyter (ou no REPL) é que ele cria um elemento html de áudio, em que se pode reproduzir o som clicando-se no elemento, além de outras possibilidade de interação.

* Aqui, vamos usar uma modificação do `WAVArray`, denominada `CWAVArray`, que inclui um texto de "caption", para facilitar a indicação do áudio associado ao elemento html.

* Esse struct `CWAVArray` está no módulo `AudioCaptionDisplay` no arquivo local `src/AudioCaptionDisplay.jl`.

* Qualquer uma dessas formas inclui não só o vetor, ou matriz, com as intensidades, mas também uma número em ponto flutuante indicando a taxa de amostragem.

```julia
?wavplay
```

```
Error: syntax: invalid identifier name "?"
```




## Frequências e notas musicais

* Para a construção das notas, vamos considerar funções definidas em $\mathbb{R}$ (na verdade, para qualquer ponto flutuante...) que sejam periódicas de período 1.

* Assim, se $f=f(t)$ é uma função periódica de período $1$ e $\nu > 1$, então $f(\nu t)$ é uma função periódica de período $1/\nu$ e frequência $\nu$.

* As funções fundamentais para isso são as sinusoidais, $\cos(2\pi t)$ e $\sin(2\pi t)$, ou translações dela, onde a translação é a fase $\varphi$, e que podemos escrever de forma mais geral como
$$ \sin(\varphi + 2\pi t) \quad \text{ou} \quad \cos(\varphi + 2\pi t).
$$

* Abaixo, vamos considerar simplesmente $\sin(2\pi t)$.

* Podemos ter outras funções, com formas retangulares, triangulares, serra, etc.

* As notas são dadas pela frequência $\nu$, enquanto que a "cor" da nota (e.g. piano, violão, saxofone, etc.) é dada pela forma da onda.


### Resolução

* Como o ouvido humado pode sentir sons de até $20.000 \,\texttt{Hz}$, devemos usar uma discretização temporal suficientemente mais fina para uma boa "resolução" dessas frequências audíveis.

* Em digitalizações de áudio, é comum se utilizar a resolução de [$44.100\,\texttt{Hz}$](https://en.wikipedia.org/wiki/44,100_Hz).

* Isso é devido ao [Teorema de Nyquist–Shannon](https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem) e está ligado ao fenômeno de [*aliasing*](https://en.wikipedia.org/wiki/Aliasing).

* É necessária uma resolução maior do que o dobro da maior frequência a ser sampleada, caso contrário, a mesma série de dados pode representar ondas de diferentes frequências.

* Inicialmente, outras frequências de sampleamento foram sugeridas e utilizadas, em particular levando a disputas entre companhias como Sony e Philips, prevalecendo a escolha de $44.1\,\texttt{KHz}$, que tem sido mantida até hoje, em diversas mídias e formatos.

```julia
fs = 44100.0 # frequência de sampleamento 44.1 kHz
Tf = 1.0 # intervalo de tempo pro sampleamento
t = 0.0:inv(fs):Tf # malha temporal, com sampleamento de intervalo 1/fs segundos
nothing
```


```julia
ν = 20 # 20Hz
A = 1
g = A * sin.(2π * ν * t)
nothing
```


```julia
plot(t, g, xaxis = "tempo (segundos)", yaxis = "amplitude", label=nothing,
    title="Onda senoidal com frequência de $ν Hz", titlefont=10)
```

\fig{images/1103-Ondas_sonoras_elementos_musicais_6_1.png}


### Reproduzindo frequências baixas

* Apesar de conseguirmos ouvir frequências a partir de $20\,\texttt{Hz}$, não conseguimos, em geral, produzir sons com frequências tão baixas assim (mas há exceções).

* Em geral, produzimos sons a partir de $85\,\texttt{Hz}$, até uns $3\,\texttt{kHz}$.

* Mesmo equipamentos de som nem sempre conseguem produzir sons tão baixos.

* Vejamos na experiência abaixo (no computador que utilizo, identifico o som a partir de $20\,\texttt{Hz}$ no fone-de-ouvido, mas só a partir dos $80\,\texttt{Hz}$ na saída de som do computador).

```julia
for ν in 20:20:120
    g = sin.(2π * ν * t)
    display(CWAVArray(fs, g, "ν=$ν Hz:"))
end
```

```
Error: UndefVarError: CWAVArray not defined
```




### Reproduzindo frequências altas

* Da mesma forma, em geral, só conseguimos produzir som com as nossas cordas vocais até uns $3\,\texttt{kHz}$.

* E equipamentos de som também não conseguem produzir sons tão altos quanto $20.000\,\texttt{Hz}$.

* Vejamos a experiência abaixo (no meu laptop, identifico o som até uns $12.000\,\texttt{Hz}$).

```julia
for ν in 10000:1000:16000
    g = sin.(2π * ν * t)
    display(CWAVArray(fs, g, "ν=$ν Hz:"))
end
```

```
Error: UndefVarError: CWAVArray not defined
```




### As notas musicais

* As **notas musicais** são obtidas a partir de ondas com determinadas frequências.

* O nosso ouvido, de uma maneira ou de outra, sente certas combinações de notas de maneira mais agradável do que outras.

* A divisão dessas notas/frequências em cada música ou conjunto de músicas nos leva ao conceito de **escala musical**.

* Há várias escalas conhecidas, como as **diatônicas** (sete notas), **pentatônicas** (cinco notas) e a **cromática** (doze).

* Em certas escalas, podemos considerar diversos **modos**, que são conjuntos menores de notas da escala, definidos pela relação entre duas notas consecutivas.

* Por exemplo, os modos eólio, dórico, frígio, lídio, mixolidio, jônio e lócrio são modos diatônicos.

* As escalas maiores e menores são exemplos de escalas diatônicas nos modos eólio e jônio, respectivamente.

* As escalas pentatônicas também possuem modos menor e maior.

* Juntando as notas de todas as escalas diatônicas, obtemos um conjunto de doze notas, que formam a escala cromática.


### Oitavas

* As escalas se repetem em **oitavas**. Cada nota de uma oitava tem o dobro da frequência da mesma nota na oitava anterior.

* A partir das menores frequências que podemos ouvir, distinguir e produzir com a voz ou com instrumentos ($\sim 20,\texttt{Hz}$), as oitavas são denotadas numericamente, 0, 1, 2, ....

* A nota LÁ, por exemplo, é também denotada pela letra $A$, e assim temos o LÁ nessas diversas oitavas denotado por $A_0, A_1, A_2, \ldots$.

* Um piano padrão tem 55 teclas, cobrindo um pouco mais de sete oitavas (de $A_0$ a $C_8$).


### Afinação

* Não há nada de especial em uma determinada frequência por si só. É a composição dela com outras que faz sentido musical.

* Nesse aspecto, podemos partir de qualquer frequência para montar uma determinada escala e as suas oitavas.

* Por convenção, a nota $A_4$ tem a frequência de $440\,\texttt{Hz}$ (ou variações disso:  $432, 434, 436, \ldots, 446\,\texttt{Hz}$).


### Nota LÁ em diferentes oitavas

* Como dito acima, as escalas se repetem em oitavas, que são formadas a partir de potências de dois.

* Para uma determinada nota com frequência $\nu$, podemos considerar os seus múltiplos de potências de 2: $2\nu$, $4\nu$, $8\nu$ e assim por diante.

* Vejamos abaixo, a nota LÁ em diferentes oitavas, tanto separadamente como em conjunto.

```julia
ν₀ = 27.5 # A_0
f = zeros(length(t))
multiples = 3:5
nt = Int(floor(fs/ν₀/2^first(multiples))) + 1 # índice do período do primeiro múltiplo considerado
p = plot(title="Nota LÁ em diferentes oitavas", xlabel="tempo (ms)", titlefont=10)
for n in multiples
    ν = 2^n * ν₀
    g = sin.(2π * ν * t)
    f .+= g
    plot!(p, 1000 * t[1:nt],g[1:nt], label="A_$n (ν = $ν)")
    display(CWAVArray(fs, g, "A_$n (ν = $ν)"))
end
display(CWAVArray(fs, f, "combinação das frequências"))
plot!(p, 1000 * t[1:nt],f[1:nt], label="combinação", linestyle=:dash)
display(p)
```

```
Error: UndefVarError: CWAVArray not defined
```




### Semitons na escala temperada

* Há, na verdade, diversas maneiras de se definir as notas dentro de uma oitava (veja [Physics of Music: Just vs Equal Temperament](https://pages.mtu.edu/~suits/scales.html).

* A **escala temperada** é obtida por uma *razão uniforme* entre as frequências de notas (semitons, nesse caso) consecutivas.

* Mais precisamente, ao consideramos doze semitons em uma oitava (e.g. escala cromática ou a união das notas de todas as escalas diatônicas), então as frequências $\nu_i, \nu_{i+1}$ de dois semitons consecutivos é definida como sendo constante, $\nu_{i+1} = r\nu_i$.

* Se $\nu$ é a primeira nota, então $\nu_{12} = r^{11}\nu$ e o tom seguinte completa uma oitava, ou seja $r\nu_{12} = 2\nu$.

* Daí tiramos que $r^{12} = 2$, ou $r = 2^{1/12}$.


### Semitons na escala harmônica

* A **escala harmônica** aparece de forma mais natural, a partir dos harmônicos gerados por uma onda fundamental.

* Em matemática, a série harmônica é conhecida como sendo a série
$$ \sum_n \frac{1}{k^n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots.
$$

* Nesse sentido "1" é o "período fundamental".

* Mas em uma corda vibrante, o período fundamental é "2", ou seja, é duas vezes o comprimento da corda.

* Assim, os períodos gerados pela vibração de uma corda tensionada são os múltiplos $2, 2/2, 2/3, 2/4, 2/5, \ldots$, do comprimento da corda, $L$.

* Observe que as frequências são os recíprocos dos comprimentos de onda, $1/2L, 2/2L, 3/2L, 4/2L, 5/2L, \ldots$. 

* Se $\nu=1/2L$ é a frequência base, os seus harmônicos são $\nu, 2\nu, 3\nu, 4\nu, \ldots.$

* Os harmônicos irão produzir notas diferentes da fundamental, mas ainda assim "agradáveis", em geral.

```julia
oitava = 3 # A_3
ν_b = (oitava + 1) * 27.5
num_harm = 6
nt = Int(floor(fs/ν_b/2)) + 1
f = zeros(length(t))
harmonicos = fill(0.0, nt, num_harm + 1)
wav_arrays = []
for n in 0:num_harm
    ν = (n+1) * ν_b
    g = sin.(2π * ν * t)
    f .+= g
    harmonicos[:,n+1] .= g[1:nt]
    push!(wav_arrays, CWAVArray(fs, g, "Comprimento de onda: 2/$(n+1) (ν = $ν)"))
end
push!(wav_arrays, CWAVArray(fs, f, "combinação"))
p = plot(1000 * t[1:nt], harmonicos, layout=(num_harm+1,1), legend=nothing,
    title = hcat(["2/$n" for n in 1:num_harm+1]...), titlefont=8,
    xticks=nothing, yticks=nothing, axis=false, ylims=(-1.1,1.1), size=(300,400))
scatter!(p, 1000 * [t[j] for j in (1,nt), i in 1:num_harm+1], fill(0.0,2,num_harm+1), layout = (num_harm+1,1), marker=:square, markersize=2, color=3)
scatter!(p, 1000 * t[nt] .* hcat(inv.(1:num_harm+1)...), zeros(num_harm), layout=(num_harm+1,1), color=2)
display(p)
for wa in wav_arrays
    display(wa)
end
```

```
Error: UndefVarError: CWAVArray not defined
```




### Espectro e timbre

* Em uma nota "real", seja de violão, guitarra, baixo, contrabaixo, violino, piano, etc., esses harmônicos estão presentes, cada um com uma determinada amplitude.

* Essa combinação de amplitudes compõe o **espectro** da nota e caracteriza a **forma** da onda e o **timbre** do instrumento.

```julia
oitava = 3
ν_b = (oitava + 1) * 27.5
nt = Int(floor(fs/ν_b/2)) + 1
num_harm = 50
f̂ = rand(MersenneTwister(220), num_harm+1) .* inv.(1:num_harm+1)
f = sum([sin.(2π * ν * τ) for τ in t, ν in ν_b * (1:num_harm+1)] .* f̂', dims=2)

p_freq = scatter(ν_b * (1:num_harm+1), f̂, label="f̂", marker=:xcross,
    xaxis = "frequência (Hz)", yaxis = "Magnitude", title="Espectro", titlefont=10)
hline!(p_freq,[0], label=nothing, color=:lightgray)
scatter!(p_freq, ν_b * (1:num_harm+1), abs.(f̂), label="|f̂|")
display(p_freq)

p_forma_per = plot(1000 * t[1:nt], f[1:nt], label=nothing,
    xlabel="tempo (ms)", ylabel="amplitude", title="Forma em um período", titlefont=10)
display(p_forma_per)

WAVArray(fs, f)
```

```
WAV.WAVArray{Float64, 2}(44100.0, [0.0; 0.3891678144889097; … ; -0.38916781
448929844; -1.6390499232467122e-13;;], "")
```


\fig{images/1103-Ondas_sonoras_elementos_musicais_11_1.png}
\fig{images/1103-Ondas_sonoras_elementos_musicais_11_2.png}


### Envelope e dinâmica

* Em um instrumento real, além da combinação de harmônicos em uma nota, temos a sua **dinâmica**.

* Essa dinâmica se refere à variação de **volume**, que cresce rapidamente no início (o "ataque") e depois decai.

* Isso pode ser recriado digitalmente através de uma função **envelope**, positiva, que multiplica a onda.

```julia
dinamica = 12.2 * t .* (t .- 1).^4
fd = dinamica .* f

p_dim = plot(t, dinamica, xaxis="tempo (s)", yaxis="envelope",
        title="Dinâmica", titlefont=10, label=nothing)
display(p_dim)

p_forma = plot(t, fd, label=nothing,
    xlabel="tempo (s)", ylabel="amplitude", title="Forma", titlefont=10)
display(p_forma)
WAVArray(fs, fd)
```

```
WAV.WAVArray{Float64, 2}(44100.0, [0.0; 0.00010765117250936182; … ; -1.2552
56677058002e-18; -0.0;;], "")
```


\fig{images/1103-Ondas_sonoras_elementos_musicais_12_1.png}
\fig{images/1103-Ondas_sonoras_elementos_musicais_12_2.png}


### Notas reais

* Instrumentos reais, na verdade, são muito mais complexos.

* Abaixo, alguns exemplos

* Violão: [Roland SC-88 Nylon String Guitar C4](https://freewavesamples.com/roland-sc-88-nylon-string-guitar-c4)

* Banjo: [Yamaha MU90R Banjo Man C4](https://freewavesamples.com/yamaha-mu90r-banjo-man-c4)

* Sino em um sintetizador: [Korg DW-8000 Hollow Bell C4](https://freewavesamples.com/korg-dw-8000-hollow-bell-c4)

* Harpa: [Korg M3R Harp C3](https://freewavesamples.com/korg-m3r-harp-c3)

```julia
soundnames = (
    "Roland-SC-88-Nylon-String-Guitar-C4",
    "Korg-DW-8000-Hollow-Bell-C4",
    "Yamaha-MU90R-Banjo-Man-C4",
    "Korg-M3R-Harp-C3"
    )
for soundname in soundnames
    filepath = joinpath("data", "audio", soundname * ".wav")
    display(wavread(filepath) |> x -> CWAVArray(x[2], x[1], soundname))
end
```

```
Error: SystemError: opening file "data/audio/Roland-SC-88-Nylon-String-Guit
ar-C4.wav": No such file or directory
```




### Análise da onda de cada áudio

```julia
for soundname in soundnames
    filepath = joinpath("data", "audio", soundname * ".wav")
    fr, frs = wavread(filepath)
    Tf = (size(fr)[1]-1)/frs
    tempos = (0:size(fr)[1]-1)./frs # intervalo de tempo
    N = length(tempos) # N = fs + 1 se T == 1
    freqs = (0:div(N,2))/Tf # frequências
    Xr = rfft(fr[:,1]) # fft real do primeiro canal
    Z = [abs(Xr[1])/N; 2abs.(Xr[2:end])/N]
    ν₀ = 16.35 # C0
    nt = Int(floor(frs/ν₀/2)) + 1
    
    display(CWAVArray(frs, fr, soundname))

    display(plot(tempos, fr[:,1], xlabel="tempo (s)", ylabel="amplitude", label=nothing,
        title="Sinal do canal 1 ($soundname)", titlefont=10))
    display(plot(tempos, fr[:,2], xlabel="tempo (s)", ylabel="amplitude", label=nothing,
        title="Sinal do canal 2 ($soundname)", titlefont=10))
    display(plot(1000 * tempos[1:nt], fr[1:nt,1], xlabel="tempo (ms)", ylabel="amplitude",
        title="Sinal do canal 1 em um curto período", titlefont=10))
    display(plot(freqs, Z, xlabel="frequências (Hz)", ylabel="amplitude", label=nothing,
        title="Espectro de amplitude", titlefont=10))
end
```

```
Error: SystemError: opening file "data/audio/Roland-SC-88-Nylon-String-Guit
ar-C4.wav": No such file or directory
```




### Examinando o espectro das frequências iniciais

```julia
for (soundname, oitava) in zip(soundnames, (4,4,4,3))
    filepath = joinpath("data", "audio", soundname * ".wav")
    fr, frs = wavread(filepath)
    Tf = (size(fr)[1]-1)/frs
    tempos = (0:size(fr)[1]-1)./frs # intervalo de tempo
    N = length(tempos) # N = fs + 1 se T == 1
    freqs = (0:div(N,2))/Tf # frequências
    Xr = rfft(fr[:,1]) # fft real do primeiro canal
    Z = [abs(Xr[1])/N; 2abs.(Xr[2:end])/N] # amplitudes
    
    npre = 0
    npos = length(Z)
    en = 0.0
    fraction = 0.98
    threshold = fraction * sum(abs2,Z)
    while npos > npre + 1
        naux = npre + div(npos - npre, 2)
        enaux = en + sum(abs2, @view Z[npre+1:naux])
        if enaux > threshold
            npos = naux
        else
            npre = naux
            en = enaux
        end
    end
    
    ν₀ = 16.35 # C0
    ν_b = ν₀ * 2^oitava
    plot(freqs[1:npos], Z[1:npos], xlims=(freqs[1], freqs[npos]), label="Espectro de amplitude", xlabel="frequência (Hz)",
        ylabel="amplitude", title="$(soundname)\nEspectro de amplitude e harmônicos - frequências com $(100*fraction) % de energia", titlefont=9)
    scatter!(ν₀ * 2 .^(0:7), zeros(8), label="Nota DÓ em diferentes oitavas")
    display(scatter!(ν_b * (1:10), maximum(Z)/20 * ones(10), alpha=0.5, label="Harmônicos da nota DÓ"))
end
```

```
Error: SystemError: opening file "data/audio/Roland-SC-88-Nylon-String-Guit
ar-C4.wav": No such file or directory
```




## Referências

1. [The Physics of Sound](https://homepages.wmich.edu/~hillenbr/206/ac.pdf).

1. [Physics of Music](https://pages.mtu.edu/~suits/Physicsofmusic.html)

1. [Understanding Music Theory](https://www.earmaster.com/music-theory-online/course-introduction.html)

1. [Free Wave Samples](https://freewavesamples.com)
