
@def title = "Mínimos quadrados não-linear"

# {{ get_title }}

* Modelos reais são raramente lineares.

* E nem todos os fenômenos lineares podem ser bem aproximados por modelos redutíveis a lineares, como vimos da última vez.

* Como ajustar parâmetros de modelos genuinamente não lineares?


## Contexto

* Considere um conjunto de dados $(x_i, y_i)$ com $x_i, y_i \in \mathbb{R}$, $i = 1, \ldots, N$.

* Buscamos aproximar o fenômeno com um modelo da forma
$$y(x) =  \varphi(x, \boldsymbol{\beta}),$$
onde $\boldsymbol{\beta} = (\beta_1, \ldots, \beta_m)$ é um conjunto de parâmetros (desconhecidos) do modelo.

* Idealmente, poderíamos ajustar os parâmetros por **colocação**, ou seja, de tal forma que eles coincidissem em todos os dados:
$$y(t_i) =  \varphi(x_i ; \beta), \quad i=1, \ldots, N.$$

* No entanto, assim como no caso linear, não esperamos essa "perfeição" em geral.


### O problema de mínimos quadrados não linear

* Buscamos, então, *reduzir o erro*, em algum sentido. Por exemplo, o de minimizar o **erro quadrático**
$$ E(\boldsymbol{\beta}) = \sum_{i=1}^N |y_i - \varphi(x_i,\boldsymbol{\beta})|^2.
$$

* Cada componente é, novamente, chamado de **resíduo** (não-linear)
$$ r_i = y_i - \varphi(x_i,\boldsymbol{\beta}), \qquad i=1, \ldots, N.
$$

* Assim, chegamos ao problema de **otimização**
$$ \hat{\boldsymbol{\beta}} = \operatorname{argmin}_{\boldsymbol{\beta}} \sum_{i=1}^N |y_i - \varphi(x_i,\boldsymbol{\beta})|^2.
$$


### Condição para ser ponto de mínimo

* Uma condição **necessária** para que $\hat{\boldsymbol\beta}$ seja um ponto de mínimo de $E(\boldsymbol\beta)$ é que ele seja um **ponto crítico:**
$$\nabla E(\hat{\boldsymbol\beta}) = 0.
$$

* Em termos de coordenadas, é necessário que
$$ \frac{\partial}{\partial \beta_j} E(\hat{\boldsymbol\beta}) = 0, \qquad \forall j=1, \ldots, m.
$$

* Calculando explicitamente, temos
$$ \frac{\partial}{\partial \beta_j} E(\hat{\boldsymbol\beta}) =   \frac{\partial}{\partial \beta_j}\left( \sum_{i=1}^N \left|y_i - \varphi(x_i, \boldsymbol\beta)\right|^2 \right) =  \sum_{i=1}^N (y_i - \varphi(x_i, \boldsymbol\beta))\frac{\partial}{\partial \beta_j}\varphi(x_i, \boldsymbol{\beta}) = 0,
$$
para $j=1, \ldots, m.$

* Em termos matriciais, podemos escrever
$$D\mathbf{r}(\hat{\boldsymbol\beta})^t \mathbf{r}(\hat{\boldsymbol\beta}) = 0. \quad\quad (2)
$$
onde $D\mathbf{r}(\boldsymbol\beta)^t$ é a transposta da matriz Jacobiana $D\mathbf{r}(\boldsymbol\beta)$, cujas linhas são os gradientes da função vetorial cujos componentes são os resíduos:
$$ \mathbf{r}(\boldsymbol\beta) = \left(y_i - \varphi(x_i, \boldsymbol\beta)\right)_{i=1, \ldots, n}.
$$


### Interlúdio para o caso linear

* Observe que, no caso linear, temos
$$\mathbf{r}(\boldsymbol\beta) = A \boldsymbol\beta - \mathbf{b}$$
e a equação acima se reduz à equação normal do problema de mínimos quadrados linear:
$$ A^t(A\boldsymbol\beta) = A^t\mathbf{b}.
$$

* Diferentemente do caso linear, onde a hipótese de $A$ ter posto completo (com $m$ colunas linearmente independentes) implica na convexidade de $\mathbf{r}$ (hessiana positiva-definida), e portanto na unicidade da solução de, o caso não-linear tem a condição acima apenas como **necessária**. Podem existir vários pontos de mínimo local.


## Algoritmos

* Os métodos de **Gradiente descendente**, **Gauss-Newton** e **Levenberg-Marquardt**, por exemplo, são algoritmos iterativos clássicos.

