
@def title = "Leis de conservação em um contexto Newtoniano"

# {{ get_title }}


## Sistema e leis de evolução

* Nesta parte, vamos considerar um sistema de $n$ partículas, com coordenadas

$$ \mathbf{r}=(\mathbf{r}_1,\ldots, \mathbf{r}_n)
$$

em um referencial inercial, onde $\mathbf{r}_i\in \mathbb{R}^3$ são as coordenadas espaciais de cada partícula, $i = 1, \ldots, n$.

* Nesse sistema, age um conjunto de forças

$$ \mathbf{F}(t,\mathbf{r}) = (\mathbf{F}_1(t,\mathbf{r}),\ldots, \mathbf{F}_n(t,\mathbf{r})),
$$

representando a combinação das forças agindo em cada partícula e dependendo da configuração geral do sistema.

* Pela segunda lei de Newton, temos

$$ m_i \mathbf{\ddot r}_i = \mathbf{F}_i(t,\mathbf{r}), \qquad i=1,\ldots, n.
$$


### Tipos de forças

* Vamos considerar uma separação das forças entre *forças internas,* de interação entre partículas, e *forças externas,* envolvendo cada partícula separadamente:

$$ \mathbf{F}(t,\mathbf{r}) = \mathbf{F}^{(i)}(\mathbf{r}) + \mathbf{F}^{(e)}(t,\mathbf{r}).
$$

* A forças internas são assumidas agindo entre pares de partículas e independentes explicitamente do tempo. Mais precisamente, a força interna $\mathbf{F}_i^{(i)}(\mathbf{r})$ agindo na partícula $i$ é assumida como sendo um *somatório* de forças de interação onde cada força no somatório ocorre apenas entre essa i-ésima partícula e uma das outras partículas:

$$ \mathbf{F}_i^{(i)}(\mathbf{r}) = \sum_{j\neq i} \mathbf{F}_{ij}(\mathbf{r}_i,\mathbf{r}_j).
$$


### A terceira lei de Newton

* Consideramos dois casos de sistemas, satisfazendo diferentes versões da terceira lei de Newton, de ação e reação:

* **Forma fraca da terceira lei de Newton:** As forças de interação entre duas partículas agem, em cada uma delas, com a mesma intensidade e em sentidos contrários:
    $$ \mathbf{F}_{ij}(\mathbf{r}_i,\mathbf{r}_j) = - \mathbf{F}_{ji}(\mathbf{r}_j,\mathbf{r}_i).
    $$

* **Forma forte da terceira lei de Newton:** As forças de interação entre duas partículas agem, em cada uma delas, com a mesma intensidade, em sentidos contrários e na direção que une essas duas partículas,
    $$ \mathbf{F}_{ij}(\mathbf{r}_i,\mathbf{r}_j) =  -\varphi(\mathbf{r}_i,\mathbf{r}_j)\frac{\mathbf{r}_i-\mathbf{r}_j}{\|\mathbf{r}_i-\mathbf{r}_j\|},
        \qquad \varphi_{ij}(\mathbf{r}_i,\mathbf{r}_j) = \varphi_{ji}(\mathbf{r}_j,\mathbf{r}_i).
    $$

Não assumimos nada de especial em relação à força externa, mas em geral ela depende apenas da posição da partícula em questão, ou seja $\mathbf{F}_i^{(e)}=\mathbf{F}_i^{(e)}(\mathbf{r}_i,t)$.

A terceira lei de Newton é relevante para a conservação dos momentos linear e angular do sistema. Para a conservação de energia, fazemos a hipótese de que as forças são conservativas, i.e. provenientes de um potencial $V(t,\mathbf{r})$:

$$ \mathbf{F}_i(\mathbf{r}) = -\frac{\partial V}{\partial\mathbf{r}_i}(t,\mathbf{r}), \qquad i=1,\ldots, n.
$$


## Momento linear

* O **momento linear total** $\mathbf{P}\in \mathbb{R}^3$ do sistema é definido pela somatório do momento linear $\mathbf{p}_i = m_i\mathbf{\dot r}_i$ de todas as partículas:

$$ \mathbf{P} = \sum_{i=1}^n m_i \mathbf{\dot r}_i.
$$

