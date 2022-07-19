
@def title = "Séries de Fourier e compressão de audio"

# {{ get_title }}

```julia
using LinearAlgebra
using Plots
using WAV
using FFTW
```


```julia
filepath = "../../../_assets/attachments/data/audio/piano-phrase.wav"
fr, frs = wavread(filepath)
tempos = (0:size(fr)[1]-1)./frs
```

```
0.0f0:2.2675737f-5:3.8457823f0
```



```julia
WAVArray(frs, fr, "Frase de piano")
```

```
WAV.WAVArray{Float64, 2}(44100.0f0, [-0.004272591326639607; -0.004272591326
639607; … ; -0.0037537766655476546; -0.0038453321939756462;;], "Frase de pi
ano")
```



```julia
display(plot(tempos, fr[:,1], xlabel="tempo (s)", ylabel="amplitude", label=nothing,
    title="Sinal sonoro", titlefont=10))
```

\fig{images/1104-Compressao_audio_4_1.png}

```julia
println("Duração: $(length(fr)/frs) s")
```

```
Duração: 3.845805 s
```



```julia
frame_duration = 100 # ms - padrão mp3 é de 26 ms
frame_length = Int(div(frame_duration * frs, 1000))
fr_frame = fr[1:frame_length, 1]
```

```
4410-element Vector{Float64}:
 -0.004272591326639607
 -0.004272591326639607
 -0.004272591326639607
 -0.004394665364543596
 -0.004150517288735618
 -0.003906369212927641
 -0.004150517288735618
 -0.0045167394024475845
 -0.004394665364543596
 -0.004272591326639607
  ⋮
  0.2216864528336436
  0.20789208655049288
  0.17896053956724753
  0.1497848445081942
  0.13623462630085148
  0.14087343974120303
  0.15601062044129765
  0.17371135593737602
  0.19104586931974243
```



```julia
WAVArray(frs, fr_frame, "Frase de piano (primeiros $(frame_duration)ms)")
```

```
WAV.WAVArray{Float64, 1}(44100.0f0, [-0.004272591326639607, -0.004272591326
639607, -0.004272591326639607, -0.004394665364543596, -0.004150517288735618
, -0.003906369212927641, -0.004150517288735618, -0.0045167394024475845, -0.
004394665364543596, -0.004272591326639607  …  0.21472823267311625, 0.221686
4528336436, 0.20789208655049288, 0.17896053956724753, 0.1497848445081942, 0
.13623462630085148, 0.14087343974120303, 0.15601062044129765, 0.17371135593
737602, 0.19104586931974243], "Frase de piano (primeiros 100ms)")
```



```julia
tempos_frame = (0:length(fr_frame)-1) / frs
freqs_frame = (0:div(frame_length, 2)) / frs # frequências
fr_frame_hat = rfft(fr_frame)
Z_frame = [
    abs(fr_frame_hat[1]) / frame_length; 
    2abs.(fr_frame_hat[2:end]) / frame_length
]

display(WAVArray(frs, fr_frame, "Parte da frase de piano"))

display(plot(tempos_frame, fr_frame, xlabel="tempo (s)", ylabel="amplitude", label=nothing,
    title="Sinal do canal 1", titlefont=10))
display(plot(freqs_frame, Z_frame, xlabel="frequências (Hz)", ylabel="amplitude", label=nothing,
    title="Espectro de amplitude", titlefont=10))
```

```
WAV.WAVArray{Float64, 1}(44100.0f0, [-0.004272591326639607, -0.004272591326
639607, -0.004272591326639607, -0.004394665364543596, -0.004150517288735618
, -0.003906369212927641, -0.004150517288735618, -0.0045167394024475845, -0.
004394665364543596, -0.004272591326639607  …  0.21472823267311625, 0.221686
4528336436, 0.20789208655049288, 0.17896053956724753, 0.1497848445081942, 0
.13623462630085148, 0.14087343974120303, 0.15601062044129765, 0.17371135593
737602, 0.19104586931974243], "Parte da frase de piano")
```


\fig{images/1104-Compressao_audio_8_1.png}
\fig{images/1104-Compressao_audio_8_2.png}

```julia
fr_frame_hat
```

