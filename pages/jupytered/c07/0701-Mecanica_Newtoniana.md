
@def title = "Mecânica Newtoniana"

# {{ get_title }}


## Fundamentos

* A base da mecânica clássica é a formulação Newtoniana de um sistema formado por $n\in\mathbb{N}$ partículas de massa  $m_i>0$, $i=1,\ldots, n$, cujas coordenadas espaciais são dadas por
$$ \mathbf{r}_i=\mathbf{r}_i(t)=(x_i(t),y_i(t),z_i(t))\in\mathbb{R}^3,
$$
em cada instante $t\in\mathbb{R}$.

* Cada partícula é sujeita a uma força $\mathbf{F}_i\in\mathbb{R}^3$.

* Em um referencial inercial, esse sistema satisfaz as equações diferenciais (segunda lei de Newton)
$$
  m_i \mathbf{\ddot r}_i = \mathbf{F}_i, \qquad i=1,\ldots,n,
$$
onde $\mathbf{\ddot r}_i$ indica a aceleração da $i$-ésima partícula, ou seja
a segunda derivada do vetor posição $\mathbf{r}_i(t)$ em relação à variável temporal $t$.

* Essas equações são as *leis de movimento* do sistema.

* A força $\mathbf{F}_i$ em cada partícula pode depender do instante de tempo $t$ e da posição das várias partículas, representando forças externas ao sistema e forças de interação entre a $i$-ésima partícula e as outras, de modo que em geral temos 
$$ \mathbf{F}_i=\mathbf{F}_i(t,\mathbf{r}), 
$$
onde 
$$ \mathbf{r}=(\mathbf{r}_1,\mathbf{r}_2,\ldots,\mathbf{r}_n)\in \mathbb{R}^{3n}
$$
são as coordenadas do sistema, ou seja, um vetor de dimensão $3n$ com as coordenadas espaciais de todas as partículas.

* Mais geralmente, para incluir efeitos eletromagnéticos, a força também pode depender da velocidade das partículas:
$$ \mathbf{F}_i=\mathbf{F}_i(t,\mathbf{r}, \mathbf{\dot r}), 
$$


## Tipos de forças

* Há vários tipos de forças: gravitacional, elétrica, magnética, elásticas, etc.

* Podemos, no entanto, separar alguns tipos de força segundo a sua natureza.

* Algumas forças são *internas*, decorrentes da interação entre as diversas particulas do próprio sistema.

* Outras são *externas*, provenientes de um "campo de força", associada a fatores externos ao sistema, muitas vezes correspondendo a uma situação aproximada em que as partículas consideradas no sistema não influenciam no movimento das partículas consideradas externas. Vamos ver alguns exemplos.

* Um exemplo típico de força externa é o campo gravitacional gerado por um corpo relativamente muito maciço e que não é incluído no conjunto de partículas do sistema, como na análise de um corpo em queda livre próximo à superfície da Terra ou mesmo na de um satélite artificial em órbita terrestre.

* Da mesma forma, podemos ter campos magnéticos e campos eletromagnéticos, onde certos objetos gerando esses campos não são incluídos no sistema de partículas do modelo.


## Exemplos de forças

* Há quatro forças fundamentais: fraca, forte, eletromagnética e gravitacional. O tratamento mais geral delas, no entanto, não é através de um sistema finito de partículas pontuais, mas sim através de teorias de campo. 

* Contudo, algumas situação podem ser bem aproximadas por um sistema discreto, como as que envolvem forças gravitacionais agindo entre partículas que se movem a velocidades bem inferiores à velocidade da luz, ou então entre partículas carregadas eletricamente.

* Essas forças podem ser entre partículas elementares ou entre conjuntos de partículas, como no caso da atração gravitacional entre corpos celestes.

* Há também forças ditas macroscópicas e provenientes da ação das forças fundamentais em certos conjuntos de partículas tratados como um único objeto, como no caso de forças elásticas entre duas massas ligados por uma mola.

* Várias forças de ligações químicas também entram nessa categoria, como a força de van der Walls e forças de torção.


## Forças internas

* Vamos ver alguns exemplos de forças internas.

* Veremos posteriormente que todas essas forças são *conservativas*, ou seja, provenientes de *potenciais*.


### Força gravitacional entre dois corpos 

* Sejam $\mathbf{r}_1, \mathbf{r}_2\in \mathbb{R}^3$ as coordenadas do centro de massa, em algum referencial inercial, de dois corpos com massas $m_1, m_2>0$, respectivamente.

* Cada corpo exerce uma *força de atração gravitacional* no outro, que depende das coordenadas dos dois corpos.

