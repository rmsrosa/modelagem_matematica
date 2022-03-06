
@def title = "Quantidades, unidades e dimensões"

# {{ get_title }}

* Análise dimensional é uma técnica clássica usada em engenharia e física para a obtenção de leis aproximadas para algum problema/fenômeno.
* Essa análise se aplica, mais geralmente, a diversas áreas.
* Uma formalização da técnica dada pela análise dimensional é o Teorema de Buckinham-Pi.
* Nesse primeira parte sobre o assunto, vamos ver os conceitos de quantidade, unidade e dimensão.


## Objetivos da análise dimensional

* Reduzir o número e a complexidade de variáveis que afetam um determinado fenômeno.

* Fornecer uma intuição simples e objetiva da realidade, apesar de aproximada.

* Benefício extra: fazer uma primeira validação de um modelo checando-se a sua consistência dimensional.


## Quantidades, unidades e dimensões - versão informal

* Uma **quantidade** é uma propriedade de um objeto (e.g. material, sistema, bem, serviço, etc.) que possa ser quantificado com alguma medida. Por exemplo, a altura de uma pessoa;
* Essa *medida* de uma *quantidade* é expressa através de um **valor** (numérico) e uma **unidade de medida**. Por exemplo, um metro e oitenta de altura, denotado por $h = 1,80\,\texttt{m}$;
* Cada unidade, ou quantidade, possui uma **dimensão**, com dada dimensão podendo ter várias unidades. Por exemplo, comprimento, denotado por $L$, medido em unidades como metro $(\texttt{m})$, quilômetro $(\texttt{km})$, centímetro $(\texttt{cm})$, etc.
* Podemos somar ou subtrair quantidades com a mesma dimensão, mantendo a dimensão, mas não necessariamente a unidade. Por exemplo, $1\,\texttt{m} + 80\,\texttt{cm} = 1800\,\texttt{mm}$;
* Podemos multiplicar e dividir dimensões diferentes, gerando novas dimensões. Por exemplo, 
comprimento $L$ ao quadrado nos dá a dimensão $L^2$ de área; comprimento $L$ sobre tempo $T$ nos dá a dimensão $L/T$ de velocidade.
* Da mesma forma, podemos multiplicar e dividir unidades e quantidades de dimensões diferentes. Por exemplo, $\texttt{m}*\texttt{m} = \texttt{m}^2$ é uma unidade de área e $(36\,\texttt{km})/(30\,\texttt{min}) = 72\,\texttt{km}/\texttt{h} = 20\,\texttt{m}/\texttt{s}$ é uma quantidade medindo velocidade.
* Mais pra frente veremos uma, das muitas possíveis, versões formais abstratas desses conceitos.


## Exemplos

* Como mencionado acima, podemos consider a *altura* como sendo uma propriedade de uma pessoa, com a dimensão de comprimento, que pode ser medida em unidades de metros, centímetros, pés, polegas, etc., e com um valor numérico apropriado. Por exemplo, a minha altura é de $h = 1,80 \,\texttt{m}$, onde $\texttt{m}$ é o símbolo para metros. A notação para a dimensão de comprimento é $[h] = L$. Em outras unidades, posso escrever $h = 180 \,\texttt{cm}$ ou $h = 5\,\texttt{ft} \;11\,\texttt{in}$.

* A pressão atmosférica é a pressão que sentimos devida à atmosfera da Terra. Ao nível do mar, na média ao redor da Terra, ela é de aproximadamente 1 **atmosfera**, ou $1 \,\texttt{atm}$, onde $\texttt{atm}$ é, mais precisamente, a **atmosfera padrão**, que é definida como 
$$
\begin{align*}
1\,\texttt{atm} & = 101,325.0\,\texttt{Pa} = 1,013.25 \,\texttt{hPa} =  1,013.25 \,\texttt{mbar} \\
& = 760 \,\texttt{mm}\;\texttt{Hg} = 29.9212 \,\texttt{in}\;\texttt{Hg} = 14.696 \,\texttt{psi}.
\end{align*}
$$




## Conjuntos de dimensões

* Em geral, para cada problema em questão, podemos nos restringir a apenas um determinado conjunto de dimensões.

* Por exemplo, para problemas mecânicos, basta considerarmos **massa**, **comprimento** e **tempo**. 

* No caso de problemas termo-mecânicos, devemos adicionar a **temperatura**.

* Em finanças, consideramos uma **dimensão monetária**. 