* Neles, busca-se uma **sequência minimizante** $\boldsymbol\beta^{(0)}, \boldsymbol\beta^{(1)}, \ldots$ se aproximando do ponto de mínimo desejado.

* A escolha do ponto de partida $\boldsymbol\beta^{(0)}$ é delicada, pois pode nos levar à mínimos locais, longe de um bom ajuste.

* O algoritmo termina quando algum **critério de parada** é alcançado. Por exemplo:
  * quando o erro $E(\boldsymbol\beta)$ é suficientemente pequeno;
  * quando a variação em $E(\boldsymbol\beta)$ é suficientemente pequena;
  * quando ${\boldsymbol\beta}^{(k+1)}$ está bem próximo de $\boldsymbol\beta^{(k)}$; ou
  * quando um número máximo de iterações é atingido.


### Gradiente descendente

* Esse método é bastante intuitivo.

* Assumindo que a função $E(\boldsymbol\beta)$ seja suave, a sua direção de maior decrescimento é a contrária ao seu gradiente.

* A idéia, então, é dar um passo na direção contrária ao gradiente, em cada iteração:

    1. Dado um ponto $\boldsymbol{\beta}^{(k)}$, em que o erro $E(\boldsymbol{\beta}^{(k)})$ ainda não é suficientemente pequeno (caso contrário já teríamos resolvido o problemo), calculamos o gradiente
    $$ \nabla E(\boldsymbol{\beta}^{(k)})
    $$
    1. Dado um "tamanho de passo" $\eta$, "andamos" na direção contrária, escolhendo o próximo ponto $\boldsymbol{\beta}^{(k+1)}$ como
    $$ \boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - \eta \nabla E(\boldsymbol{\beta}^{(k)}).
    $$


#### Deficiências do método de gradiente descendente

* A sua convergência é relativamente lenta.

* A escolha do tamanho de passo $\eta$ não segue uma receita muito bem definida.

* Passos muito grandes podem fazer com que o método não-convirja ("pule para um lugar mais alto do outro lado do vale").

* Passos muito pequenos podem levar ao acúmulo de erros numéricos ("pequenas mudanças em um passo curto acarretam em grandes mudanças no ângulo de direcionamento).


### Gauss-Newton

* O método consiste basicamente nos seguintes ingredientes:
    1. Pensar no objetivo $E(\boldsymbol{\beta}) = \|\mathbf{r}\|^2 = 0$ como um **objetivo para os resíduos**:
    $$ \mathbf{r}(\boldsymbol{\beta}) = \mathbf{0};
    $$
    1. Dado o $k$-ésimo termo da sequência, obter uma **aproximação afim** da função $\mathbf{r}$ perto do ponto $\boldsymbol{\beta}^{(k)}$;
    1. Minimizar o erro quadrático da aproximação afim.
    1. Olhar para essa solução como o novo termo $\boldsymbol{\beta}^{(k+1)}$ da sequência;
    1. Repetir o processo até alcançar um dos critérios de parada.


#### Aproximação afim

1. A partir do ponto $\boldsymbol{\beta}^{(k)}$, em que o erro $E(\boldsymbol{\beta}^{(k)})$ ainda não é suficientemente pequeno (caso contrário já teríamos resolvido o problema), buscamos uma aproximação linear para os resíduos $\mathbf{r}(\boldsymbol{\beta})$.

1. Como aproximação linear, é natural tomarmos a linearização em torno do ponto dado:
$$ \mathbf{r}(\boldsymbol{\beta}) \approx \mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)}),
$$
onde $D\mathbf{r}(\boldsymbol{\beta}^{(k)})$ é a diferencial de $\mathbf{r}$, cusas linhas são os gradientes de cada resíduo $r_i$.


#### Iteração

3. Agora, buscamos $\boldsymbol{\beta}$ de forma a minimizar o erro quadrático segundo essa aproximação afim
$$ \boldsymbol{\beta}^{(k+1)} = \operatorname{argmin}_{\boldsymbol{\beta}} \|\mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)})\|^2.
$$

3. Isso nada mais é do que um problema de mínimos quadrados linear.

3. Assumindo-se que as colunas de $D\mathbf{r}(\theta^{(k)})$ sejam **linearmente independentes** (i.e. $N\geq m$ e matriz com posto máximo), a solução é dada pelas equações normais
$$ \left(D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)})\right)\boldsymbol{\beta}^{(k+1)} = D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t\left(D\mathbf{r}(\boldsymbol{\beta}^{(k)})\boldsymbol{\beta}^{(k)}) - \mathbf{r}(\boldsymbol{\beta}^{(k)})\right).
$$