* Denotando $\mathbf{F}_{i,j}(\mathbf{r}_1,\mathbf{r}_2)$ a força que o corpo $j$ exerce no corpo $i$, para $i,j=1,2$, $i\neq j$, temos

$$
    \begin{align*}
      \mathbf{F}_{1,2}(\mathbf{r}_1,\mathbf{r}_2)& =-Gm_1m_2\frac{\mathbf{r}_1-\mathbf{r}_2}{\|\mathbf{r}_1-\mathbf{r}_2\|^3}, \\
      \mathbf{F}_{2,1}(\mathbf{r}_1,\mathbf{r}_2)&=-Gm_1m_2\frac{\mathbf{r}_2-\mathbf{r}_1}{\|\mathbf{r}_2-\mathbf{r}_1\|^3}.
    \end{align*}
$$


### Força eletrostática entre dois corpos carregados

* Sejam $\mathbf{r}_1,\mathbf{r}_2\in \mathbb{R}^3$ as coordenadas do centro de massa, em algum referencial inercial, de dois corpos carregados eletricamente com cargas $q_1, q_2\in \mathbb{R}$, respectivamente.
    
* Cada corpo exerce uma força elétrostática no outro, de acordo com a **lei de Coulomb**.

* Denotando $\mathbf{F}_{i,j}(\mathbf{r}_1,\mathbf{r}_2)$ a força que o corpo $j$ exerce no corpo $i$, para $i,j=1,2$, $i\neq j$, temos

$$
    \begin{align*}
      \mathbf{F}_{1,2}(\mathbf{r}_1,\mathbf{r}_2)& =Cq_1q_2\frac{\mathbf{r}_1-\mathbf{r}_2}{\|\mathbf{r}_1-\mathbf{r}_2\|^3}, \\
      \mathbf{F}_{2,1}(\mathbf{r}_1,\mathbf{r}_2)&=Cq_1q_2\frac{\mathbf{r}_2-\mathbf{r}_1}{\|\mathbf{r}_2-\mathbf{r}_1\|^3}.
    \end{align*}
$$


### Força elástica harmônica

* Sejam $\mathbf{r}_1,\mathbf{r}_2\in \mathbb{R}^3$ as coordenadas do centro de massa, em algum referencial inercial, de dois corpos com massas $m_1, m_2>0$, respectivamente.

* Suponha que esses dois corpos estejam ligados por uma mola harmônica de comprimento de equilíbrio $\ell>0$ e coeficiente de restituição $k>0$.

* Cada corpo sofre uma **força de restituição** proporcional ao deslocamento da mola em relação à posição de equilíbrio.

* Denotando por $\mathbf{F}_{i,j}(\mathbf{r}_1,\mathbf{r}_2)$ a força exercida no corpo $i$ pela mola que a liga ao corpo $j$, para $i,j=1,2$, $i\neq j$, temos

$$
    \begin{align*}
      \mathbf{F}_{1,2}(\mathbf{r}_1,\mathbf{r}_2)& = -k(\|\mathbf{r}_1-\mathbf{r}_2\|-d)\frac{\mathbf{r}_1-\mathbf{r}_2}{\|\mathbf{r}_1-\mathbf{r}_2\|}, \\
      \mathbf{F}_{2,1}(\mathbf{r}_1,\mathbf{r}_2)&=-k(\|\mathbf{r}_2-\mathbf{r}_1\|-d)\frac{\mathbf{r}_2-\mathbf{r}_1}{\|\mathbf{r}_2-\mathbf{r}_1\|}.
    \end{align*}
$$



## Campos de força externos

* No caso de forças gravitacionais, há situações em que um corpo é muito mais massivo que outro e a influência do menos massivo no mais massivo pode ser desprezada.

* Nesse caso, o sistema consiste apenas do menos massivo e a influência do mais massivo pode ser representada por um campo de forças externas.

* Mais precisamente, suponha, por exemplo, um objeto próximo à superfície da Terra. Considerando as coordenadas do objeto como $\mathbf{r}=(x,y,z)$, com a coordenada $z$ perpendicular à superfície da Terra e com o sentido de crescimento indicando um afastamento da superfície, então a força gravitacional exercida pela Terra nesse corpo que assumimos de massa $m>0$ é dada por

$$ \mathbf{F} = m\mathbf{g},
$$

onde $\mathbf{g}=(0,0,-g)$ e $g$ é a aceleração gravitacional próxima à superfície da Terra.

* Observe que essa força pode ser escrita na forma

$$ \mathbf{F} = m\mathbf{G}(\mathbf{r}),
$$

onde

