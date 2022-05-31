
@def title = "Mecânica Lagrangiana"

# {{ get_title }}

```julia
using Images
using Plots
using DifferentialEquations.OrdinaryDiffEq
```



## Fundamentos

* Na Mecânica Lagrangiana, o *princípio de menor ação*, baseado em uma *função Lagrangiana*, substitui as leis de Newton, em particular a segunda lei de Newton, que diz que a *taxa de variação de momento em relação ao tempo é igual ao resultante das forças*.

* O **Lagrangiano** é uma função dependente da variável temporal, da posição e da velocidade dos pontos materiais envolvidos no sistema: $L(\mathbf{r}, \mathbf{\dot r}, t)$.

* A **ação** do sistema ao longo de um caminho $\mathbf{r}(t)$, $t_0\leq t \leq t_1$, é dada pela integral de caminho do Lagrangiano:

$$ S(\mathbf{r}) = \int_{t_0}^{t_1} L(\mathbf{r}(t), \mathbf{\dot r}(t), t) \;\mathrm{d} t.
$$

* O **princípio da menor ação** afirma que a trajetória que um sistema percorre saindo de uma posição $\mathbf{r}(t_0) = \mathbf{r}_0$, no instante $t_0$, e indo até uma posição $\mathbf{r}(t_1) = \mathbf{r}_1$, num instante subseqüente $t_1$, é dado pelo mínimo da ação ao longo de todos os caminhos possíveis, i.e.

$$ S(\mathbf{r}) = \min_{\mathbf{\tilde r}\in \mathcal{V}} S(\mathbf{\tilde r}),
$$

onde o mínimo é tomado em relação a todos os possíveis caminhos
ligando $\mathbf{r}_0$ a $\mathbf{r}_1$, dito **conjunto admissível** ou **conjunto de caminhos admissíveis**, i.e. 

$$ \mathcal{V} = \mathcal{V}(t_0, t_1, \mathbf{r}_0, \mathbf{r}_1) = \{ \mathbf{\tilde r} = \mathbf{\tilde r}(t); \; t_0\leq t \leq t_1,
       \mathbf{\tilde r}(t_0)=\mathbf{r}_0, \;\mathbf{\tilde r}(t_1) = \mathbf{r}_1\}.
$$


## Detalhando

* Vamos detalhar cada aspecto mencionado acima.


### Mínimo da ação

* Assim como no Cálculo de Várias Variáveis, o mínimo de $S = S(\mathbf{r})$ é encontrado como ponto crítico de $S$, buscando os "pontos" em que o "gradiente" se anula.

* Exceto que, nesse caso, olhamos para a condição das "derivadas direcionais" se anularem.

* De fato, escrevendo $\mathbf{\tilde r} =\mathbf{r}+\mathbf{w}$,  consideramos o conjunto

$$ \mathcal{W}(t_0,t_1) = \{\mathbf{w}=\mathbf{w}(t); \;t_0\leq t \leq t_1, \; \mathbf{w}(t_0)=0, \;\mathbf{w}(t_1)=0\},
$$

de modo que 
$$ \mathcal{V} = \mathbf{r} + \mathcal{W},
$$

e o problema de minimização pode ser escrito como o de encontrar

$$ \mathbf{r} \in \mathcal{V} \;\textrm{ tal que }\; \mathcal{S}(\mathbf{r}) \leq \mathcal{S}(\mathbf{r} + \mathbf{w}), \;\forall \mathbf{w} \in \mathcal{W}.
$$

* Como $\varepsilon\mathbf{w}\in \mathcal{W}$, para qualquer $\mathbf{w}\in \mathcal{W}$, a condição de $\mathbf{r}$ ser mínimo nos dá, para todo $\varepsilon > 0$,

$$ \frac{\mathcal{S}(\mathbf{r}+\varepsilon\mathbf{w})-\mathcal{S}(\mathbf{r})}{\varepsilon} \geq 0
$$

* Assim, no limite, obtemos a condição
$$ \lim_{\varepsilon\rightarrow 0^+} 
      \frac{\mathcal{S}(\mathbf{r}+\varepsilon\mathbf{w})-\mathcal{S}(\mathbf{r})}{\varepsilon} \geq 0.
