
@def title = "Análise dimensional e o Teorema de Buckingham-Pi"

# {{ get_title }}

* Análise dimensional

* Formalização via Teorema de Buckinham-Pi.


## Princípio da homogeneidade dimensional

* Temos um princípio físico fundamental para a análise dimensional, que geralmente é enunciado por: "*Não podemos somar maças e laranjas*" ("We can't add apples and oranges"), mas que pode ser mais formalmente expresso como

> **Se uma equação expressa verdadeiramente uma relação adequada entre variáveis em um processo físico, ela será dimensionalmente homogênea; isto é, todos os seus termos aditivos terão a mesma dimensão.**


### Exemplo do princípio de homogeneidade dimensional

* Por exemplo, no problema clássico de um corpo em queda livre ideal, temos a seguinte relação entre a *altura* $h$ do objeto no instante $t$, a sua *altura inicial* $h_0$, a sua *velocidade inicial* $v_0$ e a aceleração da gravidade $g$:
$$ h = h_0 + v_0 t + \frac{g}{2}t^2.
$$
Observe que
$$ [h] = [h_0] = L, \quad [v_0] = L T^{-1}, \quad [t] = T, \quad [g] = LT^{-2}
$$
de forma que
$$ [h] = [h_0] = L, \quad [v_0 t] = [v_0][t] = L T^{-1} T = L, \quad \left[\frac{g}{2}t^2\right] = [g][t]^2 = LT^{-2}T^2 = L,
$$
ou seja, todos os termos aditivos tem a mesma dimensão $L$ de comprimento.


### Outra visão desse exemplo

* Também podemos olhar para a equação diferencial que segue da segunda lei de Newton:
$$ m\dfrac{d^2 h}{d^2 t} = -mg,
$$
onde $m$ é a massa do objeto.

* Nesse caso
$$ \left[m\dfrac{d^2 h}{d^2 t}\right] = M L T^{-2}, \qquad [-mg] = [m][g] = M L T^{-2}
$$
ou seja, todo os dois termos aditivos têm dimensão $MLT^{-2}$.

* Observe que da segunda lei de Newton podemos deduzir que, independente da força exercida em um sistema mecânico, ela tem exatamente a unidade de $MLT^{-2}$.


### Dimensão em derivadas

* Aproveitamos o exemplo acima para ilustrar que o processo de derivada acarreta em incluir uma potência no denominador, relativa à dimensão da quantidade em relação à qual se está derivando.

* Mais precisamente, se temos duas quantidades variáveis $x$ e $y$ e queremos olhar para a dimensão da taxa de variação de $y$ em relação a $x$, então
$$ \left[\dfrac{dy}{dx}\right] = \left[\lim_{\Delta x\rightarrow 0}\dfrac{\Delta y}{\Delta x}\right] = \left[\frac{d y}{d x}\right] = \dfrac{[d y]}{[d x]} = \frac{[y]}{[x]}.
$$

* No caso da segunda derivada,
$$ \left[\dfrac{d^2y}{dx^2}\right] \left[\dfrac{d}{dx}\dfrac{dy}{dx}\right]= \frac{\left[\dfrac{dy}{dx}\right]}{[dx]} = \dfrac{\dfrac{[y]}{[x]}}{[x]} = \frac{[y]}{[x]^2}.
$$

* E assim por diante.


### Lei da gravitação universal

* A força gravitacional entre dois corpos pontuais de massa $m_1$ e $m_2$ que estão a uma distância $R$ entre si tem magnitude

$$ |F| = G\frac{m_1m_2}{R^2},
$$
onde $G$ é uma constante chamada de *constante universal*.

* Podemos checar a consistência dessa relação à luz do *princípio da homogeneidade dimensional*.

* A constante universal é uma constante obtida empiricamente e é dada mais precisamente por
$$ G = 6.674\times 10^{−11} \texttt{m}^3\;\texttt{kg}^{−1}\;\texttt{s}^{−2}.
$$

* Assim, temos
$$ [G] = \frac{L^3}{MT^2}, \quad [m_1] = [m_2] = M, \qquad [R] = L,
$$
de modo que
$$ [F] = \frac{L^3}{MT^2}\frac{M^2}{L^2} = \frac{ML}{T^2}
$$
o que está de acordo com a dimensão de força.