```
2206-element Vector{ComplexF64}:
  -11.404889065218056 + 0.0im
    4.401345761508306 + 0.08595490000528298im
   3.4082877653630614 + 0.08196426411445865im
    6.356587472128002 - 0.18964797651701643im
    4.869113461640563 - 3.5923118212833742im
    8.323783990508698 + 3.2490025667385174im
   3.8612916512226567 + 0.8364064885072844im
   7.5179312978981425 - 2.3330276269850465im
    8.227964101740415 + 4.175612138713387im
    8.424895602709034 + 4.742851933641199im
                      ⋮
 -0.09795696005902577 - 0.0027981825930214477im
 -0.09975011408390433 + 0.003312592743423881im
 -0.09948480393847481 - 0.0011974075667288142im
 -0.10341372301687057 - 0.0004984029279813118im
 -0.09738611974973593 + 0.0048997456655905935im
 -0.10414685693085268 - 0.0002215345564245963im
 -0.09299656851336868 - 0.0017714270969930584im
 -0.10644238614362234 + 0.005858871159521911im
 -0.10205389568773549 + 0.0im
```



```julia
Z_frame
```

```
2206-element Vector{Float64}:
 0.0025861426451741624
 0.00199645578143504
 0.0015461556382688974
 0.0028840888455569837
 0.002744156570342591
 0.004052336221113851
 0.0017917648796805968
 0.0035698930264991334
 0.004184521541841969
 0.004384657578361314
 ⋮
 4.4443046509158166e-5
 4.5263085137162955e-5
 4.512109284680357e-5
 4.690019230727104e-5
 4.422190532236617e-5
 4.723224151822258e-5
 4.218296522720364e-5
 4.834626217683909e-5
 4.628294589012947e-5
```



```julia
[eachindex(Z_frame) Z_frame]
```

```
2206×2 Matrix{Float64}:
    1.0  0.00258614
    2.0  0.00199646
    3.0  0.00154616
    4.0  0.00288409
    5.0  0.00274416
    6.0  0.00405234
    7.0  0.00179176
    8.0  0.00356989
    9.0  0.00418452
   10.0  0.00438466
    ⋮    
 2198.0  4.4443e-5
 2199.0  4.52631e-5
 2200.0  4.51211e-5
 2201.0  4.69002e-5
 2202.0  4.42219e-5
 2203.0  4.72322e-5
 2204.0  4.2183e-5
 2205.0  4.83463e-5
 2206.0  4.62829e-5
```



```julia
Z_frame_top = sortslices([eachindex(Z_frame) Z_frame], dims = 1, by = x -> x[2], rev = true)
```

```
2206×2 Matrix{Float64}:
   84.0  0.0599791
   83.0  0.0526109
  201.0  0.0472486
  117.0  0.0403817
  200.0  0.0388048
   34.0  0.0346802
  252.0  0.0297227
  118.0  0.0286083
   28.0  0.0285721
   85.0  0.0281542
    ⋮    
  835.0  1.38591e-5
 1018.0  1.30356e-5
  998.0  1.25695e-5
 1105.0  1.25672e-5
 1000.0  8.86168e-6
 1110.0  7.37743e-6
  975.0  6.53743e-6
  979.0  5.19717e-6
  896.0  4.84732e-6
```



```julia
scatter(Z_frame_top[:,2])
```

\fig{images/1104-Compressao_audio_13_1.png}

```julia
length_top = 10
Z_top_inds = Int.(Z_frame_top[1:length_top, 1])
```

```
10-element Vector{Int64}:
  84
  83
 201
 117
 200
  34
 252
 118
  28
  85
```



```julia
# need to specify length of inverse real transform since the rfft is [d/2] long
# and the inverse could be 2[d/2] or 2[d/2] + 1, depending on whether the original
# vector has even or odd length
irfft(rfft(fr_frame), frame_length) ≈ fr_frame
```

```
true
```



```julia
irfft(fr_frame_hat, frame_length)
```

```
4410-element Vector{Float64}:
 -0.00427259132663957
 -0.004272591326639584
 -0.004272591326639647
 -0.004394665364543561
 -0.0041505172887356554
 -0.00390636921292764
 -0.004150517288735565
 -0.0045167394024476434
 -0.004394665364543606
 -0.004272591326639615
  ⋮
  0.22168645283364358
  0.2078920865504928
  0.1789605395672476
  0.14978484450819404
  0.13623462630085148
  0.14087343974120303
  0.1560106204412977
  0.17371135593737597
  0.1910458693197424
```



```julia
fr_frame_hat_top = zero(fr_frame_hat)
```

```
2206-element Vector{ComplexF64}:
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
     ⋮
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
 0.0 + 0.0im
```



```julia
fr_frame_hat_top[Z_top_inds] .= fr_frame_hat[Z_top_inds]
```

```
10-element view(::Vector{ComplexF64}, [84, 83, 201, 117, 200, 34, 252, 118,
 28, 85]) with eltype ComplexF64:
  -33.7650251711755 + 127.8710499762217im
 108.41005282342019 + 41.290164676220094im
 47.289120719299596 - 92.83249405927802im
  87.41383980697884 - 16.948297321524063im
 -77.03232742431845 - 37.246795014039236im
  38.90968266012985 + 65.83057114989343im
  63.96465597470014 - 14.276368846574574im
   10.3165556316061 + 62.23208374945314im
  61.86100665910691 - 11.933514499402161im
 -61.50572488024286 - 8.42433607287688im
```



