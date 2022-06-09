
@def title = "Hamiltonianos"

# {{ get_title }}

* As equações de Euler-Lagrange formam um sistema de equações de segunda ordem.

* Em várias situações, como visto em Equações Diferenciais, pode ser útil trabalhar com um sistema de equações de primeira ordem.

* Vamos ver, aqui, como transformar as equações de Euler-Lagrange em um sistema de equações de primeira ordem na forma de um sistema de um tipo partícular chamado de sistema hamiltoniano.


## Obtendo o Hamiltoniano no caso de um grau de liberdade

* Um **sistema hamiltoniano bidimensional** é da forma

$$ \begin{cases}
     \displaystyle \dot q = \frac{\partial H}{\partial p}(q,p), \\
     \displaystyle \dot p = - \frac{\partial H}{\partial q}(q,p),
   \end{cases}
$$

* Nesse sistema, $H=H(p,q)$ é o **Hamiltoniano** do sistema.

* Em um sistema dessa forma, o hamiltoniano é conservado ao longo do movimento, ou seja, dada uma solução $(q(t),p(t))$ do sistema, temos

$$ \frac{\mathrm{d}}{\mathrm{d} t} H(q(t),p(t)) = 
      \frac{\partial H}{\partial q} \dot q + \frac{\partial H}{\partial p}\dot p
      =  \frac{\partial H}{\partial q} \left( \frac{\partial H}{\partial p}\right) 
          + \frac{\partial H}{\partial p}\left(- \frac{\partial H}{\partial q}\right)
       = 0.
$$


### Forma compacta de se escrever o sistema Hamiltoniano

* Uma forma mais compacta de escrever um sistema Hamiltoniano faz uso do gradiente de $H(q,p)$ e de uma matriz antisimétrica $J$, dados por 

$$ \nabla H(q,p) = \left( \frac{\partial H}{\partial q}(q,p), \frac{\partial H}{\partial p}(q,p) \right), \qquad J = \left[ \begin{matrix} 0 & 1 \\ -1 & 0 \end{matrix} \right].
$$

* Assim, podemos escrever

$$ (\dot q,\dot p) = J \nabla H(q,p).
$$

* Observe que o operador $J:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ leva um vetor em um outro vetor perpendicular ao original. Dessa forma, o sistema indica que o vetor velocidade é perpendicular ao vetor gradiente e, portanto, tangente à curva de nível do hamiltoniano, dando uma interpretação geométrica para o fato mostrado acima de que o hamiltoniano é conservado ao longo do movimento.


### Hamiltoniano a partir da integral de Jacobi

* Em vários exemplos o hamiltoniano é essencialmente a energia total do sistema. Mas nem sempre.

* Em geral, partindo de uma formulação Lagrangiana de um problema com um grau de liberdade, onde conhecemos o Lagrangiano $L(q,\dot q)$, é natural procurarmos o Hamiltoniano como sendo a integral de Jacobi do sistema, que é uma quantidade conservada, nesse caso de invariância temporal do Lagrangiano. 

* A integral de Jacobi tem a forma

$$ h(q,\dot q) = \dot q \frac{\partial L}{\partial \dot q}(q,\dot q)- L(q,\dot q).
$$

* Considere o momento generalizado

$$ p = \frac{\partial L}{\partial \dot q}(q,\dot q)
$$

* Usando o momento generalizado como uma nova variável dependente, no lugar da velocidade generalizada $\dot q$, procuramos inverter a relação acima e escrever $\dot q$ em função de $q$ e $p$:

$$ \dot q = \dot q(q,p).
$$

* Assim, obtemos o Hamiltoniano

$$ H(q,p) = p\dot q(q,p) - L(q,\dot q(q,p)).
$$

* Temos

$$
\begin{align*}
  \frac{\partial H}{\partial p}(q,p) & = 
      \dot q(q,p) + p\frac{\partial \dot q}{\partial p}(q,p) 
         - \frac{\partial L}{\partial \dot q}(q,\dot q(q,p))\frac{\partial \dot q}{\partial p}(q,p) \\
         & = \dot q + p\frac{\partial \dot q}{\partial p}(q,p) - p\frac{\partial \dot q}{\partial p}(q,p) \\
         & = \dot q.
\end{align*}
$$