* A **massa total** do sistema é

$$ m = \sum_{i=1}^n m_i
$$

* Por sua vez, o **centro de massa** do sistema é dado por

$$ \mathbf{C}_M = \frac{1}{m}\sum_{i=1}^n m_i\mathbf{r}_i
$$

* Observe que o momento linear total do sistema é igual ao momento linear de uma partícula de massa $m$ localizada no centro de massa, como se o sistema estivesse todo concentrado no centro de massa:

$$ \mathbf{P} = m\mathbf{\dot C}_M.
$$


### Dinâmica do momento linear

* Somando as equações de movimento de todas as partículas obtemos

$$ \mathbf{\dot P} = \mathbf{F}_T,
$$

* Na expressão acima, $\mathbf{F}_T$ é a força total exercida no sistema, dada por

$$ \mathbf{F}_T(t,\mathbf{r}) = \sum_{i=1}^n \mathbf{F}_i(t,\mathbf{r})
$$

* Essa força total pode ser separada em um força total interna e uma força total externa:

$$ \mathbf{F}_T = \mathbf{F}_T^{(i)} + \mathbf{F}_T^{(e)},
     \qquad  \mathbf{F}_T^{(i)}(t,\mathbf{r}) = \sum_{i=1}^n \mathbf{F}_i^{(i)},
     \quad  \mathbf{F}_T^{(e)}(t,\mathbf{r}) = \sum_{i=1}^n \mathbf{F}_i^{(e)}
$$


### Conservação de momento linear

* O momento linear é conservado no caso em que as duas condições a seguir são satisfeitas:

1. As forças internas satisfazem a forma fraca da terceira lei de Newton; e
1. O força externa total é nula.

* Sob essas condições,

$$ \mathbf{\dot P} = 0.
$$

* Com isso, momento angular é constante ao longo do movimento, igual a um vetor fixo $\mathbf{P}_0\in \mathbb{R}^3$:

$$ \mathbf{P}(t) = \mathbf{P}_0, \qquad \forall t.
$$


## Momento angular

* O momento angular se refere a uma rotação em relação a algum ponto dado. É uma "quantidade de movimento" em torno desse ponto.

* O **momento angular total** do sistema em torno de um certo ponto $\mathbf{r}_0$ é o somatório do momento angular $m_i(\mathbf{r}_i-\mathbf{r}_0)\times\mathbf{\dot r}_i$ de todas as partículas:

$$ \mathbf{L}_{\mathbf{r}_0} = \sum_{i=1}^n m_i (\mathbf{r}_i-\mathbf{r}_0)\times \mathbf{\dot r}_i
       =\sum_{i=1}^n (\mathbf{r}_i-\mathbf{r}_0)\times \mathbf{p}_i.
$$


### Torque 

* Utilizando as leis de movimento de Newton, podemos mostrar que

$$ \mathbf{\dot L}_{\mathbf{r}_0} = 
         - \mathbf{\dot r}_0\times \mathbf{P} + \mathbf{N}_{\mathbf{r}_0},
$$

* Na expressão acima, temos o **torque** exercido pelas forças em relação ao ponto $\mathbf{r}_0$, dado por

$$ \mathbf{N}_{\mathbf{r}_0} = \sum_{i=1}^n (\mathbf{r}_i-\mathbf{r}_0)\times \mathbf{F}_i
$$

* Esse torque pode ser separado em torque interno e externo, relativo à separação da forças entre internas e externas:

$$ \mathbf{N}_{\mathbf{r}_0} = \mathbf{N}_{\mathbf{r}_0}^{(i)} +  \mathbf{N}_{\mathbf{r}_0}^{(e)},
    \qquad \mathbf{N}^{(i)}_{\mathbf{r}_0} = \sum_{i=1}^n (\mathbf{r}_i-\mathbf{r}_0)\times \mathbf{F}^{(i)}_i,
    \quad \mathbf{N}^{(e)}_{\mathbf{r}_0} = \sum_{i=1}^n (\mathbf{r}_i-\mathbf{r}_0)\times \mathbf{F}^{(e)}_i.
$$


### Conservação do momento angular

* O momento angular é conservado no caso em que as três condições a seguir são satisfeitas:

