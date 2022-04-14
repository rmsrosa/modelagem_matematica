
@def title = "Instalando e acessando o Julia"

# {{ get_title }}

* Nessa edição da disciplina, vamos usar a [linguagem de programação Julia](https://julialang.org).
* A [versão 1.6](https://julialang.org/blog/2021/03/julia-1.6-highlights/) foi recentemente lançada e está disponível para [download aqui](https://julialang.org/downloads/)


## Informações e guias

* [Wikipedia - Julia (programming language)](https://en.wikipedia.org/wiki/Julia_(programming_language))
* [Getting Started with Julia (QuantEcon)](https://julia.quantecon.org/getting_started_julia/index.html)
* [Julia Documentation](https://docs.julialang.org/en/v1/)
* [A via rápida para Julia 1.0](https://juliadocs.github.io/Julia-Cheat-Sheet/br/)
* [MATLAB–Python–Julia cheatsheet (QuantEcon)](https://cheatsheets.quantecon.org)
* [Noteworthy Differences from other Languages](https://docs.julialang.org/en/v1/manual/noteworthy-differences/)
* [Think Julia: How to Think Like a Computer Scientist](https://benlauwens.github.io/ThinkJulia.jl/latest/book.html)
* [Introducing Julia](https://en.wikibooks.org/wiki/Introducing_Julia)
* [A Deep Introduction to Julia for Data Science and Scientific Computing](http://ucidatascienceinitiative.github.io/IntroToJulia/)


## Julia

[Julia](https://en.wikipedia.org/wiki/Julia_(programming_language)) é uma linguagem de programação de uso geral, criada para ser fácil e rápida. Ela tem a abstração de linguagens de alto nível (como python e matlab) e a rapidez de linguagens de baixo nível (como c e fortran). Há um slogan que diz que "Julia parece python, tem um espírito de Lisp e roda como fortran" (ou, no original, "looks like Python, feels like Lisp, and runs like Fortran").

Julia foi desenvolvida por [Jeff Bezanson](https://www.wikidata.org/wiki/Q20630572), [Alan Edelman](https://en.wikipedia.org/wiki/Alan_Edelman), [Viral B. Shah](https://en.wikipedia.org/wiki/Viral_B._Shah) e [Stefan Karpinski](https://en.wikipedia.org/wiki/Stefan_Karpinski), no MIT. É uma linguagem relativamente nova, tendo sido iniciada em 2009, mas cuja primeira versão estável, 1.0, sendo lançada apenas em meados de 2018. Em 24 de março de 2021, [a versão 1.6](https://julialang.org/blog/2021/03/julia-1.6-highlights/) foi lançada.

Pelas propriedades mencionadas acima, Julia tem crescido de maneira vertiginosa. O seu ecosistema de pacotes ainda é relativamente pequeno, mas limpo e em pleno crescimento, contendo, em particular, tudo que precisaremos nesta matéria.


## Comunidades

Julia é uma linguagem recente e com uma comunidade bastante amigável, com um ótimo ambiente cooperativo.

Há várias plataformas onde se pode interagir com outras pessoas empolgadas com a linguagem e com os desenvolvedores centrais da linguagem e com alguns dos próprios criadores da linguagem, como Stefan Karpinski.

Pode-se aprender muitos nas seguintes plataformas:

- [Julia Discourse](https://discourse.julialang.org)
- [The Julia Language Slack](https://julialang.org/slack/)
- [Julia Zulip](https://julialang.zulipchat.com/register/)
- [Humans of Julia - Discord](https://discord.gg/C5h9D4j)
- [julia StackOverflow](https://stackoverflow.com/tags/julia)
- [Julia Language Twitter](https://twitter.com/JuliaLanguage)
- [JuliaCon - Conference videos](https://juliacon.org/)
- [Github/Julia](https://github.com/JuliaLang/julia/issues) - todo o código julia está disponível no  github


## Modos de utilização

Você pode programar em julia de diversas maneiras

* No [Julia REPL *(read-eval-print loop)*](https://docs.julialang.org/en/v1/stdlib/REPL/), que é um ambiente interativo de linha de comando.
* No [Jupyter (notebook ou lab)](https://jupyter.org), como nas notas utilizadas aqui.
* No [Pluto](https://github.com/fonsp/Pluto.jl), que é uma versão *reativa* do Jupyter, escrita especialmente para Julia.
* No [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb); veja [Julia on Colab](https://github.com/Dsantra92/Julia-on-Colab), que é uma espécie de Jupyter notebook rodando "na nuvem", em servidores do Google.
* No [Binder](https://mybinder.org), um ambiente na nuvem para rodar notebooks Jupyter.
* Em algum editor integrado a um ambiente de computação (tecnicamente um Ambiente de Desenvolvimento Integrado, ou *IDE - Integrated Development Environment*), como, por exemplo
  * [VSCode](https://code.visualstudio.com/), com a extensão *Julia Language Support (julialang.language-julia)*
  * [Juno](https://junolab.org), feito especialmente para o Julia, mas que recentemente tem recebido menos atenção, com a adoção maior do VSCode.

Eu, pessoalmente, uso o *REPL*, *Jupyter lab*, *Binder* e *VSCode*.

Vocês podem "baixar" os notebooks para os seus computadores e utilizar qualquer ferramenta local como as mencionadas acima.

Ou interagirem com os notebooks na nuvem. O acesso a cada caderno no binder pode ser feito diretamente clicando-se no ícone "launch binder" no topo de cada página.


## Modo interativo

Tanto no REPL, como nos ambientes tipo Jupyter, podemos executar instruções de maneira interativa.

E temos acesso a quatro ambientes:
* O de **comandos julia**, propriamente;
* Um para a **manutenção de pacotes**;
* Um para **ajuda**; e
* Um para acesso ao **shell**.

Vamos falar brevemente de cada um deles.


### Julia em modo interativo

O ambiente julia é o principal ao que temos acesso. No REPL, ele aparece de início como
```julia
(base) % julia
               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.7.1 (2021-12-22)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

julia> 
```

Observe as instruções para digitar `"?"` para ajuda e `"]?"` para ajuda com os pacotes. Ao entrar nesses ambiente, pode-se voltar ao ambiente julia digitando `<backspace>` ou `<delete>`, dependendo do seu sistema/computador.

Podemos usá-lo, por exemplo, como uma calculadora:
```julia
julia> sin(π/2)
1.0
```


### Julia no notebook

No notebook, acessamos o julia em uma célula de código:

```julia
sin(pi/2)
```

```
1.0
```




Em uma célula com várias expressões, apenas o resultado da última expressão é exibido ao final da célula (a menos que haja uma operação explícita de exibição de resultado, como `println`, `@show`, `@info`, etc..

```julia
var1 = 2.0
var2 = sin(π/4)
var3 = var1 * var2
```

```
1.414213562373095
```




Aviso, no entanto, que, ao longo do curso, utilizarei muito `nothing` para evitar a exibição do resulto do último comando executado em uma célula. E vou utilizar `@show` para exibir os resultados desejados. Por exemplo,

```julia
var1 = π/4
var2 = sin(π/4)
var3 = var1 * var2
@show var3
var4 = cos(var1)
var5 = var3^2 + var1^2*var4^2
@show var5
nothing
```

```
var3 = 0.5553603672697958
var5 = 0.6168502750680849
```




Vamos falar mais desse ambiente em seguida. No momento, vamos aos outros.


### Ajuda

Digitando `?`, obtemos o *prompt* `help?>` de ajuda. Para ajuda sobre o próprio modo `help?>` basta digitar `help` seguido de `<enter>` ou `<return>`:

```julia
help?> help
search: help schedule Channel hasfield @threadcall AbstractChannel

  Welcome to Julia 1.7.1. The full manual is available at

  https://docs.julialang.org

  as well as many great tutorials and learning resources:

  https://julialang.org/learning/

  For help on a specific function or macro, type ? followed by its name, e.g.
  ?cos, or ?@time, and press enter. Type ; to enter shell mode, ] to enter
  package mode.

```


### Ajuda sobre uma função

Podemos, nesse ambiente, pedir ajuda sobre qualquer função disponível no ambiente:

```julia
help?> sin
search: sin sinh sind sinc sinpi sincos sincosd sincospi asin using isinf asinh

  sin(x)

  Compute sine of x, where x is in radians.

  ────────────────────────────────────────────────────────────────────────────

  sin(A::AbstractMatrix)

  Compute the matrix sine of a square matrix A.

  If A is symmetric or Hermitian, its eigendecomposition (eigen) is used to
  compute the sine. Otherwise, the sine is determined by calling exp.

  Examples
  ≡≡≡≡≡≡≡≡≡≡

  julia> sin(fill(1.0, (2,2)))
  2×2 Matrix{Float64}:
   0.454649  0.454649
   0.454649  0.454649
```


### Ajuda no notebook

Da mesma forma, podemos digitar `?` seguido do nome de uma função

```julia
?@time
```

```
Error: syntax: invalid identifier name "?"
```




### Shell

Podemos acessar diretamente o ambiente *shell* digitando `;`. No REPL, por exemplo, podemos obter a lista de arquivos/diretórios no diretório atual digitando `;ls`. Ao digitarmos `;`, o *prompt* automaticamente muda para `shell>`:
```zsh
shell> ls
01.01-Aspectos_curso.ipynb
01.02-Instalando_acessando_Julia.ipynb
01.03-Primeiros_passos_Julia.ipynb
```



### Acessando o shell pelo notebook

O mesmo acontece a partir de uma célula de código do notebook

```julia
;ls
```

```
Error: UndefVarError: ls not defined
```




Também podemos ler o diretório com o comando julia `readdir()`.

```julia
readdir()
```

```
2-element Vector{String}:
 "0101-Aspectos_curso.md"
 "images"
```




## O ambiente de pacotes

Assim como no python e em várias outras linguagens, pacotes adicionais estão disponíveis com diversas ferramentas. Temos pacotes para álgebra linear, vários tipos de equações diferenciais, integração e diferenciação, otimização, redes neurais, gráficos, *benchmarking*, etc.

No ambiente de pacotes, podemos **adicionar** e **remover** pacotes, ver a **situação** do ambiente de projetos, i.e. quais e que versões de pacotes estão instalados, e **atualizar** o ambiente.

Assim como no python, é possível, e saudável, ter vários ambientes separados, para cada tipo de projeto. Por isso se chama [ambiente de projeto](https://pkgdocs.julialang.org/v1/environments/). Os pacotes do ambiente estão definidos em arquivos denominados `Project.toml`, mantidos nos diretórios de cada pacote.

Uma distinção:
* Ao entrarmos no REPL, o ambiente carregado será, em princípio, um ambiente global.
* Ao entrarmos no jupyter, o ambiente carregado será o descrito pelo arquivo `Project.toml`, caso o jupyter seja chamado de um diretório contendo tal arquivo, ou o ambiente global, caso contrário.


### O ambiente de pacotes da matéria

Este repositório das notas contém um ambiente de projeto com todos os pacotes necessários. Na verdade alguns pacotes serão incluídos ao longo do andamento da matéria.

Para visualizar os pacotes já instalados, basta digitarmos `]st`, onde `]` indica o acesso ao modo de gerenciamento de pacotes e `st` é o comando para verificar o status do ambiente.

```julia
]st
```

```
Error: syntax: unexpected "]"
```




### Ativando um ambiente de pacotes

Caso você acesse o REPL e queira utilizar o ambiente de projeto da matéria (ou algum outro), primeiro navegue (ou antes de chamar o REPL ou depois, usando `;cd <path/to/folder>`) até o diretório que contenha o arquivo `Project.toml`. Em seguida, ative o modo de gerenciamento de pacotes e execute o comando `pkg> activate .`.

Ou digite diretamente `pkg> activate <path/to/folder>` a partir de qualquer diretório.


### O IJulia

Um pacote importante para acessar o Julia a partir do Jupyter é o [IJulia](https://github.com/JuliaLang/IJulia.jl).

Ao instalar o IJulia pela primeira vez, um novo *kernel* do Julia no Jupyter deve ser criado antes de acessá-lo. Pode-se instalar o IJulia e o kernel com
```
pkg> activate .
pkg> add IJulia
pkg> build IJulia
```

O kernel apropriado pode ser escolhido no menu tipo "drop-down" no canto superior direito de cada notebook. Ou na janela de seleção de kernel no momento de criação de um novo notebook.


### *Instantiate* 

Caso você copie uma estrutura de arquivos de outro lugar e caso essa estrutura já possua um arquivo `Project.toml` com os pacotes necessários, isso não significa que os pacotes venham instalados automaticamente.

Caso eles não estejam instalados, eles vão aparecer com uma marcação especial, na lista de pacotes que aparece ao se executar `]st`.

Nesse caso, é preciso *instantiate* o projeto, para que os pacotes indicados sejam instalados, sem a necessidade de adicioná-los um por um. Isso é feito com o comando 
```julia
pkg> instantiate
```


### Usando os pacotes

Ao começarmos o Julia, seja no REPL, seja no jupyter, temos disponível uma ampla gama de funções do `Julia.Base` (veja em "Base" no menu à esquerda em [Julia Documentation](https://docs.julialang.org/en/v1/).

Mas, como dito acima, há uma série de outros pacotes com funcionalidades extras. Algumas na biblioteca padrão (veja em "Standard Library", no mesmo link acima). Estas, no entanto, não estão disponíveis de imediato. Mas também não precisão ser adicionas no projeto. Elas já estão instaladas. Só não estão disponíveis.

Para utilizar um pacote que esteja instalado mas que não esteja disponível de imediado, é preciso "importá-lo*, assim como é feito no python. No Julia, no entanto, há formas diferentes de se fazer isso. Pra começar, temos dois comandos: `import` e `using`. E há várias formas de utilizá-los.

Mas essa discussão não cabe aqui nesse primeiro momento. Para quem quiser saber mais, sugiro ler a página [Modules](https://docs.julialang.org/en/v1/manual/modules) (veja, ainda, a tabela, ainda válida, na versão anterior da documentação [Modules v.1.5](https://docs.julialang.org/en/v1.5/manual/modules/#Summary-of-module-usage)).

Na prática, usaremos `using`, para simplificar, como veremos na célula a seguir e nos próximos notebooks.


### Gerenciando os pacotes a partir do Pkg()

Também é possível gerenciar os pacotes através do pacote `Pkg`, diretamente do *prompt* do julia.

Para isso, é preciso disponibilizar o pacote via `import` ou `using`. No caso, podemos fazer

```julia
using Pkg
Pkg.status()
```

```
Status `~/Dropbox/Mac/Documents/git-repositories/modelagem_matematica
/Project.toml`
  [6e4b80f9] BenchmarkTools v1.3.1
  [336ed68f] CSV v0.10.4
  [13f3f980] CairoMakie v0.7.5
  [717857b8] DSP v0.7.5
  [a93c6f00] DataFrames v1.3.2
  [0c46a032] DifferentialEquations v7.1.0
  [31c24e10] Distributions v0.25.53
  [7a1cc6ca] FFTW v1.4.6
  [713c75ef] Franklin v0.10.72
  [e9467ef8] GLMakie v0.5.5
  [28b8d3ca] GR v0.64.2
  [7073ff75] IJulia v1.23.3
  [4381153b] ImageDraw v0.2.5
  [82e4d734] ImageIO v0.6.1
  [6218d12a] ImageMagick v1.2.2
  [916415d5] Images v0.25.2
  [0f8b85d8] JSON3 v1.9.4
  [b964fa9f] LaTeXStrings v1.3.0
  [98b081ad] Literate v2.13.1
  [2fda8390] LsqFit v0.12.1
  [ae8d54c2] Luxor v3.2.0
  [2bd173c7] NodeJS v1.3.0
  [429524aa] Optim v1.6.2
  [91a5bcdd] Plots v1.27.5
  [e6cf234a] RandomNumbers v1.5.3
  [bd7594eb] SampledSignals v2.1.3
  [2913bbd2] StatsBase v0.33.16
  [1986cc42] Unitful v1.11.0
  [a5a2160c] UnitfulBuckinghamPi v0.1.0
  [42071c24] UnitfulRecipes v1.5.3
  [d6d074c3] VideoIO v1.0.0
  [8149f6b0] WAV v1.2.0
  [44d3d7a6] Weave v0.10.10
```




### Versão do Julia

Para visualizar mais detalhes sobre a máquina e a versão do julia em uso, pode-se usar o comando `versioninfo()`

```julia
using InteractiveUtils
versioninfo()
```

```
Julia Version 1.7.2
Commit bf53498635 (2022-02-06 15:21 UTC)
Platform Info:
  OS: macOS (x86_64-apple-darwin19.5.0)
  CPU: Intel(R) Core(TM) m5-6Y54 CPU @ 1.10GHz
  WORD_SIZE: 64
  LIBM: libopenlibm
  LLVM: libLLVM-12.0.1 (ORCJIT, skylake)
```




## Utilizando o Julia

No próximo caderno, vamos investigar o uso da linguagem Julia propriamente.