* Usando as equações de Euler-Lagrange,
$$
\begin{align*}
  \frac{\partial H}{\partial q}(q,p)
    & = p\frac{\partial \dot q}{\partial q}(q,p)
         - \frac{\partial L}{\partial q}(q,\dot q(q,p))
         - \frac{\partial L}{\partial \dot q}(q,\dot q(q,p))\frac{\partial \dot q}{\partial q}(q,p) \\
    & = p\frac{\partial \dot q}{\partial q}(q,p)
         - \frac{\partial L}{\partial q}(q,\dot q(q,p))
         - p\frac{\partial \dot q}{\partial q}(q,p) \\
    & = - \frac{\partial L}{\partial q}(q,\dot q(q,p)) \\
    & = - \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot q}(q,\dot q(q,p)) \\
    & = - \frac{\mathrm{d}}{\mathrm{d} t} p \\
    & = - \dot p.
\end{align*}
$$

* Logo, chegamos ao sistema hamiltoniano

$$ \begin{cases}
     \displaystyle \dot q = \frac{\partial H}{\partial p}(q,p), \\
     \displaystyle \dot p = - \frac{\partial H}{\partial q}(q,p).
   \end{cases}
$$

* Esse sistema é também chamado de **equações de Hamilton.**


### Exemplo do pêndulo planar

* Como exemplo, vamos considerar o Lagrangiano associado ao pêndulo planar, cujo Lagrangiano é

$$ L(\theta,\dot\theta) = \frac{1}{2}m\ell^2\dot\theta^2 + mg\ell\cos\theta.
$$

* Seja $\psi$ o momento conjugado à coordenada generalizada $\theta$, que nesse
caso é o momento angular do sistema, e é dado por

$$ \psi = \frac{\partial L}{\partial \dot\theta}(\theta,\dot\theta)
     = m\ell^2\dot\theta
$$

* Invertendo essa relação, temos

$$ \dot\theta = \dot\theta(\psi) = \frac{1}{m\ell^2}\psi.
$$

* A integral de Jacobi é

$$ h(\theta,\dot\theta)  = \dot\theta\psi - L(\theta,\dot\theta).
$$

* Substituindo $\dot\theta$ por $\dot\theta(\psi)= \psi/m\ell^2$, obtemos o Hamiltoniano

$$ H(\theta,\psi) = \frac{1}{2m\ell^2}\psi^2 -mg\ell\cos\theta.
$$

* E as equações de Hamilton tomam a forma conhecida do sistema de primeira ordem para o pêndulo simples.

$$ \begin{cases}
     \displaystyle \dot \theta = \frac{1}{m\ell^2}\psi, \\
     \displaystyle \dot \psi = -mg\ell\sin\theta.
   \end{cases}
$$


## Obtendo o Hamiltoniano no caso de vários graus de liberdade

* A idéia é a mesma. Partimos de um Lagrangiano de um sistema com coordenadas generalizadas $\mathbf{q}\in \mathbb{R}^d$, $d\in \mathbb{N}$,

$$ L(\mathbf{q},\mathbf{\dot q}).
$$

* Temos a integral de Jacobi, onde, novamente, $\mathbf{p}$ é o momento generalizado do sistema:

$$ h(\mathbf{q},\mathbf{\dot q}) = \mathbf{\dot q}\cdot\mathbf{p} - L(\mathbf{q},\mathbf{\dot q}), \qquad \mathbf{p} = \nabla_{\mathbf{\dot q}} L(\mathbf{q},\mathbf{\dot q})
$$

* Em certos casos, podemos inverter a relação acima e escrever a velocidade generalizada em termos do momento generalizado (e das coordenadas generalizadas),

$$ \mathbf{\dot q} = \mathbf{\dot q}(\mathbf{q},\mathbf{p}).
$$

* Assim, o Hamiltoniano é dado por

$$ H(\mathbf{q},\mathbf{p}) =\mathbf{p}\cdot\mathbf{\dot q}(\mathbf{q},\mathbf{p}) - L(\mathbf{q},V(\mathbf{q},\mathbf{p}).
$$

* Como no caso de um grau de liberdade, temos o sistema Hamiltoniano (ou equações de Hamilton)

$$ \begin{cases}
     \displaystyle\mathbf{\dot q} = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p}), \\
     \displaystyle \mathbf{\dot p} = - \frac{\partial H}{\partial \mathbf{q}}(\mathbf{q},\mathbf{p}),
   \end{cases}
$$

* Nesse sistema,

