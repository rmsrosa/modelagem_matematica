
@def title = "Leis de conservação em um contexto Lagrangiano"

# {{ get_title }}

* Vamos considerar as leis de conservação a partir do Lagrangiano.

* Isso tem vantagens e desvantagens. Uma desvantagem é que nesse caso estamos restritos a problemas com forças conservativas. A grande vantagem é o tratamento facilitado de problemas com vínculos.

* Vamos considerar sistemas sem vínculos, em coordenadas espaciais $\mathbf{r} =(\mathbf{r}_1,\ldots,\mathbf{r}_n)$ de $n$ partículas, com Lagrangiano

$$ L(\mathbf{r},\mathbf{\dot r},t).
$$

* E vamos considerar sistemas com vínculos, em coordenadas generalizadas $\mathbf{q}=(q_1,\ldots,q_d)$, com Lagrangiano na forma

$$ L(\mathbf{q},\mathbf{\dot q},t).
$$


## Momento linear

* No caso sem vínculos, temos as equações de Euler-Lagrange

$$ \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t) 
      - \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t) = 0.
$$

* No caso clássico em que $L = K - V$, o termo a seguir coincide com o momento no sentido clássico:

$$ \mathbf{p} =\frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r},t).
$$

* E a equação de movimento pode ser escrita como

$$ \mathbf{\dot p} =  \frac{\partial L}{\partial\mathbf{r}}(\mathbf{r},\mathbf{\dot r},t).
$$ 

* Note que esta é uma equação no espaço $\mathbb{R}^{3n}$, onde "mora" $\mathbf{p}=(\mathbf{p}_1,\ldots,\mathbf{p}_n)$.

* Isso pode ser escrito na forma de $n$ equações em $\mathbb{R}^3$, uma para cada partícula:

$$ \mathbf{\dot p}_i = \frac{\partial L}{\partial\mathbf{r}_i}(\mathbf{r},\mathbf{\dot r},t).
$$


### Momento linear total

* O momento linear total do sistema é o somatório dos momentos lineares individuais e é um elemento de $\mathbb{R}^3$:

$$ \mathbf{P} = \sum_{i=1}^n \mathbf{p}_i,
$$

* A equação de evolução do momento total pode ser escrita como

$$ \mathbf{\dot P} = \sum_{i=1}^n \frac{\partial L}{\partial\mathbf{r}_i}(\mathbf{r},\mathbf{\dot r},t).
$$


### Caracterização da conservação do momento linear

* Para a conservação de momento linear total, $\mathbf{P}$ deve ser constante em $\mathbb{R}^3$ ao longo do tempo.

* Isso quer dizer que cada coordenada dele deve ser constante.

* Isso pode ser escrito através da relação

$$ \mathbf{P}(t)\cdot \mathbf{e}_k = \text{ constante,}
$$

para cada $k=1,2,3$, onde $\mathbf{e}_1=(1,0,0)$, $\mathbf{e}_2=(0,1,0)$ e
$\mathbf{e}_3=(0,0,1)$ formam a base canônica de $\mathbb{R}^3$.

* Mais geralmente, podemos escrever a conservação de momento linear na forma

$$ \mathbf{P}(t)\cdot\mathbf{h} = \text{ constante,}
$$

para qualquer vetor $\mathbf{h}\in \mathbb{R}^3$ fixo.


### Simetria por translação e conservação do momento linear

* Para que $\mathbf{P}(t)\cdot\mathbf{h}$ seja constante, devemos ter $\mathbf{\dot P}(t)\cdot \mathbf{h} = 0$, ou seja

$$ \sum_{i=1}^n \frac{\partial L}{\partial\mathbf{r}_i}(\mathbf{r},\mathbf{\dot r}, t)\cdot \mathbf{h} = 0.
$$

* Observe que isso pode ser escrito na forma

$$ \left. \frac{\mathrm{d} }{\mathrm{d} s} L(\mathbf{r}+s\mathbf{h}^n,\mathbf{\dot r},t)\right|_{s=0} = 0,
$$

onde $\mathbf{h}^n = (\mathbf{h},\ldots, \mathbf{h})\in \mathbb{R}^{3n}$.

* Em outras palavras, a derivada direcional de $L(\mathbf{r},\mathbf{\dot r},t)$ na direção $(\mathbf{h}^n,0,0)$ em $(\mathbf{r},\mathbf{\dot r},t)$ deve ser nula.

* Isso acontece quando o Lagrangiano $L(\mathbf{r}+s\mathbf{h}^n,\mathbf{\dot r},t)$ é constante em $s$, ou seja, é constante quando fazemos uma translação de cada 
$\mathbf{r}_i$ na direção $\mathbf{h}$, na forma $\mathbf{r}\mapsto \mathbf{r}+s\mathbf{h}^n$ (i.e. uma translação uniforme de cada coordenada $\mathbf{r}_i$).