```julia
fr_frame_top = irfft(fr_frame_hat_top, frame_length)
```

```
4410-element Vector{Float64}:
  0.11150196680249652
  0.11516766061405592
  0.11368059086290214
  0.10637386031287596
  0.09315763965670329
  0.07450428034735375
  0.05137454324737221
  0.02509723558159485
 -0.0027807386079490206
 -0.03065452950203258
  ⋮
  0.09465256693964458
  0.08038808658361979
  0.07101057618668619
  0.06709023634234279
  0.06848536640942049
  0.07438762259453545
  0.08343888439499116
  0.09390397105741916
  0.10387772808735343
```



```julia
freqs_frame = (0:div(frame_length, 2)) / frs # frequências
fr_frame_top_hat = rfft(fr_frame)
Z_frame_top_back = [
    abs(fr_frame_top_hat[1]) / frame_length; 
    2abs.(fr_frame_top_hat[2:end]) / frame_length
]

display(WAVArray(frs, fr_frame_top, "Parte da frase de piano comprimida"))

display(plot(tempos_frame, fr_frame_top, xlabel="tempo (s)", ylabel="amplitude", label=nothing,
    title="Sinal do canal 1", titlefont=10))
display(plot(freqs_frame, Z_frame_top_back, xlabel="frequências (Hz)", ylabel="amplitude", label=nothing,
    title="Espectro de amplitude", titlefont=10))
```

```
WAV.WAVArray{Float64, 1}(44100.0f0, [0.11150196680249652, 0.115167660614055
92, 0.11368059086290214, 0.10637386031287596, 0.09315763965670329, 0.074504
28034735375, 0.05137454324737221, 0.02509723558159485, -0.00278073860794902
06, -0.03065452950203258  …  0.11255622795344103, 0.09465256693964458, 0.08
038808658361979, 0.07101057618668619, 0.06709023634234279, 0.06848536640942
049, 0.07438762259453545, 0.08343888439499116, 0.09390397105741916, 0.10387
772808735343], "Parte da frase de piano comprimida")
```


\fig{images/1104-Compressao_audio_20_1.png}
\fig{images/1104-Compressao_audio_20_2.png}

```julia
display(WAVArray(frs, fr_frame, "Parte da frase de piano"))

display(plot(tempos_frame, fr_frame, xlabel="tempo (s)", ylabel="amplitude", label=nothing,
    title="Sinal do canal 1", titlefont=10))
display(plot(freqs_frame, Z_frame, xlabel="frequências (Hz)", ylabel="amplitude", label=nothing,
    title="Espectro de amplitude", titlefont=10))
```

```
WAV.WAVArray{Float64, 1}(44100.0f0, [-0.004272591326639607, -0.004272591326
639607, -0.004272591326639607, -0.004394665364543596, -0.004150517288735618
, -0.003906369212927641, -0.004150517288735618, -0.0045167394024475845, -0.
004394665364543596, -0.004272591326639607  …  0.21472823267311625, 0.221686
4528336436, 0.20789208655049288, 0.17896053956724753, 0.1497848445081942, 0
.13623462630085148, 0.14087343974120303, 0.15601062044129765, 0.17371135593
737602, 0.19104586931974243], "Parte da frase de piano")
```


\fig{images/1104-Compressao_audio_21_1.png}
\fig{images/1104-Compressao_audio_21_2.png}

```julia
function compress_frame(fr_frame, frs, length_top = 50)
    frame_length = length(fr_frame)
    # tempos_frame = ( 0 : frame_length - 1 ) / frs
    freqs_frame = (0 : div(frame_length, 2)) / frs # frequências
    fr_frame_hat = rfft(fr_frame)
    Z_frame = [
        abs(fr_frame_hat[1]) / frame_length; 
        2abs.(fr_frame_hat[2:end]) / frame_length
    ]
    Z_frame_top = sortslices([eachindex(Z_frame) Z_frame], dims = 1, by = x -> x[2], rev = true)
    Z_top_inds = Int.(Z_frame_top[1:length_top, 1])
    fr_frame_hat_top = zero(fr_frame_hat)
    fr_frame_hat_top[Z_top_inds] .= fr_frame_hat[Z_top_inds]
    return (
        inds = Z_top_inds,
        freqs = fr_frame_hat[Z_top_inds],
    )
end

function uncompress_frame(inds, freqs, frame_length)
    fr_frame_hat_top = zeros(ComplexF64, div(frame_length, 2) + 1)
    fr_frame_hat_top[inds] .= freqs
    fr_frame_back = irfft(fr_frame_hat_top, frame_length)
    return fr_frame_back
end
```

