# Modelagem Matemática - IM/UFRJ - Período 2021/1

[![Text License: CC-BY-NC-ND license](https://img.shields.io/badge/Text%20License-CC--BY--NC--ND-yellow.svg)](https://opensource.org/licenses/MIT) [![Code License: GNU-GPLv3](https://img.shields.io/badge/Code%20License-GNU--GPLv3-yellow.svg)](https://www.gnu.org/licenses/gpl.html) ![GitHub repo size](https://img.shields.io/github/repo-size/rmsrosa/nbbinder)

Notas de aula da disciplina de Modelagem Matemática do Instituto de Matemática da UFRJ do Professor [Ricardo M. S. Rosa](http://www.im.ufrj.br/rrosa/), período 2021/1.

## Links diretos para as notas de aula

[![Github](https://img.shields.io/badge/ModMat2021p1-github-green.svg?logo=github)](notas_de_aula/00.00-Pagina_inicial.ipynb) [![NBViewer](https://img.shields.io/badge/ModMat2020p2-nbviewer-orange.svg?logo=nbviewer)](https://nbviewer.jupyter.org/github/rmsrosa/modelagem_matematica/blob/modmat2021p1/notas_de_aula/00.00-Pagina_inicial.ipynb) [![ModMat2021p1 Binder](https://img.shields.io/badge/ModMat2021p1-binder-E66581.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/rmsrosa/modelagem_matematica/julia-env-for-binder-2021p1?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Frmsrosa%252Fmodelagem_matematica%26urlpath%3Dtree%252Fmodelagem_matematica%252Fnotas_de_aula%252F00.00-Pagina_inicial.ipynb%26branch%3Dmodmat2021p1) [![ModMat2020p2 Colab](https://img.shields.io/badge/ModMat2021p1-colab-blue.svg?logo=google%20colab)](https://colab.research.google.com/github/rmsrosa/modelagem_matematica/blob/motmat2021p1/notas_de_aula/00.00-Pagina_inicial.ipynb)

## Utilização

- As notas de aula estão dispostas na forma de uma coleção de [cadernos Jupyter](https://jupyter.org/), e estão disponíveis no subdiretório [notas_de_aula](notas_de_aula).

- Há uma [Página Inicial](notas_de_aula/00.00-Pagina_Inicial.ipynb) exibindo a coleção de cadernos de forma estruturada, com links para cada caderno.

- Os cadernos podem ser visualizados dentro do próprio [Github](https://github.com), ou acessadas nas "nuvens de computação" [Binder](https://beta.mybinder.org/) e [Google Colab](http://colab.research.google.com), através dos links exibidos acima.

- A utilização no [Google Colab](http://colab.research.google.com), no entanto, não é imediata. É preciso configurá-lo para rodar Julia. Mais sobre isso em breve. Mas o [Binder](https://beta.mybinder.org/) já está preparado para rodar sem mais configurações.

- As notas de aula estão inteiramente disponíveis *online* neste repositório.

- Cada período será mantido em um ramo próprio do repositório. Este é sobre o período 2021/1.

- O repositório inteiro, incluindo a coleção com todos os cadernos que compõem as notas de aula, pode ser copiado *(downloaded)* para uma máquina local através do link `Clone or Download` da página inicial do repositório, escolhendo a opção `Download ZIP`.

- Cada caderno, além de poder ser visualizado diretamente no [Github](https://github.com), também pode ser copiado individualmente para uma máquina local clicando-se no ícone `Raw`, que aparece em cada página, e salvando o conteúdo que aparece (é um arquivo fonte de cadernos [jupyter](https://jupyter.org/), com a extensão `".ipynb"`).

- Contrariamente às outras edições, desta vez vamos utilizar a linguagem de programação [Julia](https://julialang.org). Mais sobre isso nas notas de aula.

## Modificando os cadernos

Ao longo do período, é esperado que os alunos modifiquem os cadernos existentes e criem os seus próprios cadernos para resolver os exercícios, os testes e escrever os mini-projetos e o projeto final.

- Isso pode ser feito localmente, em máquinas com [Julia](https://julialang.org) e com os devidos pacotes devidamente instalados (veja os pacotes no arquivo [Project.toml](Project.toml)).

- Caso não seja possível trabalhar localmente, é possível trabalhar na "nuvem". Ao acessar os arquivos deste repositório no [Binder](https://beta.mybinder.org/), um ambiente Julia temporário é montado e os cadernos podem ser alterados e executados interativamente. Mas eles não são guardados para uma próxima sessão. Se quiser salvar as alterações, é necessário "baixar" os cadernos alterados para a sua máquina. Esses arquivos baixados podem ser carregados novamente em sessões futuras do Binder.

- Uma alternativa, caso tenha o [Google Drive](https://www.google.com/drive/), é habilitar o [Google Colab](http://colab.research.google.com) em sua conta do Google e copiar as notas para um diretório denominado *Colab Notebooks* que será automaticamente criado em seu [Google Drive](https://www.google.com/drive/). Nesse caso, as notas podem ser acessadas, executadas e gravadas normalmente, como se estivesse com uma instalação local do [jupyter](https://jupyter.org/). Mas, como ressaltado acima, a utilização no colab não é imediata.

- Uma outra alternativa é criar uma conta no [github](https://github.com), *clonar* o repositório e usar o [Google Colab](http://colab.research.google.com) ou o [Binder](https://beta.mybinder.org/) a partir do seu repositório. Será necessário, no entanto, após a clonagem, modificar os cadernos para atualizar os links com o nome do seu repositório. Trabalhar com o github não é trivial, mas uma vantagem é que será mais fácil submeter correções ou sugestões para este repositório, ajudando-o a melhorar.

## Edições atual e anteriores

O material de cada edição da disciplina ministrada neste formato está em um determinado ramo *(branch)* deste repositório:

[![ModMat2021p1](https://img.shields.io/badge/Repo%20Branch-ModMat2021p1-darkgreen)](https://github.com/rmsrosa/modelagem_matematica/tree/modmat2021p1)

[![ModMat2020p2](https://img.shields.io/badge/Repo%20Branch-ModMat2020p2-darkgreen)](https://github.com/rmsrosa/modelagem_matematica/tree/modmat2020p2)

[![ModMat2019p1](https://img.shields.io/badge/Repo%20Branch-ModMat2019p1-darkgreen)](https://github.com/rmsrosa/modelagem_matematica/tree/modmat2019p1)

PS: A edição de 2020/1 foi adiada devido à pandemia de Covid-19 e outro professor acabou sendo responsável pela disciplina. Dessa maneira, o material não foi disponibilizado por aqui.

## Licença

Os **textos** neste repositório estão disponíveis sob a licença [CC-BY-NC-ND license](LICENSE-TEXT). Mais informações sobre essa licença em [Creative Commons Attribution-NonCommercial-NoDerivs 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode).

Os **códigos** neste repositório, nos blocos de código dos [jupyter notebooks](https://jupyter.org/) ou em arquivos separados de códigos, estão disponíveis sob a [licença GNU-GPL](LICENSE-CODE). Mais informações sobre essa licença em [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl.html).