* Conclusão: se o Lagrangiano for invariante por translações de $\mathbf{r}_i$ em qualquer direção, então o momento linear total é conservado.

* Pode acontecer do Lagrangiano ser invariante por translações em apenas algumas direções, como no caso de um corpo em queda livre, tomando $z$ como a direção perpendicular à superfície da Terra, de tal modo que o Lagrangiano é invariante por translações em $x$ e $y$, mas não em $z$


### Conservação do momento linear no caso com vínculos

* No caso de um Lagrangiano de um sistema com vínculos, escrito em coordenadas generalizadas 

$$ L(\mathbf{q},\mathbf{\dot q},t),
$$

pode também acontecer de ele ser invariante por translações em apenas algumas das coordenadas generalizadas, ou seja, apenas na direção de um certo vetor $\mathbf{h}\in \mathbb{R}^d$, $\mathbf{q}\mapsto\mathbf{q}+s\mathbf{h}$.

* Nesse caso, o *momento generalizado* associado a essas direções é conservado:

$$ \mathbf{p}\cdot\mathbf{h} = \text{ constante,}
$$

onde

$$  \mathbf{p} = \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t). 
$$


## Grupos de simetria no espaço

* A translação acima, que levou à lei de conservação de momento linear, é um exemplo de grupo de transformações.

* Um **grupo de transformações** é uma família de transformações parametrizada por um parâmetro pertencente a um grupo no sentido algébrico. Para explicar melhor isso, vamos relembrar o que é um grupo algébrico.

* Um conjunto $\mathcal{G}$ é um *grupo* quando está munido de uma operação $\oplus:\mathcal{G}\times \mathcal{G} \rightarrow \mathcal{G}$ com as propriedades de

  1. **associatividade:** $(g_1\oplus g_2)\oplus g_3 = g_1\oplus (g_2\oplus g_3)$, para quaisquer $g_1,g_2,g_3\in \mathcal{G}$;
  
  1.  **existência de um elemento neutro:** existe $e$ tal que $g\oplus e = e\oplus g = g$ para todo $g\in \mathcal{G}$;
  
  1. **existência de elementos inversos:** para cada $g\in \mathcal{G}$ existe um elemento inverso $\tilde g$ tal que $\tilde g \oplus g = g \oplus \tilde g = 0$.

* Esse grupo é chamado **comutativo,** ou **abeliano,** quando possui, ainda, a propriedade de

  4. **comutatividade:** Para quaisquer $g_1,g_2\in \mathcal{G}$, vale $g_1\oplus g_2 = g_2\oplus g_1$.

* É comum explicitarmos a operação na definição de grupo escrevendo-o na forma $(\mathcal{G},\oplus)$.

* Um exemplo de grupo comutativo é o de $\mathbb{R}$ munido da operação de adição.

* Outro é o de reais não nulos munidos da operação de multiplicação.


### Grupos de transformações

* Vamos nos restringir a grupos comutativos.

* Um **grupo (comutativo) de transformações** em um conjunto $X$ é uma família $\{G_g\}_{g\in \mathcal{G}}$ de transformações $G_g: X \rightarrow X$ em $X$, parametrizada por um parâmetro $g$ pertencente a algum grupo comutativo $\mathcal{G}$ e satisfazendo as seguintes propriedades:

  1. $G_e=$ identidade em $X$, onde $e$ é o elemento identidade de $\mathcal{G}$;
  
  2. $G_{g_1\oplus g_2} = G_{g_1}\circ G_{g_2}$, para quaisquer $g_1,g_2\in \mathcal{G}$.

* O nosso interesse é partícularmente no caso $(\mathcal{G},\oplus)=(\mathbb{R},+)$, em que o grupo é simplesmente o conjunto dos números reais munido da operação de adição. 

* A translação das coordenadas generalizadas $\mathbf{q}\in\mathbb{R}^d$ na direção de um vetor dado $\mathbf{h}\in \mathbb{R}^d$ pode ser colocada nesse contexto de grupo de transformações definindo

$$ G_s(\mathbf{q}) = \mathbf{q}+s\mathbf{h}, \qquad \forall s\in \mathbb{R}.
$$

* No caso geral, denotando $\mathbf{q}_s = G_s(\mathbf{q})$, uma trajetória $\mathbf{q}(t)$ é transformada, para cada $s\in \mathcal{G}$, em uma trajetória $\mathbf{q}_s(t) = G_s(\mathbf{q}(t))$, cujo vetor velocidade é dado por

$$ \mathbf{\dot q}_s = \frac{\mathrm{d}}{\mathrm{d} t} G_s(\mathbf{q}(t)) = D_\mathbf{q} G_s(\mathbf{q}(t))\mathbf{\dot q}(t).
$$