```
uncompress_frame (generic function with 1 method)
```



```julia
comp = compress_frame(fr_frame, frs)
```

```
(inds = [84, 83, 201, 117, 200, 34, 252, 118, 28, 85  …  250, 149, 38, 184,
 52, 12, 87, 80, 13, 199], freqs = ComplexF64[-33.7650251711755 + 127.87104
99762217im, 108.41005282342019 + 41.290164676220094im, 47.289120719299596 -
 92.83249405927802im, 87.41383980697884 - 16.948297321524063im, -77.0323274
2431845 - 37.246795014039236im, 38.90968266012985 + 65.83057114989343im, 63
.96465597470014 - 14.276368846574574im, 10.3165556316061 + 62.2320837494531
4im, 61.86100665910691 - 11.933514499402161im, -61.50572488024286 - 8.42433
607287688im  …  -1.5763830555113825 - 26.78384302022884im, 25.9035319678887
46 - 5.098261475424842im, -13.390624767147212 - 21.70999974515257im, 17.801
332197848172 + 18.00447646320448im, -14.644280862638023 - 20.64103380445097
7im, -7.686096144051215 + 22.207414433972165im, -22.74665240232254 - 4.2549
79491656448im, 8.768875950052678 - 19.891876336588567im, 7.732962888637599 
- 19.993290844392874im, -8.32520479424382 + 19.273903426153318im])
```



```julia
fr_frame_bak = uncompress_frame(comp.inds, comp.freqs, frame_length)
```

```
4410-element Vector{Float64}:
  0.12204643788761159
  0.11851994936975584
  0.11077768425394953
  0.09853635305203902
  0.08198994752532585
  0.061800262610382094
  0.039030251100656194
  0.015029397447569462
 -0.008713844757604408
 -0.030733682579983965
  ⋮
  0.11803899901224801
  0.1132353841973656
  0.10990532262619378
  0.10862157921677112
  0.10949925216054505
  0.1121862270524816
  0.1159167139641682
  0.11961978742660018
  0.12206801454800163
```



```julia
display(WAVArray(frs, fr_frame_bak, "compressed audio"))
```

```
WAV.WAVArray{Float64, 1}(44100.0f0, [0.12204643788761159, 0.118519949369755
84, 0.11077768425394953, 0.09853635305203902, 0.08198994752532585, 0.061800
262610382094, 0.039030251100656194, 0.015029397447569462, -0.00871384475760
4408, -0.030733682579983965  …  0.12335843470416524, 0.11803899901224801, 0
.1132353841973656, 0.10990532262619378, 0.10862157921677112, 0.109499252160
54505, 0.1121862270524816, 0.1159167139641682, 0.11961978742660018, 0.12206
801454800163], "compressed audio")
```



```julia
frame_duration = 26 # ms - padrão mp3 é de 26 ms
frame_length = Int(div(frame_duration * frs, 1000))
```

```
1146
```



```julia
uncomp = Array{Float64, 2}(undef, div(length(fr), frame_length) * frame_length, 1)
for n in 1:div(length(fr), frame_length)
    nstart = ( n - 1 ) * frame_length + 1
    nend = n * frame_length
    lfr_frame = fr[nstart:nend, 1]
    comp_frame = compress_frame(lfr_frame, frs, 50)
    uncomp_frame = uncompress_frame(comp_frame.inds, comp_frame.freqs, length(lfr_frame))
    uncomp[nstart:nend, 1] .= uncomp_frame
end
```


```julia
display(WAVArray(frs, uncomp, "compressed audio"))
```

```
WAV.WAVArray{Float64, 2}(44100.0f0, [-0.0007923241279948214; -0.00153024020
11201565; … ; -0.005413102257079467; -0.006042595345009632;;], "compressed 
audio")
```



```julia
display(WAVArray(frs, fr, "Frase de piano"))
```

```
WAV.WAVArray{Float64, 2}(44100.0f0, [-0.004272591326639607; -0.004272591326
639607; … ; -0.0037537766655476546; -0.0038453321939756462;;], "Frase de pi
ano")
```




## Referências

1. [Rassol Raissi, The theory behind MP3, dez/2002](http://www.mp3-tech.org/programmer/docs/mp3_theory.pdf)

1. [A. Carlacci, Ogg Vorbis and MP3 Audio Stream charecterization](https://webdocs.cs.ualberta.ca/~c603/latex/LaTeX_docs/article2/oggVorbis.pdf)