$$
\begin{align*}
  \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p})
     & = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p}) = \left(\frac{\partial H}{\partial p_1}(\mathbf{q},\mathbf{p}),
          \ldots, \frac{\partial H}{\partial p_d}(\mathbf{q},\mathbf{p})\right), \\
   \frac{\partial H}{\partial \mathbf{q}}(\mathbf{q},\mathbf{p})
     & = \frac{\partial H}{\partial\mathbf{q}}(\mathbf{q},\mathbf{p}) = \left(\frac{\partial H}{\partial q_1}(\mathbf{q},\mathbf{p}),
          \ldots, \frac{\partial H}{\partial q_d}(\mathbf{q},\mathbf{p})\right).         
\end{align*}
$$


## Obtendo o Lagrangiano a partir do Hamiltoniano

* Dado um Lagrangiano $L(\mathbf{q},\mathbf{\dot q})$, vimos como obter o Hamiltoniano a partir da relação

$$ H(\mathbf{q},\mathbf{p}) = \mathbf{\dot q}\cdot\mathbf{p} - L(\mathbf{q},\mathbf{\dot q}), \qquad \mathbf{\dot q} = \mathbf{\dot q}(\mathbf{q},\mathbf{p}),
$$

* Nessa relação, $\mathbf{\dot q} = \mathbf{\dot q}(\mathbf{q},\mathbf{p})$ é solução de

$$\mathbf{p} = \nabla_{\mathbf{\dot q}} L(\mathbf{q},\mathbf{\dot q}).
$$

* De maneira inversa, podemos obter o Lagrangiano a partir de um Hamiltoniano $H(\mathbf{q},\mathbf{p})$ reescrevendo a relação acima na forma

$$ L(\mathbf{q},\mathbf{\dot q}) = \mathbf{\dot q}\cdot\mathbf{p} - H(\mathbf{q},\mathbf{p}), \qquad\mathbf{p}=\mathbf{P}(\mathbf{q},\mathbf{\dot q})
$$

* Nesse caso, $\mathbf{p} = \mathbf{P}(\mathbf{q},\mathbf{\dot q})$ é solução da segunda equação do sistema Hamiltoniano,

$$ \mathbf{\dot p} = - \frac{\partial H}{\partial\mathbf{q}}(\mathbf{q},\mathbf{p}).
$$


### Obtendo o Lagrangiano do Hamiltoniano no caso do pêndulo planar 

* No caso do pêndulo planar, vimos que o Hamiltoniano é

$$ H(\theta,\psi) = \frac{1}{2m\ell^2}\psi^2 - mg\ell\cos\theta.
$$ 

* A velocidade angular é dada pela primeira equação de Hamilton,

$$ \dot\theta = \frac{\partial H}{\partial \psi}(\theta,\psi)
       = \frac{1}{m\ell^2}\psi,
$$

* A sua inversa nos dá o momento angular em termos da velocidade angular:

$$ \psi = m\ell^2\dot\theta.
$$

* Substituindo essa relação na fórmula para o Lagrangiano a partir do Hamiltoniano, obtemos

$$
\begin{align*}
L(\theta,\dot\theta) & = \dot\theta\psi - H(\theta,\psi) \\
       & = m\ell^2 \dot\theta^2 
          - \left(\frac{1}{2m\ell^2}(m\ell^2\dot\theta)^2 - mg\ell\cos\theta\right) \\
       & = \frac{1}{2}m\ell^2\dot\theta^2 + mg\ell\cos\theta,
\end{align*}
$$

* Recuperamos, assim, o Lagrangiano desse sistema.


## Sistemas não-autônomos

* Mesmo no caso não-autônomo, em que o Lagrangiano depende também da variável temporal, podemos obter um sistema na forma Hamiltoniana.

* De fato, considere um Lagrangiano

$$ L(\mathbf{q},\mathbf{\dot q},t).
$$

* Temos

$$ \begin{cases}
     \displaystyle\mathbf{\dot q} = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p},t), \\
     \displaystyle \mathbf{\dot p} = - \frac{\partial H}{\partial \mathbf{q}}(\mathbf{q},\mathbf{p},t),
   \end{cases}
$$

* A diferença, agora, é que o Hamiltoniano também depende da variável temporal, sendo da forma

$$ H(\mathbf{q},\mathbf{p},t).
$$

* É fundamental notar que, nesse caso, o Hamiltoniano não é conservado, e a sua variação temporal ao longo de uma solução é dada por

$$ \frac{\mathrm{d} }{\mathrm{d} t} H(\mathbf{q}(t),\mathbf{p}(t),t) = 
    \frac{\partial H}{\partial t}(\mathbf{q}(t),\mathbf{p}(t),t).