* Nesse caso, $D_\mathbf{q} G_s(\mathbf{q})$ é o operador diferencial da transformação $\mathbf{q}\mapsto G_s(\mathbf{q})$. 

* No caso partícular da translação, em que $G_s(\mathbf{q})=\mathbf{h}+s\mathbf{h}$, temos que o vetor $s\mathbf{h}$ é constante em relação ao tempo, para cada $s\in\mathbb{R}$. Portanto,

$$ \mathbf{\dot q}_s = \mathbf{\dot q}.
$$

* De outra maneira, temos, no caso da translação, que $D_\mathbf{q} G_s(\mathbf{q})$ é o operador identidade, logo 

$$ \mathbf{\dot q}_s = D_\mathbf{q} G_s(\mathbf{q}(t))\mathbf{\dot q} = \mathbf{\dot q}.
$$


### Simetrias do Lagrangiano

* Vários sistemas físicos têm certas propriedades de simetria que podem ser identificadas através de simetrias do Lagrangiano, no sentido do Lagrangiano ser invariante por certos grupos de transformação. 

* Podemos pensar nessa terminologia de simetria fazendo uma analogia com a simetria naturalmente associada a objetos invariantes por reflexão em relação a um plano, por exemplo, que pode ser considerado como um grupo de transformações formado por apenas dois elementos, $\mathcal{G}=\{1,-1\}$, munido da operação de multiplicação, com $G_1=$ identidade; $G_{-1}=$ reflexão em relação ao plano em questão.

* O conjunto de pontos no espaço que forma um objeto com essa simetria é invariante por aplicações das transformações $G_1$ e $G_{-1}$ nesse grupo.

* No caso em que o Lagrangiano é invariante por translações, temos a transformação das variáveis generalizadas

$$(\mathbf{q},\mathbf{\dot q},t) \mapsto (\mathbf{q}_s,\mathbf{\dot q}_s,t)=(\mathbf{q}+s\mathbf{h},\mathbf{\dot q},t).
$$

* A condição do Lagrangiano ser invariante por translações significa que ele não se altera sob essas transformações:

$$ L(\mathbf{q}+s\mathbf{h},\mathbf{\dot q},t) = L(\mathbf{q},\mathbf{\dot q},t), \qquad \forall s\in \mathbb{R}.
$$

* Isso pode ser escrito na forma de invariância pelo grupo de transformações $\{G_s\}_{s\in \mathbb{R}}$ dado por $\mathbf{q}_s=G_s(\mathbf{q})$ e $\mathbf{\dot q}_s=\mathrm{d} G_s(\mathbf{q})/\mathrm{d} t$.

* Nesse caso,

$$ L(\mathbf{q}_s,\mathbf{\dot q}_s,t) = L(\mathbf{q},\mathbf{\dot q},t) = 
    \text{ constante em } s\in \mathbb{R}.
$$

* Mais geralmente, quando um Lagrangiano $L(\mathbf{q},\mathbf{\dot q},t)$ **é invariante por um grupo de transformações** $\{G_s\}_{s\in \mathbb{R}}$ nas coordenadas $\mathbf{q}$ quando satisfaz

$$ L(\mathbf{q}_s,\mathbf{\dot q}_s,t), \qquad \forall s\in \mathbb{R}.
$$


### O efeito da simetria no Lagrangiano

* Com a simetria, temos, então,

$$ L(\mathbf{q}_s,\mathbf{\dot q}_s,t) = \textrm{constante}, \quad s\in \mathbb{R}.
$$

* Nesse caso em que o grupo $\{G_s\}_{s\in \mathbb{R}}$ é contínuo, obtemos que

$$ \frac{\mathrm{d}}{\mathrm{d} s}  L(\mathbf{q}_s,\mathbf{\dot q}_s,t) = 0, \qquad \text{ em } s=0.
$$

* Essa derivada em relação ao parâmetro $s$ é nula para todo $s$, mas nos interessa, no final, apenas o caso em que $s = 0$. E isso nos dará uma lei de conservação.


## O Teorema de Noether: simetrias e leis de conservação

* O Teorema de Emmy Noether afirma que qualquer simetria diferenciável da ação de um sistema físico conservativo está associada a uma lei de conservação.

* Mais precisamente, lembre-se que, sob uma simetria diferenciável como representada pela transformação $\{G_s\}_{s\in \mathbb{R}}$, temos

$$ \frac{\mathrm{d}}{\mathrm{d} s} L(G_s(\mathbf{q}),\frac{\mathrm{d}}{\mathrm{d} t}G_s(\mathbf{q}), t) = 0.
$$

* Efetuando essa derivação, usando a regra da cadeia, e, em seguida, tomando $s=0$, obtemos