* Em química, precisamos de uma dimensão para a **quantidade de uma substância**.

* Em outros problemas, uma dimensão para a **corrente elétrica**, para **luminosidade**, etc.


## Sistemas de unidades

* Junto com a determinação de um conjunto de dimensões para um determinado problema, podemos escolher um conjunto de unidades para representar quantidades em cada dimensão.

* Fixando as unidades, podemos abstrair os valores e facilitar os cálculos entre as quantidades.

* Uma determinada escolha de unidades é chamada de **sistema de unidades**.


### Sistema MKS

* Por exemplo, o sistema **MKS** considera metros, quilograma e segundos para as dimensões de comprimento, massa e tempo, como exibido na tabela a seguir. 

| Grandeza       | Unidades       | Nome       |  Dimensão |
|:---------------|:--------------:|:----------:|:---------:|
| comprimento    | $\texttt{m}$   |    metro   |    $L$    |
| massa          | $\texttt{kg}$  | quilograma |    $M$    |
| tempo          | $\texttt{s}$   |  segundos  |    $T$    |


### Agregando a temperatura

* Em problemas termo-mecânicos, precisamos incluir a temperatura, usualmente medida em Kelvin, nos levando ao sistema

| Grandeza       | Unidades       | Nome       |  Dimensão |
|----------------|:--------------:|:----------:|:---------:|
| comprimento    | $\texttt{m}$   |    metro   |    $L$    |
| massa          | $\texttt{kg}$  | quilograma |    $M$    |
| tempo          | $\texttt{s}$   |  segundos  |    $T$    |
| temperatura    | $\texttt{K}$   |   kelvin   | $\Theta$  |


### O sistema internacional de unidades

* Este sistema inclui ainda **corrente elétrica**, **unidade para a quantidade de substância**, e **intensidade luminosa**.


| Grandeza                 | Unidades       | Nome       |  Dimensão |
|--------------------------|:--------------:|:----------:|:---------:|
| comprimento              | $\texttt{m}$   |    metro   |    $L$    |
| massa                    | $\texttt{kg}$  | quilograma |    $M$    |
| tempo                    | $\texttt{s}$   |  segundos  |    $T$    |
| temperatura              | $\texttt{K}$   |   kelvin   | $\Theta$  |
| corrente elétrica        | $\texttt{A}$   |   ampére   |    $I$    |
| intensidade luminosa     | $\texttt{cd}$  |   candeia  |    $J$    |
| quantidade de substância | $\texttt{mol}$ |    mole    |    $N$    |


### Dimensões e unidades fundamentais e derivadas

* As dimensões e as unidades associadas às grandezas físicas são divididas em duas categorias: **fundamentais** (ou **de base**) e **derivadas**.

* No sistema **MKS**, por exemplo, as dimensões fundamentais são comprimento, massa e tempo. A partir delas, podemos obter volume, área, velocidade, aceleração e densidade, por exemplo, com dimensões, respectivamente, de $L^3$, $L^2$, $L/T$, $L/T^2$ e $M/L^3$.

* Mas essa classificação é arbitrária. Poderíamos considerar o volume como unidade fundamental, no lugar de comprimento, e obter o comprimento $L=\text{volume}^{1/3}$. Ou considerar ainda a densidade no lugar da massa e obter $M=\text{densidade}\times\text{volume}$.

* Associadas à escolha das dimensões fundamentais, temos as unidades fundamentais correspondentes, assim como as unidades derivadas.


### Exemplos de unidades derivadas

| Grandeza |  Unidades     | Dimensão | Nome |
|----------|:-------------:|:------:|-------|
| área       |  $\texttt{m}^2$  | $L^2$  | |
| volume     | $\texttt{m}^3$ | $L^3$ | |
| velocidade | $\texttt{m}\,/\,\texttt{s}$ = $\texttt{m}\,\texttt{s}^{-1}$ | $L T^{-1}$ | |
| aceleração | $m/s^2$ = $m \, s^{-2}$ | $L T^{-2}$| |
| força      | $N$ = $\dfrac{\texttt{kg}\,\texttt{m}}{\texttt{s}^2}$ = ${\texttt{kg} \, \texttt{m} \, \texttt{s}^{-2}}$ | $M L T^{-2}$ | Newton |
| trabalho / energia | $\texttt{J}$ = $\dfrac{\texttt{kg} \, \texttt{m}^2}{\texttt{s}^2}$ = ${\texttt{kg} \, \texttt{m}^2 \, \texttt{s}^{-2}}$ | $M L^2 T^{-2}$ | Joule |
| pressão | $\texttt{Pa}$ = $\dfrac{\texttt{kg}}{\texttt{m} \, \texttt{s}^2}$ = ${\texttt{kg} \, \texttt{m}^{-1} \, \texttt{s}^{-2}}$ | $M L^{-1} T^{-2}$ | Pascal |
| densidade (massa específica)      | $\dfrac{\texttt{kg}}{\texttt{m}^3}$ = $\texttt{kg} \, \texttt{m}^{-3}$ | $M L^{-3}$ | |
| difusividade (de massa e térmica) | $\dfrac{\texttt{m}^2}{\texttt{s}}$ = $\texttt{m}^2 \, \texttt{s}^{-1}$ | $M^2 T^{-1}$ | |