$$ \mathbf{G} = \mathbf{g}
$$

é chamado de **campo gravitacional uniforme** próximo à superfície da Terra.

* A vantagem de escrever a força dessa forma é que se tivermos $n$ objetos de massas $m_1,\ldots,m_n$, então basta considerarmos o campo $\mathbf{G}(\mathbf{r})=\mathbf{g}$, de forma que a força gravitacional em cada objeto é dada por

$$ \mathbf{F}_i = m_i \mathbf{G}.
$$

* Há vários tipos de *campos de força*, correspondentes aos tipos de força.

* De fato, podemos ter campos gravitacionais, campos elétricos, campos magnéticos, campos eletro-magnéticos, etc.


### Campo gravitacional

* Um campo de vetores $\mathbf{G}=\mathbf{G}(\mathbf{r})$ de $\mathbb{R}^3$em $\mathbb{R}^3$ pode ser interpretado como um campo gravitacional quando a força exercida por esse campo em uma partícula de massa $m>0$ e posição $\mathbf{r}\in \mathbb{R}^3$ é dada por

$$ \mathbf{F}(\mathbf{r}) = m\mathbf{G}(\mathbf{r}).
$$

* É claro que $n$ partículas de massas $m_i$ e coordenadas $\mathbf{r}_i$, $i=1,\ldots, n$, sofrem forças

$$ \mathbf{F}_i(\mathbf{r}_i) = m_i\mathbf{G}(\mathbf{r}_i),
$$

respectivamente.

* Há vários casos partículares interessantes:


#### Campo gravitacional uniforme

* Esse é um caso partícular em que $\mathbf{G}$ é constante, geralmente denotado $\mathbf{G}(\mathbf{r})=\mathbf{g}$, para algum vetor $\mathbf{g}\in \mathbb{R}$ representando a aceleração gravitacional.

* No caso clássico em que $\mathbf{r}=(x,y,z)$ e $z$ representa a altura em relação à superfície da Terra, temos $\mathbf{g}=(0,0,-g)$, onde $g$ é a aceleração gravitacional próxima à superfície da Terra.


#### Campo gravitacional de um corpo celeste

* Considerando um corpo de massa $M$ e posição $\mathbf{r}_0\in \mathbb{R}^3$, em algum referencial inercial, o campo gravitacional gerado por esse corpo é dado por

$$ \mathbf{G}(\mathbf{r}) = -GM\frac{\mathbf{r}-\mathbf{r}_0}{\|\mathbf{r}-\mathbf{r}_0\|^3}.
$$

* Considerando um corpo de massa $m$, a força exercida neste corpo por esse campo gravitacional é

$$ \mathbf{F}(\mathbf{r}) = m\mathbf{G}(\mathbf{r}).
$$ 


#### Campo elétrico

* De maneira análoga, um campo de vetores $\mathbf{E} = \mathbf{E}(\mathbf{r})$ de $\mathbb{R}^3$ em $\mathbb{R}^3$ pode ser interpretado como um campo elétrico quando a força exercida por esse campo em uma partícula de carga $q>0$ e posição $\mathbf{r}\in \mathbb{R}^3$ é dada por

$$ \mathbf{F}(\mathbf{r}) = q\mathbf{E}(\mathbf{r}).
$$

* Um capacitor de placa paralela, por exemplo, gera um campo elétrico uniforme semelhante ao campo gravitacional uniforme.


#### Campo magnético agindo em partículas carregadas eletricamente

* Um campo magnético $\mathbf{B} = \mathbf{B}(\mathbf{r})$ de $\mathbb{R}^3$ em $\mathbb{R}^3$ exerce uma força em uma partícula carregada eletricamente que é de uma natureza um pouco mais complicada que às anteriores.

* Sendo $q$ a carga elétrica, $\mathbf{r}\in \mathbb{R}^3$ a posição, e $\mathbf{\dot r}\in \mathbb{R}^3$ a velocidade, então essa força é dada por

$$ \mathbf{F}(\mathbf{r},\mathbf{\dot r}) = q\mathbf{\dot r} \times \mathbf{B}(\mathbf{r}).
$$

* Campos magnéticos uniformes aparecem, por exemplo, em aceleradores circulares de partícula, com o plano em que as partículas circulam sendo perpendicular ao campo magnético. 


#### Campo eletromagnético

* Um campo eletromagnético $(\mathbf{E}, \mathbf{B})$ age em uma partícula carregada eletricamente através de uma força chamada de **força de Lorentz**, que é dada por

$$ \mathbf{F}(\mathbf{r},\mathbf{\dot r}, t) = q(\mathbf{E}(\mathbf{r}, t) + \mathbf{\dot r}\times \mathbf{B}(\mathbf{r},t)).
$$