$$ \frac{\partial L}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t)\cdot \left. \frac{\mathrm{d}}{\mathrm{d} s} 
    G_s(\mathbf{q})\right|_{s=0} 
     +\frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t)
            \cdot \left.\frac{\mathrm{d}}{\mathrm{d} s} \frac{\mathrm{d}}{\mathrm{d} t}G_s(\mathbf{q})\right|_{s=0} = 0.
$$

* Observe que

$$ \frac{\mathrm{d}}{\mathrm{d} s} \frac{\mathrm{d}}{\mathrm{d} t}G_s(\mathbf{q})
     = \frac{\mathrm{d}}{\mathrm{d} t} \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})
$$

* Pelas equações de Euler-Lagrange,

$$ \frac{\partial L}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t) 
     = \frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t),
$$

* Assim, obtemos

$$  \left(\frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t)\right)
          \cdot \left. \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0} 
        + \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) 
          \cdot \left(\left.\frac{\mathrm{d}}{\mathrm{d} t} \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0} \right)= 0.
$$

* Observe agora que essa expressão é uma derivada de um produto escalar, derivada esta que é, então, nula:

$$ \frac{\mathrm{d}}{\mathrm{d} t} \left(\frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) 
        \cdot \left. \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0} \right) = 0.
$$

* Portanto, esse produto escalar é constante,

$$ \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) 
        \cdot \left. \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0} = \text{ constante em $t$.}
$$ 

* Denote

$$ \mathbf{a}(\mathbf{q}) = \left. \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0}.
$$

* Vemos que 

$$ J(\mathbf{q},\mathbf{\dot q}, t) = \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) \cdot \mathbf{a}(\mathbf{q})
     = \text{ constante em } t.
$$

* Lembrando a definição do momento generalizado $\mathbf{p}$, vemos que a quantidade conservada pode ser escrita como

$$ J(\mathbf{q},\mathbf{\dot q},t) = \mathbf{p}\cdot \mathbf{a}(\mathbf{q}), \qquad \mathbf{p}= \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q}, t).
$$

* No caso de um sistema autônomo, em que $L=L(\mathbf{q},\mathbf{\dot q})$ não depende explicitamente de $t$, temos a quantidade conservada escrita como 

$$ J(\mathbf{q},\mathbf{\dot q}) =  \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q}) \cdot \mathbf{a}(\mathbf{q})
     = \mathbf{p}\cdot \mathbf{a}(\mathbf{q}) = \text{ constante em } t.
$$ 


## Revisitando o momento linear

* A simetria para a conservação de momento linear está associada aos grupos de translação, por exemplo,

$$ G_s(\mathbf{q}) = \mathbf{q}+s\mathbf{h}, \qquad \forall s\in \mathbb{R}.
$$

* Nesse caso,

$$ \mathbf{a}(\mathbf{q}) = \left. \frac{\mathrm{d}}{\mathrm{d} s} G_s(\mathbf{q})\right|_{s=0} = \left. \frac{\mathrm{d}}{\mathrm{d} s} ( \mathbf{q}+s\mathbf{h} ) \right|_{s=0} = \mathbf{h}.
$$

* Assim, a quantidade conservada é 

$$ J(\mathbf{q},\mathbf{\dot q}) = \mathbf{p}\cdot \mathbf{a}(\mathbf{q}) = \mathbf{p}\cdot \mathbf{h}.
$$

* No corpo em queda livre, as únicas translações sobre as quais o Langrangiano é invariante são as translações horizontais, ao longo dos eixos $\mathbf{x}$ e $\mathbf{y}$. Nesse caso, podemos tomar $\mathbf{h} = \mathbf{e}_1$ e $\mathbf{h} = \mathbf{e}_2$.

* Mas, digamos, no espaço, desprezando a gravidade, então $\mathbf{h}$ é arbitrário, o que significa que o próprio momento $\mathbf{p}$ é conservado.

* Isso pode ser tratado de uma única vez com o grupo de translações $\{ G_{\mathbf{h}} \}_{\mathbf{h}\in \mathbb{R}^3}$ dado por $G_{\mathbf{h}}(\mathbf{q}) = \mathbf{q}+\mathbf{h}$.


## Momento angular

* Para a análise do momento angular, consideramos grupos de transformações associadas a rotações no espaço.

* O grupo de rotações arbitrárias no espaço não é comutativo, mas podemos nos restringir a um certo subgrupo de rotações formado por rotações em torno de um eixo fixo.

* Mais precisamente, dado um vetor unitário $\boldsymbol{\omega}\in \mathbb{R}^3$, consideramos o conjunto de rotações de um ângulo $\theta\in \mathbb{R}$ em torno do eixo gerado por $\boldsymbol{\omega}$ e no sentido da "regra da mão direita", com o polegar apontado no sentido de $\boldsymbol{\omega}$.

* Denotemos essa rotação por $R_{\boldsymbol{\omega}}(\theta)$.