* Isso mostra a consistência da fórmula acima.


## Teorema de Buckingham-Pi

Ou **Teorema Pi de Buckingham** ou **Teorema Buckingham-$\mathbf{\Pi}$**

* O teorema foi proposto em 1914 por Buckingham. O nome Pi se deve a notação matemática $\Pi$ para um produtório, neste caso, um produto de grandezas (variáveis e parâmetros), dado que os *grupos adimensionais* fornecidos pelo teorema são produtos de potências (inteiras) de notados por originalmente por $\pi_1$, $\pi_2$, etc.

* Os fundamentos do método de análise dimensional repousa em duas hipóteses:
1. **Universalidade:** todas as variáveis relevantes foram incluídas no modelo.
1. **Homogeneidade dimensional:** A relação física proposta pelo modelo é dimensionalmente homogênea


### O Teorema

> **Teorema (Buckingham-Pi)**  Considere um sistema com $n$ quantidades $q_1, \ldots, q_n$ em que $m$ dimensões fundamentais estão envolvidas. Então, $n-m$ grandezas adimensionais $\pi_1,\ldots, \pi_{n-m}$ podem ser definidas como potências das quantidades originais (um monômio nessas quantidades). 

> Além disso, cada equação (escalar) entre essas quantidades,
$$
f(q_1, \ldots, q_n) = 0,
$$
dado em modelo matemático associado ao sistema, pode ser substituída por uma relação correspondente entre os $\pi_i$:
$$
f^*(\pi_1, \ldots, \pi_{n-m}) = 0
$$

* As quantidades $q_i$ incluem tanto variáveis (e.g. posição) como parâmetros (e.g. aceleração da gravidade).

* Cada equação do modelo pode contemplar vetores, matrizes, etc, porém, para o objetivo da análise, todas as componentes escalares devem ser tratadas separadamente como quantidades.

* No centro da demonstração está o *Teorema do Núcleo e da Imagem*.


### Demonstração

* Formemos o produto
$$
\pi = q_1^{r_1} ~\cdots~ q_n^{r_n}.
$$

* Queremos saber para quais escolhas de $r_i$ o produto é adimensional.

* Para ver isso, olhamos para a dimensão do produto e substituímos cada $[q_i]$ em termos de suas dimensões fundamentais.

* Se temos apenas $m$ dimensões fundamentais $D_1, \ldots, D_m$, então essa substituição dá origem a um produto
$$ [\pi] = [q_1]^{r_1} ~\cdots~ [q_n]^{r_n} =  D_1^{s_1} \cdots D_m^{s_m},
$$
onde cada $s_j$, $j = 1, \ldots, m$, é uma combinação linear dos $r_i$, $i = 1, \ldots, n$. 


* Escrevemos a dependência linear dos $s_j$ nos $r_i$ como 
$$ s = A r, \qquad s=(s_1, \ldots, s_m)\in \mathbb{R}^m, \;r=(r_1, \ldots, r_N)\in\mathbb{R}^N.
$$

* Para que o produto $[\pi] = D_1^{s_1} \cdots D_m^{s_m}$ seja adimensional, devemos ter cada potência se anulando, i.e.
$$
s_i = 0, \quad \text{para} \quad i = 1, \ldots, m.
$$

* Isso nos leva a um sistema linear homogêneo de $m$ equações lineares para $n$ incógnitas $r_1, \ldots, r_n$.

* Ou seja, reduzimos o problema a se determinar o núcleo de uma matriz de tamanho $m \times n$, associada ao sistema linear, i.e.
$$ N(A) = \{ r\in \mathbb{R}^n; Ar = 0\}.
$$


* O Teorema da Imagem e do Núcleo nos diz que
$$ \dim N(A) + \dim \text{Im}(A) = n.
$$

* Como $\dim \text{Im}(A) \leq m$, obtemos
$$ \dim N(A) = n - \dim \text{Im}(A) \geq n - m.
$$

* Ou seja, a dimensão do núcleo é no mínimo $n-m$.

* Portanto, teremos no mínimo $n-m$ soluções linearmente indepentes, $r_k$, $k=1, \ldots, n-m$.