$$

* As relações entre o Lagrangiano e o Hamiltoniano são como no caso
autônomo.


## Transformada de Legendre

* Vamos considerar o caso de apenas um grau de liberdade, para simplificar, ou seja, com 

$$ \mathbf{q}=q\in \mathbb{R}, \qquad \mathbf{\dot q} = \dot q, \qquad \mathbf{p} = p = \frac{\partial L}{\partial \dot q}(q,\dot q).
$$


### A transformada de Legendre relacionando Lagrangiano e Hamiltoniano

* Observe que, considerando $q$ como um parâmetro e esquecendo por um momento a dependência do Lagrangiano e do Hamiltoniano em $q$, a transformação entre essas funções pode ser escrita na forma

$$ H(p) = pq - L(\dot q), 
     \qquad \text{ onde } \dot q = \dot q(p)  \text{ é a inversa de } 
     p=\frac{\partial L(\dot q)}{\partial \dot q}.
$$

* Trocando a notação, podemos escrever a seguinte transformação:

$$ g^*(s) = sr - g(r), \qquad \text{ onde } r=r(s) \text{ é a inversa de }
     s=g'(r).
$$

* Essa transformação está bem definida para $s\in \mathbb{R}$ desde que $g:\mathbb{R}\rightarrow \mathbb{R}$ seja diferenciável e $g':\mathbb{R}\rightarrow \mathbb{R}$ seja invertível. 

* Veremos, a seguir, que, sob certas condições, $g^*$ pode ser escrito como

$$ g^*(s) = \max_{r\in \mathbb{R}} \left\{ sr - g(r) \right\}.
$$

* A operação acima que leva $g$ em $g*$ é chamada de **Transformada de Legendre.**

* O Hamiltoniano é, em certo sentido, a transformada de Legendre do Lagrangiano. 

* E vice-versa!


### Reescrevendo a transformada de Legendre

* Note, agora, como mencionado acima, que, formalmente, a transformação $g^*(s) = sr - g(r),$ onde $r=r(s)$ é a inversa de $s=g'(r),$ pode ser escrita como

$$ g^*(s) = \max_{r\in \mathbb{R}} \left\{ sr - g(r) \right\}.
$$

* De fato, o máximo, sob certas condições, é atingido quando 

$$ \frac{\partial}{\partial r} \left\{ sr - g(r) \right\} = s - g'(r) = 0,
$$

* Ou seja, quando $r$ é tal que $s = g'(r).$

* No caso em que esse máximo existe e é único, isso define a função $r=r(s)$ que é inversa de $g'$. 

* Por outro lado, para essa última definição fazer sentido, não é necessário nem que $g$ seja diferenciável. 

* Podemos assumir que $g$ é contínua e com crescimento superlinear, i.e.

$$ \frac{g(r)}{|r|} \rightarrow \infty, \qquad \text{quando } |r|\rightarrow \infty.
$$

* Esse crescimento implica em $sr-g(r)$ ser limitada superiormente em relação a $r,$ para todo $s\in\mathbb{R}$ fixo e, com isso, que o supremo de $sr-g(r)$ em $r$ seja limitado. E a continuidade implica que esse supremo é um máximo.

* Vejam, nos exercícios, condições para que $g^*$ seja contínua e com crescimento superlinear e, com isso, que a transformada de Legendre possa ser aplicada em $g^*,$ nos dando uma função $g^{**}.$ E, ainda, que $g^{**}$ concide com $g$. 


## Exercícios

1. Ache o Hamiltoniano e as equações de Hamilton nos seguintes casos:
    1. Corpo em queda livre, com o seguinte Lagrangiano, onde $m,g>0$:
        $$ L(h,\dot h) = \frac{1}{2}m\dot h^2 + mgh.
        $$ 
    1. Corpo deslizando em um plano inclinado, com o seguinte Lagrangiano, onde $m,g>0$, $\alpha\in \mathbb{R}$:
        $$ L(x,\dot x) = \frac{1}{2}m\dot x^2\sec^2\alpha  + mg x\tan\alpha,
        $$
    1. Sistema massa-mola, com o seguinte Lagrangiano, onde $m,k>0$:
        $$ L(x,\dot x) = \frac{1}{2} m \dot x^2 + \frac{1}{2} k x^2,
        $$   