$$


### Derivada de Gâteaux da ação

* Nesse contexto de função $S(\mathbf{r})$ de funções $\mathbf{r}$, as derivadas direcionais ganham o nome pomposo de *derivadas de Gâteaux*.

* Para o cálculo da derivada de Gâteaux, assumindo $L(\mathbf{r}, \mathbf{\dot r}, t)$ uma função suave, temos a expansão de Taylor

$$ L(\mathbf{r} + \varepsilon \mathbf{w}, \mathbf{\dot r} + \varepsilon \mathbf{\dot w}, t) = L(\mathbf{r}, \mathbf{\dot r}, t) + \varepsilon \frac{\partial L}{\partial \mathbf{r}} (\mathbf{r}, \mathbf{\dot r}, t)\mathbf{w} + \varepsilon \frac{\partial L}{\partial \mathbf{\dot r}} (\mathbf{r}, \mathbf{\dot r}, t)\mathbf{\dot w} + \mathcal{O}(\varepsilon^2).
$$

* Os termos $\mathbf{r}$ e $\mathbf{\dot r}$ são vetores, então as derivadas parciais acima são, na verdade, vetores gradientes.

* Dividindo por $\varepsilon > 0$ e integrando, obtemos

$$ \frac{\mathcal{S}(\mathbf{r}+\varepsilon\mathbf{w})-\mathcal{S}(\mathbf{r})}{\varepsilon} = \int_{t_0}^{t_1} \left( \frac{\partial L}{\partial \mathbf{r}} (\mathbf{r}, \mathbf{\dot r}, t)\mathbf{w} + \frac{\partial L}{\partial \mathbf{\dot r}} (\mathbf{r}, \mathbf{\dot r}, t)\mathbf{\dot w} \right) \;\mathrm{d} t + \mathcal{O}(\varepsilon)
$$

* Integrando por partes o segundo termo, usando as condições $\mathbf{w}(t_0) = \mathbf{w}(t_1) = 0$ nos extremos, obtemos

$$ \frac{\mathcal{S}(\mathbf{r}+\varepsilon\mathbf{w})-\mathcal{S}(\mathbf{r})}{\varepsilon} = \int_{t_0}^{t_1} \left( \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t) 
           - \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t)\right)\mathbf{w}(t) \;\mathrm{d} t + \mathcal{O}(\varepsilon)
$$

* Tomando o limite, chegamos à expressão para a derivada de Gâteaux de $S(\cdot)$ no "ponto" $\mathbf{r}$, na direção $\mathbf{w}$, com a condição para $\mathbf{r}$ ser mínimo devendo valer para todo $\mathbf{w} \in \mathcal{W}$:

$$ \lim_{\varepsilon\rightarrow 0} 
      \frac{\mathcal{S}(\mathbf{r}+\varepsilon\mathbf{w})-\mathcal{S}(\mathbf{r})}{\varepsilon}
      = \int_{t_0}^{t_1} \left( \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t) 
           - \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t)\right)\mathbf{w}(t) \;\mathrm{d} t \geq 0.
$$

* Como $-\mathbf{w}$ também pertence a $\mathcal{W}$, isso nos dá a condição

$$
\int_{t_0}^{t_1} \left( \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t) - \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t)\right)\mathbf{w}(t) \;\mathrm{d} t = 0, \qquad \forall \mathbf{w}\in \mathcal{W}.
$$


### Equações de Euler-Lagrange

* Como a condição acima deve valer para todo $\mathbf{w}\in \mathcal{W}$, obtemos as chamadas **equações de Euler-Lagrange** para trajetória que minimiza a ação:

$$ \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t) - \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t) = 0, \qquad \forall t \in (t_0, t_1).
$$

* Essas equações são as equações de movimento do sistema, substituindo as equações de Newton.


### O Lagrangiano em mecânica clássica

* Não há uma expressão geral para o Lagrangiano.

* Em mecânica clássica, não relativística, de sistemas conservativos de $n$ corpos de massa $m_1, \ldots, m_n$, o Lagrangiano é da forma

$$ L = K - V,
$$

