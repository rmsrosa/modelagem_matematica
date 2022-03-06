
@def title = "Exemplos de tipos de modelagem"

# {{ get_title }}

* empírico
* análise dimensional
* ad-hoc
* mecanicista
  * heurístico
  * fundamental


## Tipos de modelagem

O processo de modelagem pode seguir vários caminhos:

* **empírico:** através da observação, seja de fenômenos naturais ou de experimentos controlados
* **análise dimensional:** baseado na análise das dimensões de quantidades envolvidas no fenômeno
* **ad-hoc:** introduzida sem muito fundamento e sem muita capacidade de generalização/extrapolação
* **mecanicista:** baseado em mecanismos envolvidos no fenômeno
  * **heurístico:** baseada em mecanismos qualitativos (e.g. os termos de interação entre duas espécies)
  * **fundamental:** baseado em relações/modelos bem estabelecidas e "precisos" (e.g. mecânica, termodinâmica, lei ação de massas)

Vale ressaltar que vários desses processos estão interligados.


## Modelagem empírica, alometria e a tilápia-do-nilo

* Como exemplo de modelagem empírica, vamos considerar um problema em alometria.
* **Alometria** trata do estudo entre as escalas de diversos atributos de um dado organismo. Por exemplo, relação entre tamanho do coração e a idade do indivíduo, entre o comprimento e a massa de um organismo, entre sua capacidade de locomoção e o tamanho dos membros de um animal -- asas, patas, pernas, barbatanas).


### Tilápia-do-nilo

* A tabela abaixo mostra dados da evolução da massa e do comprimento da *Tilápia-do-nilo* criada em cativeiro:

| Days of culture | 1 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| Massa (g) | 28.6±4.2 | 88.6±1.4 | 177.6±3.6 | 313.8±12.8 | 423.7±12.7 | 774.4±23.6 |
| Comprimento (cm) | 10.9±0.4 | 15.3±0.4 | 19.1±0.2 | 22.8±0.5 | 26.3±0.6 | 31.3±0.4 |