* Cada solução $r_k=(r_{k,1}, \ldots, r_{k,n})$, $k=1, \ldots, n-m$, nos dá uma quantidade adimensional
$$ \pi_k = q_1^{r_{k,1}} ~\cdots~ q_n^{r_{k,n}}.
$$

* Isso corresponde justamente às $n-m$ grandezas adimensionais do enunciado do teorema.


* Agora, para a segunda parte, considere 
$$ f(q_1, \ldots, q_n) = 0.
$$

* Obtivemos que
$$ \pi_k = q_1^{r_{k,1}} ~\cdots~ q_n^{r_{k,n}}, \qquad k=1, \ldots, n-m.
$$

* A dificuldade aqui é obter a relação inversa da dependência dos $q_i$'s nos $\pi_k$'s.

* De fato, isso é, em geral, impossível para todos os $q_i$'s, pois usualmente temos mais grandezas $q_i$, $i=1, \ldots, n$, do que quantidades adimensionais $\pi_k$, $k=1, \ldots, n-m$ (e equações correspondentes).

* Mas podemos resolver para $n-m$ grandezas:
$$ q_{n-m+1}, \ldots, q_n = \text{ monômios em } \pi_1, \ldots, \pi_{n-m}, q_1 \ldots q_{n-m}.
$$

* Isso nos leva a um novo modelo
$$ f^*(q_1, \ldots, q_{n-m}, \pi_1, \ldots, \pi_{n-m}) = 0.
$$

* Por fim, pelo princípio de homogeneidade dimensional, é possível mostrar que o termo acima é independente de $q_1, \ldots, q_{n-m}$, nos levando finalmente a
$$ f^*(\pi_1, \ldots, \pi_{n-m}) = 0.
$$


### O pêndulo simples

* Vamos rever o exemplo do pêndulo, tratado no terceiro caderno, à luz do Teorema de Buckingham-Pi.

* As variáveis envolvidas na descrição do fenômeno são o ângulo $\theta$ e o tempo $t$. E os parâmetros são a massa $m$ do prumo, o comprimento $\ell$ da haste rígida e a aceleração da gravidade $g$.

* Observe que agora estamos considerando o ângulo, que nao consideramos anteriormente, mas observe também que o ângulo é uma quantidade adimensional, pois podemos enxergá-lo como a razão entre o comprimento do arco $r\theta$ que ele descreve em uma circunferência e o raio $r$ da mesma.

* Assim, temos $[\theta] = 1$ (adimensional), $[t]=T$, $[m] = M$, $[\ell] = L$ e $[g]=LT^{-2}$. Portanto, temos as dimensões fundamentais $L$, $M$ e $T$.

* Ou seja, na notação do teorema, temos $n=5$ grandezas físicas e $m=3$ dimensões fundamentais.

* Assim, $n-m=2$ grandezas adimensionais $\pi_1$ e $\pi_2$ podem ser escritas como potências dos parâmetros e das variáveis originais.

* Como $\theta$ já é adimensional, podemos tomá-lo como uma dessas duas quantidades. Falta encontrar a outra.


### Segunda quantidade adimensional

* Para encontrar a outra quantidade adimensional, vamos descartar $\theta$ que já foi encontrado e formar o produto
$$
\pi_2 = t^{r_1} \ell^{r_2} m^{r_3} g^{r_4}.
$$

* Temos, 
$$ [t] = T, \quad [\ell] = L, \quad [m] = M, \quad [g] = LT^{-2}.
$$

* Substituindo no produto acima, obtemos
$$
[\pi_2] = T^{r_1} L^{r_2} M^{r_3} (LT^{-2})^{r_4} = T^{r_1 - 2 r_4} L^{r_2 + r_4} M^{r_3},
$$

* A condição de pedir que o produto seja adimensional nos dá o sistema linear
$$ 
\begin{cases}
  r_1 - 2 r_4  = 0, \\
  r_2 + r_4 = 0, \\
  r_3 = 0,
\end{cases}
$$

* Esse sistema possui infinitas soluções:
$$
\begin{cases}
  r_1 = 2s \\
  r_2 = -s \\
  r_3 = 0 \\
  r_4 = s