* Onde $K = K(\mathbf{\dot r}) = (1/2)\sum_j m_j \|\mathbf{\dot r}_j\|^2$ é a energia cinética e $V = V(\mathbf{r})$ é a energia potencial, com $\mathbf{r} = (\mathbf{r}_1, \ldots, \mathbf{r}_n)$ sendo o conjunto de posições dos centros de massa dos corpos.

* Escrevemos, mais explicitamente,

$$ L(\mathbf{r}, \mathbf{\dot r}) = K(\mathbf{\dot r}) - V(\mathbf{r}).
$$

* Temos

$$ \frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r}) = \frac{\partial K}{\partial\mathbf{\dot r}}(\mathbf{\dot r}) = \frac{1}{2}\frac{\partial}{\partial\mathbf{\dot r}}\sum_j m_j \|\mathbf{\dot r}_j\|^2 = m_j \mathbf{\dot r}_j.
$$

* De onde obtemos

$$ \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t) = m_j \mathbf{\ddot r}_j.
$$

* Além disso,

$$ \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r}) = - \frac{\partial V}{\partial\mathbf{r}}(\mathbf{r}) = \mathbf{F}(\mathbf{r}).
$$

* Assim, as equações de Euler-Lagrange nos dão as equações clássicas de um sistema conservativo com potencial $V$:

$$ m_j \mathbf{\ddot r}_j = - \frac{\partial V}{\partial \mathbf{r}_j}(\mathbf{r}).
$$


### Lagrangiano em relatividade restrita

* Em relatividade restrita, as equações de movimento de uma partícula livre são dadas por

$$ \frac{\mathrm{d}}{\mathrm{d} t} \left(\frac{m\mathbf{\dot r}}{\displaystyle\sqrt{1-\frac{\|\mathbf{\dot r}\|^2}{c^2}}} 
          \right)= 0,
$$

onde $c$ é a velocidade da luz e $m$ é a massa de repouso da partícula. 

* Essa equação pode ser deduzida através das equações de Euler-Lagrange para o Lagrangiano

$$ L(\mathbf{\dot r}) = -mc^2\sqrt{1 - \frac{\|\mathbf{\dot r}\|^2}{c^2}}.
$$


## Sistemas com vínculos

* Um dos grandes "poderes" da mecânica Lagrangiana é facilitar a dedução das equações quando há alguma espécie de restrição que limita os possíveis estados, ou configurações, do sistema.

* Por exemplo, o problema de um **corpo em queda livre** possui as restrições $x = y = 0$.

* Em um **pêndulo planar simples**, a massa do pêndulo está restrita a um movimento circular. As coordenadas $x(t), y(t), z(t)$ do seu centro de massa devem satisfazer $x = 0$, $y^2 + z^2 = \ell^2$.

* No **pêndulo tridimensional**, temos apenas uma restrição, com o movimento restrito a uma esfera,

$$ x^2 + y^2 + z^2 = \ell^2.
$$

* No problema de uma **bola quicante**, estando o "piso" no plano $xy$, a restrição é da forma $z \geq 0$.

* Em uma **mola vertical**, o extremo "livre" está em uma posição $\mathbf{r} = (x, y, z)$ com $x = y = 0$.

* No caso de um **pêndulo planar com extremidade variável**, onde a extremidade fixa passa a se mover de forma determinada $(x, y) = (f(t), g(t))$ ao longo do plano $xy$, temos as restrições

$$ x = f(t), \quad (y - g(t))^2 + z^2 = \ell^2.
$$