## Campos conservativos

* Vamos considerar agora o caso em que as forças no sistema são conservativas, provenientes de um campo potencial escalar.

* No caso em que as forças dependem apenas da posição das partículas do sistema, um campo de forças é conservativo quando é menos o gradiente de uma função escalar, dita potencial do campo.

* Mais precisamente, $\mathbf{F} =(\mathbf{F}_1, \mathbf{F}_2,\ldots, \mathbf{F}_n)$ é um **campo conservativo** quando existe uma função escalar $V$, chamada de **potencial** do campo, tal que

$$ \mathbf{F}(t,\mathbf{r})=-\frac{\partial V}{\partial\mathbf{r}}(t,\mathbf{r}),
$$

onde $\partial/\partial\mathbf{r}$ indica as derivadas parciais apenas em relação às coordenadas espaciais

$$ \mathbf{r}=(\mathbf{r}_1,\mathbf{r}_2,\ldots,\mathbf{r}_n).
$$

* Lembramos que cada $\mathbf{r}_i=(x_i,y_i,z_i)$ tem três coordenadas, ou seja,

$$ \frac{\partial V}{\partial\mathbf{r}} = 
     \left(\frac{\partial V}{\partial\mathbf{r}_1}, \ldots, \frac{\partial V}{\partial\mathbf{r}_n}\right)
     = \left(\frac{\partial V}{\partial x_1}, \frac{\partial V}{\partial y_1}, 
           \frac{\partial V}{\partial z_1}, \ldots, \frac{\partial V}{\partial x_n}, 
           \frac{\partial V}{\partial y_n}, \frac{\partial V}{\partial z_n} \right).
$$

* A força em cada partícula $i$ tem a forma

$$ \mathbf{F}_i(t,\mathbf{r}) = - \frac{\partial V}{\partial\mathbf{r}_i}(t,\mathbf{r})
     = - \left(\frac{\partial V}{\partial x_i}, \frac{\partial V}{\partial y_i}, \frac{\partial V}{\partial z_i}\right).
$$


### Exemplos de campos conservativos

* **Campo gravitacional uniforme:** Em coordenadas $xyz$, o campo gravitacional uniforme $\mathbf{F}(x, y, z) = m\mathbf{g}$, $\mathbf{g} = (0, 0, -g)$ possui como potencial a função escalar $V(x,y,z) = mgz$.

* **Campo gravitacional:** Um sistema gravitacional de $n\in \mathbf{N}$ corpos de massas $m_i>0$ e posições $\mathbf{r}_i\in \mathbb{R}^3$, $i=1,\ldots, n$, é um sistema conservativo com potencial gravitacional 
$$
    \begin{align*}
      V(\mathbf{r}) & = -\frac{1}{2}\sum_{\genfrac{}{}{0pt}{}{j,k=1, \ldots, n}{j\neq k}} 
         \frac{Gm_jm_k}{\|\mathbf{r}_j-\mathbf{r}_k\|} \\
         & = -\sum_{\genfrac{}{}{0pt}{}{j,k=1, \ldots, n}{j< k}} \frac{Gm_jm_k}{\|\mathbf{r}_j-\mathbf{r}_k\|} \\
         & = - \sum_{j=1}^{n-1} \sum_{k=j+1}^n \frac{Gm_jm_k}{\|\mathbf{r}_j-\mathbf{r}_k\|}.
    \end{align*}
$$

* **Mola harmônica:** A força de restituição de uma mola harmônica ligando duas massas $m_1$ e $m_2$ em posições $\mathbf{r}_1$ e $\mathbf{r}_2$ é uma força conservativa com potencial

$$ V_{ij}(\mathbf{r}) =\frac{1}{2} \kappa(|\mathbf{r}_i - \mathbf{r}_j|-\ell_0)^2,
$$

onde $\kappa$ é o coeficiente de restituição da mola, $\ell_0$ é o comprimento de equilíbrio da mola livre e $\mathbf{r} = (\mathbf{r}_1, \mathbf{r}_2) \in \mathbb{R}^{6}$.

* **Campo elétrico:** A força elétrica que age entre dois corpos carregados eletricamente com cargas $q_1, q_2\neq 0$ e posições $\mathbf{r}_1, \mathbf{r}_2$, tem a forma

$$ \mathbf{F}_{ij}(\mathbf{r}) = \frac{q_iq_j}{4\pi\epsilon_0}\frac{\mathbf{r}_i-\mathbf{r}_j}{\|\mathbf{r}_i-\mathbf{r}_j\|^3},
$$