\end{cases}
$$
para $s\in \mathbb{R}$ qualquer. Isso nos dá
$$ \pi_2 = t^{2s} \ell^{-s}g^{s} = (t^2\ell^{-1}g)^s.
$$

* Uma solução em particular é com $s=1/2$ (apenas escolhido para que a potência em $t$ seja $1$, nada mais). 

* Nesse caso, temos a quantidade adimensional
$$ \pi_2 = t\sqrt{\frac{g}{\ell}}.
$$

* Note que a massa $m$ não está presente em nenhuma grandeza adimensional, ou seja, ela não influencia no movimento do pêndulo, pelo menos segundo as hipóteses que fizemos.


### Periodicidade

* Na análise acima, a quantidade $t$ é uma variável do problema. A relação **não** diz que $\pi_2$, e consequentemente $t$, é constante. Apenas diz que a quantidade $\pi_2 = t\sqrt{g/\ell}$ é adimensional.

* Além disso, nada na análise dimensional acima diz que o movimento do pêndulo é periódico.

* Mas se intuírmos, através da observação, que o movimento é (aproximadamente) periódico, então o período é uma grandeza característica do problema.

* E se consideramos esse período $\tau$ como parâmetro no sistema, no lugar da variável $t$, então obtemos a relação adimensional
$$ \pi_2 = \tau \sqrt{\frac{g}{\ell}}
$$

* Isso nos leva à relação para o período
$$ \tau \propto \sqrt{\frac{\ell}{g}}.
$$


### Pêndulo com pequenos ângulos

* Na análise acima, obtivemos as grandezas adimensionais $\pi_1 = \theta$ e $\pi_2 = \tau\sqrt{g/\ell}$. Nada afirma que elas sejam constantes.

* Mas é razoável assumirmos que haja uma relação entre essas quantidades da forma
$$
f(\pi_1, \pi_2) = 0
$$

* Podemos fazer uma aproximação de primeira ordem em $\pi_2$ e obter
$$
0 = f(\pi_1, 0) + \pi_2\frac{\partial f}{\partial \pi_2}(\pi_1, 0).
$$

* Podemos escrever
$$
\pi_2 \approx -\frac{f(\pi_1, 0)}{\frac{\partial f}{\partial \pi_2}(\pi_1, 0)}
$$

* Isso nos dá $\pi_2 \approx A(\pi_1)$, para $A(\pi_1) = - f_{\pi_1}(\pi_1,0)/f_{\pi_2}(\pi_1, 0)$.

* Portanto,
$$
\tau \approx A(\theta)\sqrt{\frac{\ell}{g}}.
$$


### Velocidade do som

* Considerando um certo fluido sob pressão $p$ e densidade $\rho$.

* Assumindo a hipótese de que a velocidade $v$ do som nesse meio depende apenas dessas duas quantidades, como podemos deduzir uma relação entre elas?

* Temos que a pressão é força por área e que a força é $ML/T^2$, logo
$$ [p] = \frac{M}{LT^2}
$$

* Além disso,
$$ [v] = \frac{L}{T}, \qquad [\rho] = \frac{M}{L^3}.
$$

* Assim,
$$ [v^\alpha p^\beta \rho^\gamma] = \left(\frac{L}{T}\right)^\alpha \left(\frac{M}{LT^2}\right)^\beta \left(\frac{M}{L^3}\right)^\gamma = L^{\alpha-\beta-3\gamma}M^{\beta + \gamma}T^{-\alpha-2\beta}.
$$

* Observe que temos $3$ quantidades, $p$, $\rho$ e $v$, para três dimensões, $L$, $M$, $T$. O Teorema de Buckingham-Pi nos garante *pelo menos* $n-m = 3 - 3 = 0$ quantidades adimensionais. Ou seja, não há nada garantido nesse caso. Mas nada nos impede de tentar.


* Para termos $\pi = v^\alpha p^\beta \rho^\gamma$ adimensioal, precisamos resolver o sistema
$$ \begin{cases}
  \alpha - \beta - 3\gamma = 0 \\
  \beta + \gamma = 0 \\
  -\alpha-2\beta = 0.
\end{cases}
$$

* Resolvendo,
$$ \begin{cases}
  \alpha = 2\gamma \\
  \beta = -\gamma,