* Um exemplo fundamental é o de um **pêndulo girante** (veja relação com o [*governador centrífugo*](https://en.wikipedia.org/wiki/Centrifugal_governor)), que consiste em um pêndulo tridimensional mas girando com uma velocidade angular determinada $\omega$, em torno do eixo $z$. Nesse caso, denotando por $\theta = \theta(x,y)$ o ângulo entre o vetor $(1, 0)$ e o vetor $(x,y)$, no sentido trigonométrico, temos as restrições

$$ x^2 + y^2 + z^2 = \ell^2, \quad \dot\theta = \omega.
$$

* Mais um exemplo interessante é o de um **movimento planar sobre um relevo**. Nesse caso, assumimos que o movimento se dá no plano $yz$, com $z = h(y)$, ou seja, ao longo de um relevo dado pelo gráfico de $h$. Podemos escrever essas restrições na forma

$$ x = 0, \quad z = h(y).
$$



### Vínculos holônomos


* Vamos nos concentrar no caso de **vínculos holônomos**, que são os vínculos "integráveis", que não dependem do movimento em si, apenas das posições, podendo ser escritos como (uma ou mais) equações envolvendo apenas a posição e o tempo:

$$ \Phi_k(\mathbf{r}, t) = 0, \qquad k = 1, \ldots, n_r.
$$

* Há, no entanto, uma série de [vínculos não-holonômos](https://en.wikipedia.org/wiki/Nonholonomic_system) importantes.

* No caso do *pêndulo planar,* temos os vínculos holônomos

$$ \Phi_1(x, y, z) = x, \quad \Phi_2(x, y, z) = y^2 + z^2 - \ell^2.
$$

* No caso do *pêndulo tridimensional,* temos o único vínculo

$$ \Phi_1(x, y, z) = x^2 + y^2 + z^2 - \ell^2.
$$

* No caso do *pêndulo planar com extremo forçado,* temos os vínculos holônomos

$$ \Phi_1(x, y, z, t) = x - f(t), \quad \Phi_2(x, y, z) = y^2 + z^2 - \ell^2.
$$

* Mesmo no caso do *pêndulo girante,* a condição $\dot\theta = \omega$ pode ser integrada, nos levando aos vínculos holônomos

$$ \Phi_1(x, y, z) = x^2 + y^2 + z^2 - \ell^2, \qquad \Phi_2(x, y, z, t) = \theta(x, y) - \omega t.
$$

* No do *movimento planar sobre um relevo,* temos os vínculos

$$ \Phi_1(x, y, z) = x, \qquad \Phi_2(x, y, z) = z - h(y).
$$


### Princípio da menor ação com vínculos holônomos

* Impondo o vínculo, temos uma restrição no espaço de caminho admissíveis,

$$ \mathcal{V}_\Phi(t_0,t_1) = \{\mathbf{r}=\mathbf{r}(t); \;t_0\leq t \leq t_1, \; \mathbf{r}(t_0)=\mathbf{r}_0, \;\mathbf{r}(t_1)=\mathbf{r}_1, \;\Phi_k(\mathbf{r}, t) = 0, \;k = 1, \ldots, n_r\},
$$

* Com isso, o problema de minimização pode ser escrito como o de encontrar

$$ \mathbf{r} \in \mathcal{V}_\Phi \;\textrm{ tal que }\; \mathcal{S}(\mathbf{r}) \leq \mathcal{S}(\mathbf{\tilde r}), \;\forall \mathbf{\tilde r} \in \mathcal{V}_\Phi.
$$


### Coordenadas generalizadas

* Em muitos casos, os vínculos holônomos $\Phi_k(\mathbf{r}, t) = 0$ podem ser satisfeitos de maneira explícita, $\mathbf{r} = \mathbf{r}(\mathbf{q}, t)$, através de **coordenadas generalizadas** $\mathbf{q}$.

* Por exemplo, no *corpo em queda livre*, temos a coordenada generalizada $h$, com

$$ \mathbf{r} = (0, 0, h).
$$

* Na *mola vertical*, temos a coordenada generalizada $u$, com

$$ \mathbf{r} = (0, 0, -u).
$$

* No *pêndulo planar simples*, temos a coordenada generalizada $\theta$, com

$$ \mathbf{r} = (0, \ell\sin\theta, - \ell\cos\theta).
$$

* No *pêndulo tridimensional*, temos duas coordenada generalizadas, $\theta$ e $\varphi$, com

$$ \mathbf{r} = (\ell\sin\varphi\cos(\theta),\ell\sin\varphi\sin(\theta),-\ell\cos\varphi).
$$

* No *pêndulo forçado*, temos a coordenada generalizada $\theta$, com

$$ \mathbf{r} = (f(t), g(t) + \ell\sin\theta, - \ell\cos\theta).
$$

* No *pêndulo girante*, temos a coordenada generalizada $\varphi$, com

$$ \mathbf{r} = (\ell\sin\varphi\cos(\omega t),\ell\sin\varphi\sin(\omega t),-\ell\cos\varphi).
$$


### Princípio da menor ação em coordenadas generalizadas

* No caso de vínculos $\Phi_k(\mathbf{r}, t) = 0$, $k = 1, \ldots, n_r$, plenamento  satisfeitos por coordenadas generalizadas $\mathbf{r} = \mathbf{r}(\mathbf{q}, t)$, para $\mathbf{q} \in \mathbb{R}^d$ (ou em uma variedade $d$-dimensional sem bordo), temos $\mathbf{q}_0$ e $\mathbf{q}_1$ tais que

$$ \mathbf{r}_0 = \mathbf{r}(\mathbf{q}_0, t_0), \quad \mathbf{r}_1 = \mathbf{r}(\mathbf{q}_1, t_1).
$$

* Com isso, podemos escrever

$$ \mathcal{V}_\Phi = \left\{\mathbf{r} = \mathbf{r}(\mathbf{q}(t), t), \;t_0\leq t\leq t_1, \;\mathbf{q}(t_0) = \mathbf{q}_0, \;\mathbf{q}(t_1) = \mathbf{q}_1\right\}.
$$

* Defina o operador $\mathbf{R}$ que leva caminhos $\mathbf{q}$ em caminhos $\mathbf{r} = \mathbf{R}(\mathbf{q})$ dados por

$$ \mathbf{r}(t) = \mathbf{R}(\mathbf{q})(t) = \mathbf{r}(\mathbf{q}(t), t), \quad t_0 \leq t \leq t_1.
$$

* Assim, podemos escrever que $\mathcal{V}_\Phi$ é a imagem de um conjunto de caminhos $\mathcal{Q}$ por $\mathbf{R}$:

$$ \mathcal{V}_\Phi = \mathcal{R}(\mathcal{Q}), \quad \mathcal{Q} = \left\{\mathbf{q} = \mathbf{q}(t), \;t_0\leq t\leq t_1, \;\mathbf{q}(t_0) = \mathbf{q}_0, \;\mathbf{q}(t_1) = \mathbf{q}_1\right\}.
$$

* O princípio de menor ação restringindo os possíveis caminhos a esses vínculos toma a forma: encontrar

$$ \mathbf{q} \in \mathcal{Q} \;\textrm{ tal que }\; \mathcal{S}(\mathbf{R}(\mathbf{q})) \leq \mathcal{S}(\mathbf{R}(\mathbf{\tilde q})), \;\forall \mathbf{\tilde q} \in \mathcal{Q}.
$$


### Equações de Euler-Lagrange em coordenadas generalizadas

* Nas coordenadas generalizadas, temos

$$ \mathbf{r} = \mathbf{r}(\mathbf{q}, t), \qquad \mathbf{\dot r} = \frac{\partial \mathbf{r}}{\partial \mathbf{q}}(\mathbf{q}, t)\mathbf{\dot q} + \frac{\partial \mathbf{r}}{\partial t}(\mathbf{q}, t).
$$


* Assim, reescrevemos o Lagrangiano como

$$ L_\Phi(\mathbf{q}, \mathbf{\dot q}, t) = L(\mathbf{r}(\mathbf{q}, t), \frac{\partial \mathbf{r}}{\partial \mathbf{q}}(\mathbf{q}, t)\mathbf{\dot q} + \frac{\partial \mathbf{r}}{\partial t}(\mathbf{q}, t),  t).
$$

* A ação toma a forma

$$ S(\mathbf{r}) = \int_{t_0}^{t_1} L(\mathbf{r}(t), \mathbf{\dot r}(t), t) \;\mathrm{d} t = \int_{t_0}^{t_1} L(\mathbf{r}(\mathbf{q}, t), \frac{\partial \mathbf{r}}{\partial \mathbf{q}}(\mathbf{q}, t)\mathbf{\dot q} + \frac{\partial \mathbf{r}}{\partial t}(\mathbf{q}, t),  t) \;\mathrm{d} t = \int_{t_0}^{t_1} L_\Phi(\mathbf{q}, \mathbf{\dot q}, t) \;\mathrm{d} t.
$$

* Como antes, pelo princípio da menor ação, a trajetória é dada pelas equações de Euler-Lagrange, só que dessa vez associadas ao Lagrangiano $L_\Phi$:

$$ \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L_\Phi}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) - \frac{\partial L_\Phi}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t) = 0, \qquad \forall t \in (t_0, t_1).
$$