onde $\epsilon_0$ é a constante de permissividade do meio. O potencial elétrico correspondente é costumeiramente denotado por $\phi$, ao invés de $V$, e tem a forma

$$ \phi(\mathbf{r}) = \frac{1}{4\pi \epsilon_0}\frac{q_iq_j}{\|\mathbf{r}_i-\mathbf{r}_j\|},
$$

onde $\mathbf{r} = (\mathbf{r}_1, \mathbf{r}_2) \in \mathbb{R}^{6}$. No caso de várias partículas carregadas eletricamente, basta somar o potencial para cada par de cargas, com a mesma ressalva feita no caso gravitacional, para evitar contar cada potencial duas vezes.


### Potenciais vetoriais

* Os campos magnético e eletromagnético também possuem campos potenciais, mas os seus potenciais não são mais funções escalares; são potenciais vetoriais.

* O **potencial magnético** é um campo vetorial $\mathbf{A}$ cujo rotacional é igual ao campo magnético:

$$ \boldsymbol{\nabla} \times \mathbf{A} = \mathbf{B}.
$$

* No caso de um campo eletromagnético $(\mathbf{B}, \mathbf{E})$, o potencial magnético $\mathbf{A}$ pode ser combinado com o potencial elétrico $\phi$ visto anteriormente para nos dar o **potencial eletromagnético**.

* Nesse caso, o campo eletromagnético são obtidos do potencial eletromagnético por

$$ \mathbf{B} = \boldsymbol{\nabla} \times \mathbf{A}, \qquad \mathbf{E} = - \boldsymbol{\nabla} \phi - \frac{\partial \mathbf{A}}{\partial t}.
$$

* Esses tipos de campos serão mais explorados na parte de Mecânica Lagrangiana.


## Exercícios

1. Verifique que uma força $\mathbf{F}(\mathbf{r})=(F_x,F_y,F_z)\in \mathbb{R}^3$ de um sistema de uma única partícula com coordenadas $\mathbf{F}=(x,y,z)\in\mathbb{R}^3$ é conservativo se, e somente se, o rotacional de $\mathbf{F}(\mathbf{r})$ se anula para todo $\mathbf{r}\in \mathbb{R}^3$, i.e.
$$ \boldsymbol{\nabla} \times \mathbf{F}(\mathbf{r}) = (0,0,0), \qquad \forall\;\mathbf{r}\in \mathbb{R}^3.
$$

1. Verifique que uma força $\mathbf{F}(\mathbf{r})\in \mathbf{R}^3$ de um sistema de uma única partícula com coordenadas $\mathbf{r}\in \mathbb{R}^3$ é conservativo se, e somente, se o trabalho
$$ \int_\gamma \mathbf{F}(\mathbf{r})\cdot \mathrm{d} \mathbf{r} = 0, 
$$
ao longo de qualquer caminho fechado suave $\gamma$ (i.e. $\gamma$ é uma curva parametrizada suave $\mathbf{r}:[t_0,t_1]\rightarrow \mathbb{R}^3$ com $\mathbf{r}(t_0)=\mathbf{r}(t_1)$.)

1. Escreva o potencial gravitacional uniforme em um referencial inclinado de uma ângulo $\alpha$, apropriado para o movimento de uma partícula deslizando sobre um plano inclinado próximo à superfície da Terra. 

1. Escreva o potencial associado a três molas harmônicas, ligando cada par de uma série de três partículas de massa $m_i$ no espaço, como em um triângulo, e onde cada mola tem um coeficiente de restituição $k_i$ e um comprimento de equilíbrio $\ell_i$, $i=1,2,3$.     

1. Mostre que se as forças entre duas partículas i) atuam na direção que une essas duas partículas; ii) têm sentidos contrários; iii) têm a mesma magnitude; e iv) essa magnitude dependente apenas da distância entre essas duas partículas, então esse conjunto de forças  é conservativo. Mais precisamente, assuma que $\mathbf{F}_{ij}(\mathbf{r})$ tem a forma
$$ \mathbf{F}_{ij}(\mathbf{r}) = -\varphi(\|\mathbf{r}_i-\mathbf{r}_j\|)\frac{\mathbf{r}_i-\mathbf{r}_j}{\|\mathbf{r}_i-\mathbf{r}_j\|},
$$
onde $\varphi:(0,\infty)\rightarrow \mathbb{R}$, e mostre que o potencial é dado por 
$$ V_{ij}(\mathbf{r})=\psi(\|\mathbf{r}_i-\mathbf{r}_j\|),
$$
para uma determinada função escalar $\psi$.