1. Ache o Hamiltoniano no caso de um pêndulo girante, cujo Lagrangiano é
$$ L(\varphi,\dot\varphi) = \frac{1}{2}m\ell^2(\dot\varphi^2 + \omega\sin^2\varphi)
        + mg\ell\cos\varphi,
$$
onde $m,g,\ell>0$, $\omega\in \mathbb{R}$, e verifique que as equações de Hamilton desse sistema tomam a forma
$$ \begin{cases}
        \displaystyle \dot \varphi = \frac{1}{m\ell^2}\psi, \\
        \displaystyle \dot \psi = 2\omega^2\sin\varphi\cos\varphi --mg\ell\sin\varphi.
    \end{cases}
$$


## Exercícios - parte 1

1. Analogamente ao caso bidimensional, ache uma matriz antisimétrica $\mathbf{J}\in \mathbb{R}^{2d \times 2d}$ tal que um sistema Hamiltoniano em $\mathbb{R}^{2d}$ pode ser escrito na forma
$$ (\mathbf{\dot q}, \mathbf{\dot p}) = \mathbf{J} \boldsymbol{\nabla} H(\mathbf{q},\mathbf{p}),
$$
onde $\boldsymbol{\nabla} H(\mathbf{q},\mathbf{p}) = (\boldsymbol{\nabla}_\mathbf{q} H(\mathbf{q},\mathbf{p}),\boldsymbol{\nabla}_\mathbf{p} H(\mathbf{q},\mathbf{p}))$ é o gradiente de $H(\mathbf{q},\mathbf{p})$. 
1. Verifique, nesse caso de vários graus de liberdade, que as soluções da equações de Euler-Lagrange de um Lagrangiano $L(\mathbf{q},\mathbf{\dot q})$ satisfazem as equações de Hamilton
$$ \begin{cases}
        \displaystyle\mathbf{\dot q} = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p}), \\
        \displaystyle \mathbf{\dot p} = - \frac{\partial H}{\partial \mathbf{q}}(\mathbf{q},\mathbf{p}),
    \end{cases}
$$
para o Hamiltoniano $H(\mathbf{q},\mathbf{p})$ correspondente.
1. Considere o problema de três corpos planar restrito circular, em que um corpo celeste $L$ com massa $M_L>0$ gira em movimento circular com freqüência constante $\omega>0$ em torno de um outro corpo celeste $T$ de massa $M_T>0$, e um satélite de massa $m\ll M_L,M_T$ muito menor que a dos dois corpos se movimenta sob a atração gravitacional desses corpos. Considerando um referencial girante centrado em $T$ e acompanhando a rotação de $L$ em torno de $T$, o Lagrangiano para o movimento do satélite pode ser escrito na forma polar
$$ L(r,\theta,\dot r,\dot \theta) = \frac{1}{2} m \dot r^2 
    + \frac{1}{2} m r^2 (\omega+\dot\theta) 
    + G \frac{mM_T}{r} + G\frac{mM_L}{\sqrt{r^2+R^2 -2rR}}.
$$
Obtenha o Hamiltoniano desse sistema e verifique que o sistema hamiltoniano associado pode ser escrito na forma
$$ \begin{cases}
        \displaystyle \dot r = \frac{p_r}{m}, \\
        \displaystyle \dot \theta = \frac{p_\theta}{mr^2} - \omega, \\
        \displaystyle \dot p_r = \frac{p_\theta}{r} - G\frac{mM_T}{r^2} 
        - 2G(r-R)\frac{mM_L}{\sqrt{r^2+R^2 -2rR}}, \\
        \displaystyle \dot p_\theta = 0,
    \end{cases}
$$
onde $p_r$ e $p_\theta$ são os momentos conjugados às coordenadas
generalizadas $r$ e $\theta$, respectivamente.
1. Ache o Hamiltoniano e as equações de Hamilton de um problema
de dois pêndulos co-planares com a mesma massa $m>0$ e hastes de mesmo 
comprimento $\ell>0$.


## Exercícios - parte 2

1. Nos problemas das seções anteriores, faça o caminho inverso, obtendo o Lagrangiano a partir do Hamiltoniano, conforme descrito acima.


## Exercícios - parte 3