Observe que o **litro** é uma unidade de volume igual a um **decímetro cúbico**, i.e. $\texttt{l} = \texttt{dm}^3$. 

Para uma lista mais completa, veja [Lista de grandezas físicas](https://en.wikipedia.org/wiki/List_of_physical_quantities)


### Sistemas de mesma classe

* Um outro sistema semelhante ao MKS é o CGS, onde as unidades tomadas para as dimensões de comprimento, massa e tempo são **centímetro**, **grama** e **segundos**.

* Observe que eles representam as mesmas dimensões. Qualquer dimensão em um sistema é representável por uma dimensão (fundamental ou derivada, mas nesse caso sempre fundamental) no outro. Nesse casos, eles são ditos sistemas de mesma classe. 

* Sistemas da mesma classe são facilmente intercambiáveis. Podemos expressar qualquer quantidade possível em um ou em outro sistema. Por exemplo, como vimos acima, podemos representar uma distância de 2 metros como sendo de 200 centímetros. E uma densidade de $1000\,\texttt{kg}/\texttt{m}^3$ como sendo de $1.000.000\,\texttt{g}/100^3\texttt{cm}^3 = 1\,\texttt{g}/\texttt{cm}^3$. 


## Quantidades, unidades e dimensões - uma versão formal

* Uma **quantidade** é um conjunto de pares ordenados $(r, \texttt{u})$, onde $r\in \mathbb{R}$ é um **valor numérico** e $\texttt{u}$ é uma **unidade**, pertencente a um *conjunto de unidades* $\texttt{U}$.
* Em termos de notação, escrevemos $q=(r,\texttt{u})$ como $q = r\,\texttt{u}$.
* Uma hipótese fundamental é a de que existe uma *relação de equivalência* $\sim$ no conjunto $\texttt{U}$ das unidades, onde cada classe de equivalência é chamada de **dimensão**.
* Em termos de notação, escrevemos a *dimensão* de uma unidade $\texttt{u}$ por $[\texttt{u}]$.
* Essa relação de equivalência se estende, naturalmente, às quantidades: $r \,\texttt{u}\sim s \,\texttt{v} \Leftrightarrow \texttt{u}\sim \texttt{v}$. Dessa forma, a dimensão de uma quantidade $q$ é definida através da dimensão da sua unidade: $[q]=[\texttt{u}]$.
* Outra hipótese é a de que o conjunto de classes de equivalência possui uma operação de multiplicação com a qual é um grupo abeliano. O elemento neutro recebe uma terminologia especial, a de ser **adimensional**. 
* Nesse grupo formado pelo conjunto de classes de equivalência, também se assume que os inteiros agem "livremente" e "transitivamene" nele, ou seja, dados elementos $D_1$ e $D_2$ na classe, existe um único inteiro $n$ tal que $nD_1 = D_2$.
* Outra hipótese fundamental é a de que, em cada classe de equivalência, temos uma operação de adição sob a qual a classe de equivalência também forma um grupo abeliano.  
* Por fim, temos a hipótese de que quaisquer unidades $\texttt{u}$ e $\texttt{v}$ com a mesma dimensão estão relacionadas por uma transformação *afim*, ou seja, existem $a_0\in\mathbb{R}$ e $\lambda > 0$ tais que, para qualquer $r\in \mathbb{R}$, temos 
$$ r\,\texttt{u} = (a_0 + \lambda r) \,\texttt{v}.
$$
* Na maioria dos casos, no entanto, as unidades escolhidas na prátia possuem uma relação *linear*, i.e. com $a_0=0$.


### Propriedades

* Com as hipóteses acima, podemos comparar as magnitudes de quaisquer duas dimensões $q=r\,u$ e $p=s\,\texttt{v}$ com a mesma dimensão através da comparação de seu valores na mesma unidade, ou seja, comparando-se $a_0 + \lambda r$ com $s$, onde $a_0$ e $\lambda$ são dados pela relação $1 \,\texttt{u} = (a_0 + \lambda) \,\texttt{v}$.
* Das hipóteses de adição e de subtração, temos as propriedades $[q + p] = [q] + [p]$, para quantidades de mesma dimensão, e $[pq] = [p][q]$, para quantidades de dimensões diferentes.
* A adição se estende para quantidades de mesma dimensão: $r\,\texttt{u} + s\,\texttt{v} = (a_0 + \lambda r + s)\,\texttt{v}$. Naturalmente, a dimensão é preservada: $[r\,\texttt{u} + s\,\texttt{v}] = [\texttt{u}] = [\texttt{v}]$.
* As hipóteses do conjunto de unidades ser um grupo abeliano (em particular, qualquer dimensão $D$ possui inversa $D^{-1}$, com $D^0=1$ adimensional) e dos racionais agirem livremente nele (em particular, dados $D$ e $n$ existe o elemento $(1/n)D$ e é unico, de forma que podeos chamamá-lo de $D^{1/n}$.)
* Essa multiplicação se estende naturalmente a unidades e quantidades.
  * No caso de unidades, definimos $(\texttt{u},\texttt{v})\rightarrow \texttt{u}*\texttt{v}$, com $[\texttt{u}\texttt{v}] = [\texttt{u}][\texttt{v}]$, assim como a inversa multiplicativa $[\texttt{u}/\texttt{v}] = [\texttt{u}]/[\texttt{v}]$, sendo que $[\texttt{u}/\texttt{u}] = 1$, representando a adimensionalidade.
  * No caso de quantidades, temos $r\,\texttt{u} * s\,\texttt{v} = rs \,\texttt{u}\texttt{v}$ e $(r\,\texttt{u}) / (s\,\texttt{v}) = (r/s)\,\texttt{u}\texttt{v}$, quando $s\neq 0$.


### Funções transcendentais

* As funções trigonométricas, a função exponencial, o logaritmo e outras funções transcendentais não são estendidas diretamente a quantidades, unidades e dimensões.

* Elas podem ser definidas por geometria ou por séries de potências ou por outras maneiras não puramente algébricas e que não estão plenamente disponíveis no contexto dimensional.

* Elas só se aplicam a quantidades *adimensionais*.

* O logaritmo, no entanto, pode ser dado um certo sentido em geral, mas é preciso ter cuidado.


### Dimensões com estrutura de espaço vetorial e "um" logaritmo

* De maneira apropriada, podemos associar o grupo $\mathcal{D}$ de dimensões com um espaço vetorial sobre os racionais.

* Para diferenciar o conjunto de dimensões munido das operações de grupo, que denotamos por $\mathcal{D}$, do mesmo conjunto munido das operações vetoriais, vamos denotar este último por $\overline{\mathcal{D}}$.

* A cada $D$, vamos denotar por $\bar D$ essa dimensão vista como elemento de $\overline{\mathcal{D}}$. (Imagine "mergulhar" $x\in\mathbb{R}$ em $\bar x = (x,0)\in \mathbb{R}^2$, ou trasformar $s\in (0,\infty)$ em $\bar s = \log s \in \mathbb{R}$... 😉)

* Dados um racional $q$ e dimensões $\bar D$, $\bar D_1$ e $\bar D_2$ em $\overline{\mathcal{D}}$, definimos o produto escalar e a soma vetorial em $\mathcal{D}$ respectivamente por
$$ q \bar D = \overline{D^q}, \qquad \bar D_1 + \bar D_2 = \overline{D_1 D_2}.
$$

* Verifique, de fato, que isso faz de $\bar{D}$ um espaço vetorial sobre os racionais!

* E observe que, com essa representação, a transformação $D\mapsto \bar D$ tem a "cara" (propriedades algébricas) de um logaritmo.

* Por conta disso, podemos renomear essa transformação para $\operatorname{Log}$:
$$ q \operatorname{Log}(D) = \operatorname{Log}(D^q), \qquad \operatorname{Log}(D_1D_2) = \operatorname{Log}(D_1) + \operatorname{Log}(D_2).
$$

* Observe o meu cuidado em não escrever $\log$, mas $\operatorname{Log}$, para ressaltar que ele não é o mesmo operador que age concretamente nos reais (e nos complexos, quaternions, etc.)


### O espaço de dimensões do sistema MKS

* No sistema MKS, só consideramos as dimensões de comprimento, massa e tempo: $L$, $M$ e $T$.

* A partir delas, temos velocidade $L T^{-1}$, aceleração $L T^{-2}$, área $L^2$, volume $L^3$, densidade $ML^{-3}$, energia $ML^2T^{-2}$ e assim por diante.

* Claramente, isso tem uma aspecto de base, onde $L$, $M$ e $T$ geram todas as outras dimensões desse sistema.

* Essa associação fica mais clara quando usamos a representação logarítmica anterior, onde podemos escrever
$$ \begin{align*}
  \operatorname{Log}(L T^{-1}) & = \operatorname{Log}(L) - \operatorname{Log}(T), & \text{(velocidade)} \\
  \operatorname{Log}(L T^{-2}) & = \operatorname{Log}(L) - 2\operatorname{Log}(T), & \mathrm{(aceleração)} \\
  \operatorname{Log}(L^2) & = 2 \operatorname{Log}(L), & \mathrm{(área)} \\
  \operatorname{Log}(L^3) & = 3 \operatorname{Log}(L), & \mathrm{(volume)} \\
  \operatorname{Log}(ML^{-3}) & = \operatorname{Log}(M) - 3\operatorname{Log}(L), & \mathrm{ (densidade)} \\
  \operatorname{Log}(ML^{2}T^{-2}) & = \operatorname{Log}(M) - 2\operatorname{Log}(L) - 2\operatorname{T}, & \mathrm{(energia)} 
  \end{align*}
$$


### Logaritmos de quantidades e unidades

* A mesma ideia pode ser estendida a quantidades e unidades, afinal eles também tem essa estutura de grupo abeliano para a multiplicação.

* Podemos considerar $\operatorname{Log}(\texttt{u})$ de uma unidade $\texttt{u}$ e, associado a isso, $\operatorname{Log}(q)$ de uma quantidade.

* **Mas cuidado!:** 
  * A operação $\operatorname{Log}(\texttt{u}) + \operatorname{Log}(\texttt{v})$ deve ser vista meramente como uma representação da unidade $\texttt{u}\texttt{v}$, não como números reais sendo somados. Essa adição mora em um espaço vetorial abstrato.
  * Da mesma forma para quantidades, mas, mais ainda, nem pensar em fazer $\operatorname{Log}(2 \;\texttt{metros}) = \log(2) + \operatorname{Log}(\texttt{metros})$. Isso não tem o menor sentido. Não podemos "quebrar" a unidade $(2, \texttt{m})$ em dois objetos separados e operar em cada um deles, nem tampouco somar um número real $\log(2)$ com essa representação abstrata $\operatorname{Log}(\texttt{metros})$ da unidade metros.
  * E não confundir $\operatorname{Log}$ com $\log$!


## Quantidades e unidades como um subespaço afim unidimensional real

* O conjunto de unidades também pode ter uma representação mais concreta.

* Cada conjunto de equivalência de unidade pode ser visto como um subespaço afim unidimensional sobre os reais.

* Na maioria dos casos, simplesmente como um subespaço.

* Dadas duas unidades $\texttt{u}$ e $\texttt{v}$ na mesma classe, ou seja, de mesma dimensão, existem um $a_0\in \mathbb{R}$ e um fator $\lambda>0$ tais que, qualquer $r\in \mathbb{R}$, podemos sempre escrever $r\,\texttt{u}$ como $r\,\texttt{u} = (a_0 + \lambda r)\,\texttt{v}$, para algum $s\in \mathbb{R}$.

* É essencialmente como se cada unidade se comportasse como uma base para o subespaço.


## Referências

1. C. Dym, Principles of Mathematical Modeling, 2nd ed, Academic Press, 2004.

1. E. A. Bender, An Introduction to Mathematical Modeling, Dover, 1978.

1. G. Barenblatt, G. -- *Scaling*, Cambridge University Press, 2003.

1. Groesen, E. van, and Molenaar, J. -- *Continuum Modeling in the Physical Sciences*, SIAM, 2007. 

1. [T. Tao, A mathematical formalisation of dimensional analysis](https://terrytao.wordpress.com/2012/12/29/a-mathematical-formalisation-of-dimensional-analysis/).