* Podemos escrever essa rotação explicitamente na forma
$$
R_{\boldsymbol{\omega}}(\theta)\mathbf{r} = (\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega} 
       + (\cos\theta) (\mathbf{r}-(\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega})
       + (\sin\theta) \boldsymbol{\omega}\times\mathbf{r}, \qquad \forall \mathbf{r}\in \mathbb{R}^3.
$$

* Temos, assim, o grupo de transformações $\{R_{\boldsymbol{\omega}}(\theta)\}_{\theta\in \mathbb{R}}$ em $\mathbb{R}^3$.

* Observe que, por uma questão de interpretação física, o parâmetro que denotamos anteriormente por $s$ está sendo denotado agora por $\theta$.

* Se forem $n$ partículas com coordenadas $\mathbf{r} =(\mathbf{r}_1,\ldots,\mathbf{r}_n)$, o grupo de transformações age nas coordenadas de cada partícula, i.e.
$$ R^n_{\boldsymbol{\omega}}(\theta)\mathbf{r} = (R_{\boldsymbol{\omega}}(\theta)\mathbf{r}_1,\ldots,R_{\boldsymbol{\omega}}(\theta)\mathbf{r}_n),
    \qquad \theta\in \mathbb{R}.
$$

* Considere, agora, um Lagrangiano $L(\mathbf{r},\mathbf{\dot r})$ invariante por 
$\{R^n_{\boldsymbol{\omega}}(\theta)\}_{\theta\in \mathbb{R}}$, i.e.

$$ L(R^n_{\boldsymbol{\omega}}(\theta)\mathbf{r},\frac{\mathrm{d}}{\mathrm{d} t} R^n_{\boldsymbol{\omega}}(\theta)\mathbf{q}) 
     = L(\mathbf{r},\mathbf{\dot r}), \qquad \forall \;\theta\in \mathbb{R},
$$

* Então a quantidade conservada é

$$ J(\mathbf{r},\mathbf{\dot r}) = \frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r}) \cdot \mathbf{a}(\mathbf{r}) 
$$

* Sendo que, nesse caso, temos

$$ \mathbf{a}(\mathbf{r}) = \left. \frac{\mathrm{d}}{\mathrm{d} \theta} R^n_{\boldsymbol{\omega}}(\theta)\mathbf{r} \right|_{\theta=0}
$$


### Explicitando a quantidade conservada

* Mais exatamente, temos

$$ \frac{\mathrm{d}}{\mathrm{d} \theta} R^n_{\boldsymbol{\omega}}(\theta)\mathbf{r}
     = ( \frac{\mathrm{d}}{\mathrm{d} \theta} R_{\boldsymbol{\omega}}(\theta)\mathbf{r}_1, \ldots,
         \frac{\mathrm{d}}{\mathrm{d} \theta} R_{\boldsymbol{\omega}}(\theta)\mathbf{r}_n)
$$

* Sendo que

$$ \frac{\mathrm{d}}{\mathrm{d} \theta} R_{\boldsymbol{\omega}}(\theta)\mathbf{r}_i = \boldsymbol{\omega}\times \mathbf{r}_i,
$$

* Logo

$$ \mathbf{a}(\mathbf{r}) = (\boldsymbol{\omega}\times \mathbf{r}_1,\ldots,\boldsymbol{\omega}\times\mathbf{r}_n).
$$

* Observe, ainda que

$$ \frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r})
     = (\frac{\partial L}{\partial\mathbf{\dot r}_i}(\mathbf{r},\mathbf{\dot r}), \ldots, 
         \frac{\partial L}{\partial\mathbf{\dot r}_n}(\mathbf{r},\mathbf{\dot r}))
     = (\mathbf{p}_1,\ldots, \mathbf{p}_n),
$$

* Portanto, 

$$ J(\mathbf{r},\mathbf{\dot r}) =\sum_{i=1}^n \mathbf{p}_i \cdot (\boldsymbol{\omega}\times \mathbf{r}_i).
$$

* Usando a identidade vetorial $\mathbf{a}\cdot(\mathbf{b}\times \mathbf{c}) = \mathbf{b}\cdot(\mathbf{c}\times\mathbf{a})$, temos que

$$ J(\mathbf{r},\mathbf{\dot r}) = \sum_{i=1}^n \boldsymbol{\omega} \cdot (\mathbf{r}_i\times \mathbf{p}_i)
      = \boldsymbol{\omega} \cdot \left( \sum_{i=1}^n \mathbf{r}_i\times \mathbf{p}_i\right)
      = \boldsymbol{\omega} \cdot \mathbf{L}_0
$$

* Essa é a componente, na direção $\boldsymbol{\omega}$, do momento angular $\mathbf{L}_0$ em relação à origem. 

* Quando o Lagrangiano é invariante por rotações em torno de qualquer eixo $\boldsymbol{\omega}$, então o vetor momento angular total é conservado:

$$ \mathbf{L}_0 =  \sum_{i=1}^n \mathbf{r}_i\times \mathbf{p}_i
$$

* Fizemos isso para rotações em torno de eixos passando pela origem. É possível aplicar essas idéias para deduzir que, nos casos apropriados, o vetor momento angular em relação ao centro de massa também é conservado.


## Translações temporais e energia total

* Deduzimos a conservação de energia a partir das equações de Newton no caso de forças autônomas conservativas e sem vínculo.

* Na modelagem Lagrangiana, nessa mesma situação, o Lagrangiano também é independente do tempo.

* Podemos interpretar essa independência em relação ao tempo como uma simetria em relação a translações temporais.

* Dessa simetria, segue uma lei de conservação correspondente.

* Nesse caso, sem vínculos, temos a lei de conservação de energia. Mas o raciocínio também se aplica a Lagrangianos com vínculo, desde que o Lagrangiano seja independente do tempo. Nesse caso com vínculos, no entanto, nem sempre a quantidade conservada é exatamente a energia total, dada pela energia cinética mais a energia potencial.


### Balanço de energia

* Consideremos primeiro um Lagrangiano qualquer, em coordenadas generalizadas $\mathbf{q}=(q_1,\ldots,q_d)$, 

$$ L(\mathbf{q},\mathbf{\dot q}, t).
$$

* Derivando o Lagrangiano em relação ao tempo, ao longo de uma solução do sistema, obtemos

$$ \frac{\mathrm{d}}{\mathrm{d} t} L(\mathbf{q},\mathbf{\dot q},t) 
     = \frac{\partial L}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t)\cdot \mathbf{\dot q}
         + \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q}, t) \cdot\mathbf{\ddot q} 
         + \frac{\partial L}{\partial t}(\mathbf{q},\mathbf{\dot q},t)
$$ 

* Das equações de Euler-Lagrange, temos que

$$ \frac{\partial L}{\partial\mathbf{q}}(\mathbf{q},\mathbf{\dot q},t) 
      = \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t),
$$

* Logo,

$$ \frac{\mathrm{d}}{\mathrm{d} t} L(\mathbf{q},\mathbf{\dot q},t) 
     = \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) \cdot \mathbf{\dot q}
         + \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q}, t) \cdot\mathbf{\ddot q} 
         + \frac{\partial L}{\partial t}(\mathbf{q},\mathbf{\dot q},t).
$$

* Observe que os dois primeiros termos do lado direito são uma derivada temporal de um produto escalar,

$$ \frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t) \cdot \mathbf{\dot q}
         + \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q}, t) \cdot\mathbf{\ddot q} 
         = \frac{\mathrm{d}}{\mathrm{d} t} \left( \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t)\cdot\mathbf{\dot q}\right).
$$

* Reordenando os termos, obtemos

$$  \frac{\mathrm{d}}{\mathrm{d} t} \left( \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t)\cdot\mathbf{\dot q}
         - L(\mathbf{q},\mathbf{\dot q},t) \right)
      = - \frac{\partial L}{\partial t}(\mathbf{q},\mathbf{\dot q},t).
$$

* Definimos

$$ h(\mathbf{q},\mathbf{\dot q},t) =  \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q},t)\cdot\mathbf{\dot q}
         - L(\mathbf{q},\mathbf{\dot q},t).
$$

* Podemos escrever o *balanço de energia*

$$ \frac{\mathrm{d}}{\mathrm{d} t} h(\mathbf{q},\mathbf{\dot q},t) = - \frac{\partial L}{\partial t}(\mathbf{q},\mathbf{\dot q},t).
$$


### Conservação de energia

* Agora, no caso em que o Lagrangiano não depende explicitamente da variável temporal $t$, a derivada que aparece no lado direito da expressão acima é nula, enquanto que $h=h(\mathbf{q},\mathbf{\dot q})$ fica sendo apenas função de $\mathbf{q}$ e $\mathbf{\dot q}$:

$$ h(\mathbf{q},\mathbf{\dot q}) =  \frac{\partial L}{\partial\mathbf{\dot q}}(\mathbf{q},\mathbf{\dot q})\cdot\mathbf{\dot q}
         - L(\mathbf{q},\mathbf{\dot q}).
$$

* Nesse caso, obtemos

$$ \frac{\mathrm{d}}{\mathrm{d} t} h(\mathbf{q},\mathbf{\dot q}) = 0,
$$ 

* Portanto, essa quantidade é conservada:

$$ h(\mathbf{q},\mathbf{\dot q}) = \text{ constante em } t.
$$

* Nesse caso de um Lagrangiano independente de $t$, essa quantidade conservada $h(\mathbf{q},\mathbf{\dot q})$ é chamada de *integral de Jacobi*.