1. O ponto de referência $\mathbf{r}_0$ está fixo ou é o centro de massa;
1. As forças internas satisfazem a forma forte da terceira lei de Newton; e
1. O torque externo total é nulo.

* Sob essas condições,

$$ \mathbf{\dot L}_{\mathbf{r}_0} = 0.
$$

* Nesse caso, o momento angular é constante ao longo do movimento. 


## Energia total

* Considere, agora, o caso em que as forças são autônomas e conservativas, i.e. provenientes de um potencial $V=V(\mathbf{r})$ independente do tempo:

$$ \mathbf{F}_i(\mathbf{r}) = -\frac{\partial V}{\partial\mathbf{r}_i}(\mathbf{r}), \qquad i=1,\ldots, n.
$$

* A **energia total** do sistema é a soma da energia cinética com a energia potencial:

$$ E(\mathbf{r},\mathbf{\dot r}) = K(\mathbf{\dot r}) + V(\mathbf{r}),
$$

* A energia cinética total do sistema é dada por

$$ K(\mathbf{\dot r}) = \frac{1}{2}\sum_{i=1}^n m_i \|\mathbf{\dot r}_i\|^2
$$


### Conservação da energia total 

* Ao longo do movimento, a energia cinética varia de acordo com a equação

$$ \dot K = \sum_{i=1}^n \mathbf{\dot r}_i\cdot \mathbf{F}_i.
$$ 

* No caso de forças autônomas conservativas, temos

$$ \dot K = -\sum_{i=1}^n \mathbf{\dot r}_i\cdot \frac{\partial V}{\partial\mathbf{r}_i}(\mathbf{r})  = - \frac{\mathrm{d}}{\mathrm{d} t} V(\mathbf{r}),
$$

* Ou seja,

$$ \frac{\mathrm{d}}{\mathrm{d} t} (K+V) = 0
$$

* Nesse caso, a energia total $E = K + V$ é conservada.


## Exercícios

1. Demonstre a equação a seguir citada no texto:
$$ \frac{\mathrm{d} \mathbf{L}_{\mathbf{r}_0}}{\mathrm{d} t} = - \mathbf{\dot r}_0\times \mathbf{P} + \mathbf{N}_{\mathbf{r}_0}.
$$

1. Mostre, no caso em que o ponto de referência $\mathbf{r}_0$ está fixo, i.e. não varia com o tempo, ou esse ponto de referência é o centro de massa do sistema, $\mathbf{r}_0(t)=\mathbf{C}_M(t)$, então o termo $\mathbf{\dot r}_0 \times \mathbf{P}$ é nulo.

1. Mostre que se a forma forte da terceira lei de Newton vale para um sistema de forças $\mathbf{F}$, então o torque interno total é nulo, i.e. 
$$ \mathbf{N}^{(i)}_{\mathbf{r}_0} = \sum_{i=1}^n (\mathbf{r}_i - \mathbf{r}_0)\times \mathbf{F}^{(i)}_i = 0.
$$

1. Mostre que a energia cinética satisfaz
$$ \dot K = \sum_{i=1}^n \mathbf{\dot r}_i \cdot \mathbf{F}_i.
$$

1. No caso de uma partícula de massa $m$ e posição $\mathbf{r}\in \mathbb{R}^3$ satisfazendo a equação de Newton $\mathbf{\ddot r} = \mathbf{F}(t,\mathbf{r})$, mostre que a variação da energia cinética entre dois instantes $t_1$ e $t_2$ é dada por
$$ K_2 - K_1 = W_{12},
$$
onde $K_k=K(\mathbf{\dot r}(t_k))$ é a energia cinética no instante $t_k$, $k=1,2$, e $W_{12}$ é o **trabalho** realizado para deslocar essa partícula da posição $\mathbf{r}_1=\mathbf{r}(t_1)$ até a posição $\mathbf{r}_2=\mathbf{r}(t_2)$ através do caminho $\gamma$ parametrizado por $t \mapsto \mathbf{r}(\cdot)$:
$$ W_{12} = \int_\gamma \mathbf{F}(\mathbf{r}) \cdot \;\mathrm{d}\mathbf{r}
           = \int_{t_1}^{t_2} \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{\dot r}(t)\;\mathrm{d} t.
$$