Fontes:
1. [Gayon, J. (2000) History of the Concept of Allometry. American Zoologist 40: 748-758](https://web.archive.org/web/20070930184104/http://www-ihpst.univ-paris1.fr/_sources/jgay_allometry.pdf)
2. [Shingleton, A. (2010) Allometry: The Study of Biological Scaling. Nature Education Knowledge 3(10):2](https://www.nature.com/scitable/knowledge/library/allometry-the-study-of-biological-scaling-13228439/)
2. [T. S. de Castro Silva, L. D. dos Santos, L. C. R. da Silva, M. Michelato, V. R. B. Furuya, W. M. Furuya, Length-weight relationship and prediction equations of body composition for growing-finishing cage-farmed Nile tilapia, R. Bras. Zootec. vol.44 no.4 Viçosa Apr. 2015](https://www.scielo.br/scielo.php?script=sci_arttext&pid=S1516-35982015000400133)


### Peso x comprimento

* Analisando os dados de comprimento e de peso da *tilápia-do-nilo*, obtemos a seguinte relação aproximada, que pode ser considerada um **lei empírica para o seu crescimento**:
$$ y = 0.0203 x^{3.0604}
$$
* Diversos estudos como esse, iniciados no final do século XIX, levaram a uma lei geral de escalas entre duas quantidades $y$ e $x$ na forma de uma lei de potência
$$ y = bx^\alpha.
$$


![Alometria tilápia-do-Nilo](/assets/attachments/img/NileTilapia_WeightLength_512x373.png)


## Análise dimensional e o período de um pêndulo

* Na **análise dimensional**, busca-se obter uma relação entre os parâmetros envolvidos em um determinado problema.
* Usualmente, essa analise vem embutida com uma **hipótese de universalidade**, assumindo que o problema só depende dos parâmetros escolhidos.


### Pêndulo


![pêndulo](/assets/attachments/img/pendulum_256x256.png)


* Como exemplo, considere um pêndulo com haste de comprimento $\ell$ e massa $m$.
* Sob a ação da força gravitacional, cuja aceleração é denotada por $g$, o pêndulo oscila, com um período $\tau$.
* Buscamos entender como esse período depende dos outros parâmetros.
* A fórmula obtida pode inclusive ser utilizada para se estimar um dos parâmetros em função dos outros.


### Parâmetros e dimensões

* Cada sistema possui um **sistema de dimensões**.
* No caso de um sistema mecânico, temos as dimensões de *comprimento* $L$, *massa* $M$ e *tempo* $T$.
* Outros sistemas podem incluir unidades de temperatura $\Theta$, corrent elétrica $A$, intensidade luminosa $CD$, etc..
* Associado a isso, temos um **sistema de unidades**. Por exemplo, o sistema MKS utiliza as unidades de *metro*, *quilograma* e *segundo* para as dimensões de comprimento, massa e tempo, respectivamente, mas que não entram explicitamente na análise dimensional.
* Cada parâmetro está ligado a uma das dimensões.
* Denotamos a dimensão de uma quantidade colocando-a entre colchetes, e.g. $[m], [\ell], [g], [\tau]$.
* Assim, temos
$$ [m]=M, \quad [\ell]=L, \quad [g]=L/T^2, [\tau]=T.
$$


### Hipótese de universalidade e lei dimensional

* Como dito acima, a análise dimensional vem usualmente acompanhada de uma **hipótese de universalidade**.
* No caso do pêndulo, podemos fazer a hipótese de que o período é caracterizado apenas pela combinação dos parâmetros $\ell$, $m$ e $g$, por exemplo,
$$\tau \propto m^a \ell^b g^c.
$$
* Essa combinação tem dimensão
$$ [ m^a \ell^b g^c] = M^a L^b \frac{L^c}{T^{2c}}.
$$
* A única possibilidade disso ser de dimensão $T$ é com
$$ a = 0, \quad b = -c = 1/2, \qquad c = -1/2.
$$
* Assim, obtemos a relação
$$ \tau \propto\sqrt{\frac{\ell}{g}}.
$$
* O símbolo $\propto$ significa que uma quantidade é diretamente proporcional à outra, ou seja é um múltiplo constante da outra: $x \propto y$ é equivalente a $x = ky$ para algum $k\neq 0$.
* A constante de proporcionalidade, no entanto, não segue diretamente desssa análise.
* Além disso, desprezamos a resistência do ar, a variação na temperatura ambiente, a elasticidade da haste, o ângulo da oscilação, e outras parâmetros menos tangíveis.
* Mais adiante, veremos o Teorema de Buckinham-Pi, que formaliza mais essa análise.


## Heurístico

* Em uma modelagem heurística, aproveitamos algum mecanismo qualitativo que nos parece razoável para o problema.
* Um ótimo exemplo é o de dinâmica populacional.
* Seja de um ou mais organismos, interagindo com o meio e entre si.


### Dinâmica populacional de um único organismos

* Imaginemos uma situação controlada em laboratório, e.g. em um experimento em um placa de Petri.
* Seja $x=x(t)$ é a população (e.g. número de células) de um organismo (e.g. fungo, bactéria) em função do tempo.
* O organismo pode se multiplicar de diversas maneiras (e.g. divisão celular, brotamento).
* Tipicamente, cada organismo dá origem a um ou mais novos organismos a certos intervalos de tempo.
* Quanto mais organismos em um determinado instante, proporcionalmente mais novos organismos são gerados.
* E quanto maior o tempo decorrido, proporcionalmente mais novos organismos são gerados.
* Isso nos leva a relação $\Delta x \propto x\Delta t$.


### Taxa temporal de evolução

* A relação $\Delta x \propto x\Delta t$ é imprecisa, pois temos $x=x(t)$ do lado direito afetando toda a evolução durante o intervalo $\Delta t$.
* Isso não leva em consideração que, ao longo desse intervalo de tempo, pode já haver novos organismos participando de mais gerações, caso esse intervalo seja muito grande.
* Assim, é adequado considerarmos a **taxa temporal** de evolução, obtida tomando-se o limite quando $\Delta t \rightarrow 0$:
$$ \frac{\text{d} x}{\text{d} t} \propto x
$$
* Isso nos dá uma lei **heurística** para o crescimento do organismo.


### Relação com lei empírica

* Observe que a solução é $x(t) = x(0) e^{kt}$, onde $k$ é a constante de proporcionalidade na relação anterior.
* Essa solução poderia ter sido obtida experimentalmente, medindo-se a população do organismo, para vários tipos de bactérios e fungos.
* Nesse caso, teríamos a **lei empírica** $\log x(t) - \log x(0) \propto t$, válida pra qualquer organismo simples desse tipo.
* Ou mais explicitamente, $x(t) = x(0) e^{kt}$, com $k$ dependendo do organismo.


## Ad-hoc - crescimento com limitação

* Modelagem **ad-hoc** é utilizada quando não temos algum mecanismo razoável para considerar algum aspecto da modelagem.
* Ela é muito utilizada em combinação com outras modelagens, para complementar alguma informação faltante.
* No caso de crescimento populacional, por exemplo, isso pode aparecer ao considerarmos que o organismo depende de nutrientes para se desenvolver e gerar novos organismos.
* Podemos imaginar situações em que essa quantidade de nutrientes é limitada, como em um placa de Petri.
* Assim, o crescimento será afetado pelo tamanho da população, com a taxa de crescimento diminuindo conforme a população aumenta.


### Relação com lei empírica

* Podemos (e devemos) usar dados reais para **validar** o modelo *ad-hoc* acima.
* Mas também podemos partir dos dados e deduzir o modelo $x'=\alpha x - \beta x^2$ através do ajuste de parâmetros.
* Dessa maneira, essa forma do modelo é considerado um *ansatz*.
* De acordo com o dicionário Oxford, ansatz é uma hipótese que é feita para facilitar encontrar a solução de um problema.
* Coletando dados esses dados de crescimento em situações de recursos limitados, para uma série de organismos, podemos verificar e concluir essa lei de forma **empírica**.


### Crescimento limitado com termo quadrático

* Um hipótese comum é assumir que isso é afetado por um termo de ordem quadrática, levando-nos à equação logística:
$$ \frac{\text{d}x}{\text{d}t} = \alpha x - \beta x^2 \quad \Longleftrightarrow \quad \frac{\text{d}x}{\text{d}t} = \alpha ( 1 - \frac{\beta}{\alpha} x) x.
$$
* Observe que para $0< x \ll \alpha/\beta$, o termo quadrático é desprezível, e obtemos o crescimento natural.
* Mas para $x \sim \alpha/\beta$, o termo quadrático reduz consideravelmente a taxa de crescimento.
* Observe, no entanto, que isso foi uma dedução essencialmente matemática, em termos de ordem de grandeza, sem levar em consideração algum mecanismo especial. O mesmo efeito seria alcançado com qualquer potência maior $p>1$, não necessariamente $p=2$. Nesse sentido, foi uma escolha *ad-hoc*.


## Fundamental

* A Mecânica Clássica é um perfeito exemplo disso.
* O modelo dado pela equação 
$$ m\ddot x = F(x,\dot x)
$$
vale em geral, desde que sob condições macroscópicas mas sem exageros astronômicos e em velocidades bem mais baixas do que a velocidade da luz.
* Em alguns casos, é preciso considerar a variação de massa do objeto (e.g. foguete)
* Em outras situações, os modelos de relatividade restrita, relatividade geral, mecânica quântica, entre outros, são necessários.
* Muitos modelos considerados fundamentais surgiram baseados também em análises empíricas, dimensionais, com termos ad-hoc e/ou de forma heurística, mas ganharam solidez e confirmação com o tempo.