### Exemplos de modelagem com vínculos

#### Corpo em queda livre

* No caso de um corpo de massa $m$ em queda livre, com altura $h = h(t)$, temos que a altura faz o papel da única coordenada generalizada e a restrição da queda ser vertical se escreve

$$ \mathbf{r} = (0, 0, h).
$$

* Nesse caso, a energia cinética e o potencial são dadas por

$$ K(\mathbf{r}) = \frac{1}{2} m {\dot h}^2, \qquad V(\mathbf{r}) = mgh.
$$

* O Lagrangiano com vínculo simplifica para (omitindo o subescrito $\Phi$)

$$ L = L(h, \dot h) = \frac{1}{2} m {\dot h}^2 - mgh.
$$

* Para as equações de Euler-Lagrange, temos

$$ \frac{\partial L}{\partial h}(h, \dot h) = -mg, \qquad \frac{\partial L}{\partial \dot h}(h, \dot h) = m \dot h.
$$

* Assim,

$$ \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot h}(h, \dot h) - \frac{\partial L}{\partial h}(h, \dot h) = \frac{\mathrm{d}}{\mathrm{d} t} (m \dot h) + mg = m \ddot h + mg = 0.
$$

* Portanto, recuperamos as equações obtidas pela formulação Newtoniana:

$$ m\ddot h = -mg.
$$


#### Pêndulo planar simples

* No caso do pêndulo, temos a coordenada generalizada $\theta$, com

$$ \mathbf{r} = (0, \ell\sin\theta, - \ell\cos\theta).
$$

* As energia cinética e potencial se escrevem

$$ K = K(\dot\theta) = \frac{1}{2}m\ell^2{\dot \theta}^2, \qquad V(\theta) = -mg\ell\cos\theta.
$$

* O Lagrangiano toma a forma

$$ L(\theta, \dot \theta) = \frac{1}{2}m\ell^2{\dot \theta}^2 + mg\ell\cos\theta
$$

* Com isso, obtemos as equações de Euler-Lagrange

$$ m\ell\ddot \theta = - mg\cos\theta.
$$


#### Movimento planar em um relevo

* Nesse caso, consideramos a coordenada generalizada $y\in \mathbb{R}$ e escrevemos

$$ \mathbf{r}(y, t) = (0, y, h(y)).
$$

* Temos

$$ \mathbf{\dot r} = (0, \dot y, h'(y)\dot y).
$$

* As energias cinética e potencial tomam a seguinte forma (observe, agora, a dependência em $\mathbf{\dot r}$, ou seja, em $\dot y$, da energia cinética)

$$ K = K(y, \dot y) = \frac{1}{2} m \left( 1 + h'(y)^2 \right){\dot y}^2, \qquad V(y) = mgh(y).
$$

* O Lagrangiano em coordenadas generalizadas toma a forma

$$ L(y, \dot y) =  \frac{1}{2} m \left( 1 + h'(y)^2 \right){\dot y}^2 - mgh(y).
$$

* Temos

$$ \frac{\partial L}{\partial y}(y, \dot y) = m h'(y) h''(y) {\dot y}^2 - mgh'(y), \qquad \frac{\partial L}{\partial \dot y}(y, \dot y) = m \left( 1 + h'(y)^2 \right) \dot y.
$$

* Temos, ainda,

$$ \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot y}(y, \dot y) = \frac{\mathrm{d}}{\mathrm{d} t} \left( m \left( 1 + h'(y)^2 \right) \dot y \right) = 2m h'(y) h''(y) {\dot y}^2 + m \left( 1 + h'(y)^2 \right) \ddot y.
$$

* Assim, 

$$ \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial \dot y}(y, \dot y) - \frac{\partial L}{\partial y}(y, \dot y) = 2m h'(y) h''(y) {\dot y}^2 + m \left( 1 + h'(y)^2 \right) \ddot y - m h'(y) h''(y) {\dot y}^2 + mgh'(y) = 0.
$$

* Isso nos dá a equação de movimento

$$ m h'(y) h''(y) {\dot y}^2 + m \left( 1 + h'(y)^2 \right) \ddot y = - mgh'(y).
$$


## Vínculos holônomos implícitos (WIP)



## Exercícios

1. O **Lema Fundamental do Cálculo das Variações** diz que se uma função contínua $f:[t_0,t_1]\rightarrow \mathbb{R}$ é tal que
$$ \int_{t_0}^{t_1} g(t)w(t) \;\mathrm{d} t = 0,
$$
para toda função $w:[t_0,t_1]\rightarrow \mathbb{R}$ contínua com $w(t_0)=w(t_1)=0$, então $f(t)=0$ para todo $t\in [t_0,t_1]$. Mostre esse resultado.

1. Verifique que as equações de Euler-Lagrange associadas ao Lagrangiano 
$$ L(\mathbf{r}, \mathbf{\dot r}) = \frac{1}{2}\sum_{j=1}^n m_j \|\mathbf{r}_j\|^2 - V(\mathbf{r})
$$
são
$$ m_j \mathbf{\ddot r}_j = - \frac{\partial V}{\partial \mathbf{r}_j}(\mathbf{r}).
$$

1. Um referencial é dito inercial quando o tempo é homogêneo e o espaço é homogêneo e isotrópico, ou seja as suas propriedades métricas não dependem da posição no espaço (homogeneidade espacial), do instante de tempo (homogeneidade temporal) e da direção no espaço (isotropia). No caso de uma sistema mecânico de uma única partícula livre, isso se traduz na condição do Lagrangiano $L(\mathbf{r}, \mathbf{\dot r}, t)$, $\mathbf{r}\in\mathbb{R}^3$, ser invariante por translações no tempo e no espaço (homogeneidades espacial e temporal) e invariante por rotações no espaço (isotropia). Matematicamente, isso é expresso pelas condições
$$
    \begin{align*}
      L(\mathbf{r}+\mathbf{r}_0,\mathbf{\dot r},t) = L(\mathbf{r},\mathbf{\dot r},t),    \\
      L(\mathbf{r},\mathbf{\dot r},t+s) = L(\mathbf{r},\mathbf{\dot r},t), \\
      L(Q\mathbf{r},Q\mathbf{\dot r},t) = L(\mathbf{r},\mathbf{\dot r},t),
    \end{align*}
$$
para quaisquer $\mathbf{r}_0\in \mathbb{R}^3$, $s\in \mathbb{R}$, $Q\in O(3)$, onde $\mathbf{r}_0$  representa uma translação qualquer no espaço, $s$ uma translação qualquer no tempo, e $Q$ é uma matriz ortogonal qualquer representando uma rotação e/ou uma reflexão arbitrária. 
   Deduza que um Lagrangiano $L(\mathbf{r},\mathbf{\dot r},t)$ de uma única partícula,
    $\mathbf{r}\in\mathbb{R}^3$, em um referencial inercial é necessariamente da forma
    $$ L(\mathbf{r},\mathbf{\dot r},t) = f(\|\mathbf{\dot r}\|^2),
    $$
    para alguma função real $f$. 
    
1. Escreva as equações de movimento do pêndulo forçado.

1. Escreva as equações de movimento do pêndulo espacial.

1. Escreva as equações de movimento do pêndulo girante.

1. Considere uma partícula de massa $m$ se movendo, sem atrito, sobre uma superfície $z=h(x,y)$ e sob a ação gravitacional ao longo do eixo $z$ e contrária ao sentido de crescimento de $z$. Tomando $x$ e $y$ como coordenadas generalizadas, escreva o Lagragiano $L(x,y,\dot x,\dot y)$ e as equações de Euler-Lagrange correspondentes.