* No caso de um sistema sem vínculos com Lagrangiano $L(\mathbf{r},\mathbf{\dot r}) = K(\mathbf{\dot r}) - V(\mathbf{r}),$ a integral de Jacobi coincide com a energia total do sistema:

$$ h(\mathbf{r},\mathbf{\dot r}) = 2K(\mathbf{\dot r}) - (K(\mathbf{\dot r}) - V(\mathbf{r})) = K(\mathbf{\dot r}) + V(\mathbf{r})
     = E(\mathbf{r},\mathbf{\dot r}).
$$

* Em alguns casos de sistemas com vínculos, a integral de Jacobi também coincide com a energia total, mas este não é o caso geral. Um caso notável é o do pêndulo girante.


## Exercícios

1. Considere um sistema sem vínculos, $L(\mathbf{r},\mathbf{\dot r})=K(\mathbf{\dot r}) - V(\mathbf{r})$, de duas partículas em $\mathbf{r}=(\mathbf{r}_1, \mathbf{r}_2)$ e cujo potencial depende apenas da posição relativa entre essas partículas, i.e $V=V(\mathbf{r}_1-\mathbf{r}_2)$. Mostre que $L(\mathbf{r}, \mathbf{\dot r})$ é invariante por translações de ambas as partículas, em qualquer direção $\mathbf{h}\in \mathbb{R}^3$, $(\mathbf{r}_1,\mathbf{r}_2)\mapsto (\mathbf{r}_1+s\mathbf{h},\mathbf{r}_2+s\mathbf{h})$. Conclua que o momento total $\mathbf{P} = \mathbf{p}_1+\mathbf{p}_2$ é conservado, onde $\mathbf{p}_k =\partial L/\partial\mathbf{\dot r}_k$.

1. Considere agora um problema de $n$ partículas com $r$ vínculos e onde os vínculos são tratados implicitamentes, $\boldsymbol{\Phi}(\mathbf{r}) = 0$, onde $\boldsymbol{\Phi}:\mathbb{R}^{3n} \rightarrow \mathbb{R}^r$. Podemos tratar esse sistema através do Lagrangiano (pense em múltiplicadores de Lagrange no fato de buscarmos um mínimo da ação)
$$ L(\mathbf{r},\boldsymbol{\lambda},\mathbf{\dot r}) = K(\mathbf{\dot r}) - V(\mathbf{r}) + \boldsymbol{\lambda}\cdot\boldsymbol{\Phi}(\mathbf{r}),
$$
onde $\boldsymbol{\lambda}\in \mathbb{R}^r$. Suponha que tanto $V(\mathbf{r})$ como $\boldsymbol{\Phi}(\mathbf{r})$ dependem apenas das posições relativas entre pares de partículas. Conclua que o momento total $\mathbf{P} = \sum_{i=1}^n \mathbf{p}_i$ é conservado, onde $\mathbf{p}_i=\partial L/\partial\mathbf{\dot r}_i$. (Pode ser útil 
começar com o caso mais simples de $n=2$ e $r=1$.)

1. Considere um Lagrangiano $L(\mathbf{r},\mathbf{\dot r})$ e um vínculo escrito na forma implícita $\Phi(\mathbf{r})=0$. Suponha que ambos sejam invariantes por um grupo de transformações $\{G_s\}_{s\in\mathbb{R}}$, i.e. $L(\mathbf{r}_s,\mathbf{\dot r}_s) = L(\mathbf{r},\mathbf{\dot r})$ e $\Phi(\mathbf{r}_s)=\Phi(\mathbf{r})$, para todo $s\in \mathbb{R}$, onde $\mathbf{r}_s=G_s(\mathbf{r})$ e $\mathbf{\dot r}_s= \mathrm{d} G_s(\mathbf{r})/\mathrm{d} t$. Considere o Lagrangiano $L_\Phi(\mathbf{r},\lambda,\mathbf{\dot r})$ do sistema com vínculo implícito.  Mostre que nesse caso também vale a lei de conservação
$$ J(\mathbf{r},\mathbf{\dot r}) = \frac{\partial L}{\partial\mathbf{\dot r}}(\mathbf{r},\mathbf{\dot r})\cdot \mathbf{a}(\mathbf{r}) 
          = \text{ constante em } t,
$$
onde $\mathbf{a}(\mathbf{r})= \mathrm{d} G_s(\mathbf{r})/\mathrm{d} s$, como antes.

1. Mostre que dado um vetor unitário $\boldsymbol{\omega}\in \mathbb{R}^3$ e um vetor qualquer $\mathbf{r}$ que não seja colinear a $\boldsymbol{\omega}$, o conjunto de
vetores
$$ \left\{\frac{\mathbf{r}-(\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega}}{\|\mathbf{r}-(\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega}\|},
            \frac{\boldsymbol{\omega}\times\mathbf{r}}{\|\mathbf{r}-(\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega}\|}, \boldsymbol{\omega}\right\}