1. Mostre, nesse caso não-autônomo, que o Hamiltoniano obtido da relação
$$ H(\mathbf{q},\mathbf{p},t) = \mathbf{\dot q}\cdot\mathbf{p} - L(\mathbf{q},\mathbf{\dot q},t), \qquad \mathbf{\dot q} =\mathbf{\dot q}(\mathbf{q},\mathbf{p},t),
$$
onde $\mathbf{\dot q} = \mathbf{\dot q}(\mathbf{q},\mathbf{p},t)$ é solução de
$$\mathbf{p} = \nabla_{\mathbf{\dot q}} L(\mathbf{q},\mathbf{\dot q},t),
$$
leva as equações de Euler-Lagrange no sistema hamiltoniano
$$ \begin{cases}
        \displaystyle\mathbf{\dot q} = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p},t), \\    
        \displaystyle \mathbf{\dot p} = - \frac{\partial H}{\partial \mathbf{q}}(\mathbf{q},\mathbf{p},t), 
    \end{cases}
$$
1. Mostre que nesse caso não-autônomo o Hamiltoniano satisfaz
$$ \frac{\mathrm{d} }{\mathrm{d} t} H(\mathbf{q}(t),\mathbf{p}(t),t) = 
        \frac{\partial H}{\partial t}(\mathbf{q}(t),\mathbf{p}(t),t).
$$
1. Mostre o Lagrangiano $L(\mathbf{q},\mathbf{\dot q},t)$ associado a um Hamiltoniano 
$H(\mathbf{q},\mathbf{p},t)$ pode ser recuperado através das relações
$$ L(\mathbf{q},\mathbf{\dot q}) = \mathbf{\dot q}\cdot\mathbf{p} - H(\mathbf{q},\mathbf{p}), \qquad\mathbf{p}=\mathbf{P}(\mathbf{q},\mathbf{\dot q})
$$
onde $\mathbf{p} = \mathbf{P}(\mathbf{q},\mathbf{\dot q})$ é solução da primeira equação do sistema Hamiltoniano,
$$ \mathbf{\dot q} = \frac{\partial H}{\partial\mathbf{p}}(\mathbf{q},\mathbf{p}).
$$
1. Considere o Lagrangiano
$$ L(\theta,\dot\theta,t) = m\ell\omega\dot\theta\cos\omega t\cos\theta
    + \frac{1}{2}m\ell^2\dot\theta^2 + mg\ell\cos\theta
$$
associado a um pêndulo planar cuja haste fixa está sujeita a um movimento periódico com freqüência $\omega\in \mathbb{R}$. Obtenha o Hamiltoniano correspondente.


## Exercícios - parte 4

1. Seja $g:\mathbb{R}\rightarrow \mathbb{R}$ contínua com crescimento superlinear e considere a sua transformada de Legendre
$$ g^*(s)= \max_{r\in \mathbb{R}}\{sr - g(r)\}.
$$
  a) Mostre que $g^*:\mathbb{R}\rightarrow \mathbb{R}$ está bem definida.
  b) Mostre que $g^*$ é contínua em $\mathbb{R}$.
  c) Mostre que $g^*$ é coerciva.
  d) Mostre que se $g$ é convexa, então $g^*$ é convexa.
  e) Mostre que a segunda transformada $g^{**}$ de Legendre de $g$ está bem definida, onde
  $$ g^{**}(r) = \max_{s\in \mathbb{R}} \{rs-g^*(s)\},
  $$
  f) Mostre que se $g$ é estritamente convexa, então a segunda transformada de Legendre de $g$ coincide com a função original, ou seja, $g^{**} =g$.
  g) Suponha que $g$ seja continuamente diferenciável e com $g': \mathbb{R}\rightarrow \mathbb{R}$ invertível. Mostre que $g^*$ pode ser escrito na forma
  $$ g^*(s) = sr(s) - g(r(s)),
  $$
  para todo $s\in \mathbb{R}$, onde $r(s)$ é o único número real $r$ tal que $s=g'(r)$. De outra forma,
  $$ g^*(s) = s(g')^{-1}(s) - g((g')^{-1}(s)).
  $$
  h) Seja $g:\mathbb{R}\rightarrow \mathbb{R}$ duas vezes continuamente diferenciável e tal que a sua derivada $g':\mathbb{R}\rightarrow \mathbb{R}$ é bijetiva. Para $s\in \mathbb{R}$, considere $h:\mathbb{R}\rightarrow\mathbb{R}$ dada por
  $$ h(s) = -g(0) + \int_{g'(0)}^s (g')^{-1}(\xi)\;\mathrm{d}\xi.
  $$
  Usando a substituição de variáveis $\xi=g'(\eta)$ e integração por partes mostre que $h(s)=rs-g(r)$ onde $r$ é tal que $s=g'(r)$, i.e. $h$ é a transformada de Legendre de $g$.