5. Nesse caso, o processo iterativo pode ser escrito na forma
$$ \boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - \left( D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)})\right)^{-1} D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t\mathbf{r}(\boldsymbol{\beta}^{(k)}).
$$


**Observação:** No caso de uma matriz quadrada ($m=N$) invertível, obtemos o método de Newton $\boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - D\mathbf{r}(\boldsymbol{\beta}^{(k)})^{-1}\mathbf{r}(\boldsymbol{\beta}^{(k)})$.


#### Deficiências do Gauss-Newton

1. **O método pode divergir**: Isso pode acontecer quando $\boldsymbol\beta^{(k+1)}$ não está muito próximo de $\boldsymbol\beta^{(k)}$, de modo que o passo seja muito grande;

2. **O método pode ter que ser abortado**: A hipótese de que as colunas de $D\mathbf{r}(\boldsymbol\beta^{(k)})$ sejam linearmente independentes pode falhar em alguma iteração, de modo que o cálculo de $\theta^{(k+1)}$ não seja possível.


### Levenberg-Marquardt

* É mais recente, de meados do século XX.

* Motivado pelas deficiências do método de Gauss-Newton.

* Pode ser visto como um meio termo entre o gradiente descendente e o Gauss-Newton.

* É uma forma de um Gauss-Newton amortecido.

* Pode ser mais lento, mas é mais robusto do que o Gauss-Newton.

* Procura alcançar dois objetivos:
    1. Fazer o erro quadrático pequeno.
    2. Fazer o passo  $\|\boldsymbol\beta^{(k+1)} - \boldsymbol\beta^{(k)}\|$ também pequeno.


#### Implementação dos objetivos

* Para "penalizar" tanto o erro quando o passo, a ideia é obter $\boldsymbol\beta^{(k+1)}$ através da minimização de
$$ \|\mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)})\|^2 + \lambda\|\boldsymbol\beta - \boldsymbol\beta^{(k)}\|^2.
$$

* Isso leva em consideração a aproximação afim do erro, sendo, portanto, uma aproximação quadrádica de
$$ \|\mathbf{r}(\boldsymbol{\beta})\|^2 + \lambda\|\boldsymbol\beta - \boldsymbol\beta^{(k)}\|^2.
$$

* O parâmetro $\lambda$ é um parâmetro positivo de *regularização*, ou *suavização*, ou, ainda, de *amortecimento*.

* Esse é um problema de mínimos quadrados linear **multi-objetivo**.


#### Iteração

* O parâmetro é escolhido a cada passo, $\lambda=\lambda^{(k)}$, nos levando ao problema iterativo
$$ \boldsymbol\beta^{(k+1)} = \operatorname{argmin}_{\boldsymbol\beta}\left[\|\mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)})\|^2 + \lambda^{(k)}\|\boldsymbol\beta - \boldsymbol\beta^{(k)}\|^2\right].
$$


#### Resolução

* Podemos escrever
$$
\|\mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)})\|^2 + \lambda\|\boldsymbol\beta - \boldsymbol\beta^{(k)}\|^2 \\
= \left\| \begin{matrix} \mathbf{r}(\boldsymbol{\beta}^{(k)}) + D\mathbf{r}(\boldsymbol{\beta}^{(k)})(\boldsymbol{\beta} - \boldsymbol{\beta}^{(k)}) \\ \sqrt{\lambda}(\boldsymbol\beta - \boldsymbol\beta^{(k)})\end{matrix}\right\|^2 \\ 
= \left\| \left[\begin{matrix} D\mathbf{r}(\boldsymbol{\beta}^{(k)}) \\ \sqrt{\lambda}I\end{matrix}\right]\boldsymbol{\beta}  - \left(\begin{matrix} D\mathbf{r}(\boldsymbol{\beta}^{(k)})\boldsymbol{\beta}^{(k)} - \mathbf{r}(\boldsymbol{\beta}^{(k)}) \\ \sqrt{\lambda}\boldsymbol\beta^{(k)}\end{matrix}\right)\right\|^2.
$$

* Por esse ponto de vista, é um clássico problema de mínimos quadrados linear da form $\operatorname{argmin}\|A\boldsymbol\beta + \mathbf{y}\|^2$.

* Se $D\mathbf{r}(\boldsymbol{\beta}^{(k)})$ tiver posto máximo, assim também o tem a matriz $A$, de forma que o problema tem solução única.

* A sua forma normal $A^tA\boldsymbol{\beta} = A^t\mathbf{y}$ nos leva à fórmula de recursão (verifique!)
$$\boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - \left( D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)}) + \lambda^{(k)}I \right)^{-1} D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t \mathbf{r}(\boldsymbol{\beta}^{(k)}).$$