$$
forma uma base ortonormal de $\mathbb{R}^3$. Chamando essa base de $\epsilon$, observe que $\mathbf{r}$ pode ser representado nessa base simplesmente por 
$$ [\mathbf{r}]_\epsilon = (\|\mathbf{r}-(\mathbf{r}\cdot\mathbf{r})\boldsymbol{\omega}\|,0,\mathbf{r}\cdot\boldsymbol{\omega}).
$$
Nesse base, também podemos representar o operator rotação $R_{\boldsymbol{\omega}}(\theta)$ por
$$ [R_{\boldsymbol{\omega}}(\theta)]_\epsilon = \left[ 
        \begin{matrix} 
            \cos\theta & -\sin\theta & 0 \\
            \sin\theta & \cos\theta & 0 \\
            0 & 0 & 1
        \end{matrix}
        \right].
$$
Assim,
$$ [R_{\boldsymbol{\omega}}(\theta)\mathbf{r}]_\epsilon = [R_{\boldsymbol{\omega}}(\theta)]_\epsilon[\mathbf{r}]_\epsilon
        = (\cos\theta\|\mathbf{r}-(\mathbf{r}\cdot\mathbf{r})\boldsymbol{\omega}\|, 
            \sin\theta\|\mathbf{r}-(\mathbf{r}\cdot\mathbf{r})\boldsymbol{\omega}\|,
            \mathbf{r}\cdot\boldsymbol{\omega}).
$$
Conclua, finalmente, que, de fato,
$$ R_{\boldsymbol{\omega}}(\theta)\mathbf{r} = (\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega} 
    + (\cos\theta) (\mathbf{r}-(\mathbf{r}\cdot\boldsymbol{\omega})\boldsymbol{\omega})
    + (\sin\theta) \boldsymbol{\omega}\times\mathbf{r}.
$$

1. Continuando o exercício acima, mostre que 
$$ \frac{\mathrm{d}}{\mathrm{d} \theta} R_{\boldsymbol{\omega}}(\theta)\mathbf{r} = \boldsymbol{\omega}\times\mathbf{r}.
$$

1. Ache a integral de Jacobi nos seguintes casos e verifique se ela coincide com a energia total.
    1. Corpo em queda livre sob a atração gravitacional uniforme perto da superfície da Terra;
    2. Pêndulo planar;
    3. Pêndulo girante;
    4. Sistema massa-mola harmônica unidimensional;
    5. Sistema massa-mola harmônica planar sob a ação gravitacional uniforme;
    6. Sistema planar de dois corpos celestes sob a atração gravitacional;
    7. Um corpo de massa $m$ deslizando sobre uma curva $z=h(x)$, $y=0$, sob a atração gravitacional uniforme $\mathbf{F} =(0,0,-mg)$.

1. Considere o sistema de três corpos planar restrito, utilizando coordenadas polares em um sistema de coordenadas girante. Mais precisamente, temos dois corpos celestes $T$ e $L$ com massas $M_T$ e $M_L$, e com $L$ em órbita circular em torno de $T$. Colocando $T$ no centro de referência e o a órbita circular no plano $xy$, temos as coordenadas de cada um deles dadas por $\mathbf{r}_T=(0,0,0)$ e $\mathbf{r}_L=(R\cos(\omega t), R\sin(\omega T),0)$, onde $R$ é o raio da órbita e $\omega$ é a freqüência de oscilação da órbita ($2\pi/$período). O terceiro corpo é um "satélite", no sentido de ter uma massa $m\ll M_T,M_L$, desprezível em relação à massa dos outros dois corpos, portanto não influenciando o movimento deles. Além disso, assumimos que esse terceiro corpo se movimento no mesmo plano da órbita de $L$ em torno de $T$. Como coordenadas generalizadas, podemos utilizar as coordenadas polares $(r,\theta)$, onde $\theta$ indica o ângulo entre o vetor posição $\mathbf{r}$ do satélite e o vetor posição $\mathbf{r}_L$ do corpo $L$. O referencial $(r,\theta)$ não é inercial. O referencial "girante" $(x', y')=(r\cos\theta,r\sin\theta)$ também não é inercial. mas no referencial inercial $xyz$ podemos escrever a posição do satélite em termos das coordenadas generalizadas $(r,\theta)$ através de $\mathbf{r}=(r\cos(\theta+\omega t),r\sin(\theta+\omega t))$.
    1. Escreva o Lagrangiano $L(r,\theta,\dot r,\dot\theta)$ desse sistema;
    2. Ache os momentos generalizados $p_r$ e $p_\theta$ e verifique se eles são conservados ou não;
    3. Ache a integral de Jacobi e diga se ela é invariante ou não.
    4. Verifique se a integral de Jacobi coincide com a energia total (cinética + potencial) do sistema.