\end{cases}
$$
com $\gamma$ qualquer.

* Isso nos leva às quantidades adimensionais
$$ \pi = v^{2\gamma}p^{-\gamma}\rho^\gamma
$$

* Ou seja, mesmo nesse caso em que $m=n$, ainda temos um sistema degenerado, com um núcleo de dimensão $1$.

* Assim, obtemos
$$ v \propto \sqrt{\frac{p}{\rho}}
$$

* Esta é uma aproximação. Na prática, efeitos térmicos influenciam na lei. Além disso, ela não é universal, no sentido da constante de proporcionalidade ser independente do gás. Leia mais sobre isso em [velocidade do som](https://pt.wikipedia.org/wiki/Velocidade_do_som)


## Exercícios

1. Considere uma corda de comprimento $\ell$ com uma extremidade fixa e a outra presa a um objeto de massa $m$. Suponha que esse sistema corda-massa gire em um movimento circular uniforme, com velocidade constante $v$. Esse movimento gera uma tensão $T$ na corda. A tensão é uma força. Use análise dimensional para deduzir a relação
$$ \frac{T\ell}{mv^2} = \text{constante.}
$$

1. No problema da velocidade do som em um meio, o que acontece no caso de assumirmos que as únicas quantidades relevantes são a própria velocidade $v$ e a pressão $p$, apenas? E no caso de assumirmos que as quantidades relevantes são $v$, $p$, $\rho$ e a temperatura $\theta$ do meio?

1. Em 1941, [G. I Taylor](https://pt.wikipedia.org/wiki/Geoffrey_Ingram_Taylor), um famoso físico e matemático britânico, com grandes contribuições à mecânica dos fluidos, fez uma [estimativa do rendimento da primeira bomba nuclear](https://en.wikipedia.org/wiki/Nuclear_weapon_yield) detonada pelos EUA, na chamada [experiência Trinity](https://pt.wikipedia.org/wiki/Experiência_Trinity). A estimativa foi feita apenas com análise dimensional e [dados da evolução da frente de onda obtidos de uma filmagem da explosão](http://nuclearweaponarchive.org/Usa/Tests/Trinity.html). Assumindo que os únicos parâmetros relevantes para o cálculo do rendimento $E$ (energia despendida) são a densidade $\rho$ do ar, o raio da onda de choque $r=r(t)$ e o instante de tempo $t$, encontre uma relação adimensional entre essas quantidades.

1. Estimar o atrito na parede de um tubo é uma das tarefas mais comuns em aplicações de engenharia envolvendo fluidos. Para tubos longos circulares e ásperos em regime de escoamento turbulento, a tensão de cisalhamento no parede, $\tau_w$, é uma função da densidade $\rho$, viscosidade (dinâmica) $\mu$, velocidade média $V$, diâmetro do cano $d$, e da altura de rugosidade da parede $\varepsilon$. Assim, funcionalmente podemos escrever a relação $\tau_w = f(\rho, \mu, V, d, \varepsilon)$.
  1. Usando o procedimento do Teorema de Buckingham-Pi, mostre como chegar nos grandezas adimensionais    
  $$
    C_f = \dfrac{\tau_w}{\rho V^2}, \quad Re = \dfrac{\rho V d}{\mu}, \quad \varepsilon^* = \dfrac{\varepsilon}{d},
  $$
  2. Conclua que a relação pode ser simplificada para $C_f = f^*(Re, \varepsilon^*)$. 
  3. Obs: $C_f$ é dito o *coeficiente de atrito na parede*; $Re$ é dito o número de Reynolds; e $\varepsilon^*$ dita a rugosidade relativa.


## Referências

1. C. Dym, Principles of Mathematical Modeling, 2nd ed, Academic Press, 2004.

1. E. A. Bender, An Introduction to Mathematical Modeling, Dover, 1978.

1. G. Barenblatt, G. -- *Scaling*, Cambridge University Press, 2003.

1. Groesen, E. van, and Molenaar, J. -- *Continuum Modeling in the Physical Sciences*, SIAM, 2007. 

1. [T. Tao, A mathematical formalisation of dimensional analysis](https://terrytao.wordpress.com/2012/12/29/a-mathematical-formalisation-of-dimensional-analysis/).