#### Amortecimento

* Reescrevemos
$$\boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - \left( D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)}) + \lambda^{(k)}I \right)^{-1} D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t \mathbf{r}(\boldsymbol{\beta}^{(k)})$$
como
$$\left( D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)}) + \lambda^{(k)}I \right)\left(\boldsymbol{\beta}^{(k+1)} - \boldsymbol{\beta}^{(k)}\right) = -  D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t \mathbf{r}(\boldsymbol{\beta}^{(k)}).$$

* Observe que $\lambda^{(k)}>0$ tem o papel de reduzir o passo $\boldsymbol{\beta}^{(k+1)} - \boldsymbol{\beta}^{(k)}$.

* Por esse motivo ele é visto como um parâmetro de amortecimento.

* Ele também busca evitar abrutos "buracos" locais.


### Sobre o parâmetro de amortecimento

* O parâmetro $\lambda^{(k)}$ é também conhecido como parâmetro de confiança, pois outra forma de interpretar o problema de otimização resolvido a cada iteração é como um método de região de confiança (*trust-region method*). 

* Visto como um parâmetro de regularização/penalização, ele controla qual parte da função objetivo é levada mais em consideração.

* Diferentes estratégias para a escolha do parâmetro podem ser seguidas.
Maiores informações podem ser encontradas em [Boyd]().   


### Outros métodos

* Há vários outros métodos, alguns sendo variações dos vistos acima (e.g gradiente estocástico), mas não é o nosso objetivo explorar os diversos métodos. Isso fica para um curso de otimização.

* Vários métodos não são especificos para mínimos quadrados (não-linear), mas se aplicam a minimização de funções não-lineares em geral, como o [método de Newton](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization), [Davidon–Fletcher–Powell (DFP)](https://en.wikipedia.org/wiki/Davidon–Fletcher–Powell_formula), [Broyden–Fletcher–Goldfarb–Shanno (BFGS)](https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm) e [Limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS), etc.

* Devo mencinar que os métodos como descritos acima são métodos para problemas de minimização *sem restrição*.

* Métodos para problemas com restrição podem ser modificados para levar a restrição em consideração ou para atacar um formulação via multiplicadores de Lagrange.


### Métodos livre de derivada

* Devo ressaltar, ainda, os métodos **livres de derivada**, ou *derivative-free*.

* São úteis quando não temos a derivada disponível ou ela é muito custosa de se calcular.

* Exemplos notáveis são os seguintes.
    * **Nelder-Mead:** busca através de polítopos com $m+1$ vértices (e.g. vértices de triângulos no plano). Avalia a função nos vértices de um polítopo, (que muda a cada iteração, exceto pelo ponto "base"), retendo o ponto de mínimo dentre os vértices omo um novo ponto base para a formação do próximo polítopo.
    * **Algoritmos genéticos:** parte-se de vários pontos escolhidos aleatoriamente e busca-se reduzir o erro em cada ponto através de funções objetivo envolvendo outros critérios.
    * **Região de confiança:** busca-se modelos que aproximem bem localmente, aumentando-se aos poucos a região de busca.
    * ***Simulated annealing:*** busca-se reduzir uma função "temperatura" de maneira probabilística.


## Exercícios

1. Verifique a formula do gradiente da função erro $E(\boldsymbol\beta) = \|\mathbf{r}(\boldsymbol\beta)\|^2$, onde $\mathbf{r}(\boldsymbol\beta)$ é o vetor $\mathbf{r}(\boldsymbol\beta) = \left(y_i - \varphi(x_i, \boldsymbol\beta)\right)_{i=1}^N$.

1. Obtenha a fórmula
$$\boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - \left( D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t D\mathbf{r}(\boldsymbol{\beta}^{(k)}) + \lambda^{(k)}I \right)^{-1} D\mathbf{r}(\boldsymbol{\beta}^{(k)})^t \mathbf{r}(\boldsymbol{\beta}^{(k)}).$$
a partir da forma normal  $A^tA\boldsymbol{\beta} = A^t\mathbf{y}$ como descrito no método de Levenberg-Marquardt.

1. Escreva explicitamente a fórmula iterativa $\beta^{(k+1)} = \beta^{(k)} + \ldots$ quando temos apenas um parâmetro $\beta\in \mathbb{R}$ e o modelo tem a forma $y = \varphi(x, \beta) = x^2 + \sin(\beta x)$.


## Referência

1. [S. Boyd, L. Vandenberghe, *Introduction to Applied Linear Algebra – Vectors, Matrices, and Least Squares*, Cambridge University Press, 2018.](https://web.stanford.edu/~boyd/vmls/)
