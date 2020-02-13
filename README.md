# Modelagem Matemática - IM/UFRJ - Período 2020/1

Notas de aula da disciplina de Modelagem Matemática do Instituto de Matemática da UFRJ, do período 2020/1.

Professor da disciplina neste período: [Ricardo M. S. Rosa](http://www.im.ufrj.br/rrosa/).

## *Links* de acesso direto aos cadernos

*Links* para acessar a página inicial das notas de aula, do período 2020/1, via [Github](https://github.com), [Binder](https://beta.mybinder.org/) e [Google Colab](http://colab.research.google.com):

[![Github](https://img.shields.io/badge/view%20on-github-orange)](aulas/00.00-Pagina_Inicial.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rmsrosa/modelagem_matematica/master?filepath=aulas%2F00.00-Pagina_Inicial.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rmsrosa/modelagem_matematica/blob/master/aulas/00.00-Pagina_Inicial.ipynb)

Link para o *branch* das aulas do período anterior:

[![ModMat2019p1](https://img.shields.io/badge/branch-ModMat2019p1-darkgreen)](https://colab.research.google.com/assets/colab-badge.svg)

## Observações

- As **notas de aula** estão dispostas na forma de uma coleção de [cadernos Jupyter](https://jupyter.org/) e estão disponíveis no subdiretório [aulas](aulas). As notas serão escritas e disponibilizadas ao longo do curso.

- Há uma [Página Inicial](aulas/00.00-Pagina_Inicial.ipynb) exibindo a coleção de cadernos de forma estruturada, com links para cada caderno.

- Os cadernos podem ser visualizados dentro do próprio [Github](https://github.com), ou acessadas, modificadas e executadas nas "nuvens de computação" [Binder](https://beta.mybinder.org/) e [Google Colab](http://colab.research.google.com), através dos links exibidos acima.

- Cada período será mantido em um *branch* próprio do repositório. As notas do período corrente são mantidas no *branch* [master](https://github.com/rmsrosa/modelagem_matematica). Ao final do período, serão transferidas para outro *branch*.

- As edições anteriores da disciplina, ministradas neste formato, e que estão em outros *branches*, podem ser acessadas diretamente através dos seguintes *links:*

  - [Modelagem Matemática - Período 2019/1](https://github.com/rmsrosa/modelagem_matematica/tree/modmat2019p1).

- Ao longo do período, é esperado que os alunos modifiquem os cadernos existentes e criem os seus próprios cadernos para resolver os exercícios, os testes e escrever os mini-projetos e o projeto final.

- Em princípio, a comunicação entre o professor e os alunos será feita, prioritariamente, através do [AVA @ UFRJ (Ambiente Virtual de Aprendizagem na UFRJ)](http://ambientevirtual.nce.ufrj.br/). Informes via [SIGA/Intranet UFRJ](https://intranet.ufrj.br/) também podem ser utilizados, assim como mensagens via *e-mail*.

- Cada *branch*, contendo a coleção de todos os cadernos, figuras, dados e códigos que compõem as notas de aula, podem ser baixadas para uma máquina local através do botão `Clone or Download` da página inicial [rmsrosa/modelagem_matematica](https://github.com/rmsrosa/modelagem_matematica) do *branch* de cada repositório, escolhendo a opção `Download ZIP`.

- Cada caderno, além de poder ser visualizado diretamente no [Github](https://github.com) e acessado nas nuvens de computação, também pode ser baixado individualmente para uma máquina local clicando-se no ícone `Raw`, que aparece em cada página, e baixando para a sua máquina o conteúdo que aparecer no navegador (é um arquivo fonte de cadernos [jupyter](https://jupyter.org/), com a extensão `".ipynb"`).

- As alterações nos cadernos deste repositório e a criação de novos cadernos podem ser feitas localmente, em máquinas com o Python (versão 3.6 ou maior) e os devidos pacotes devidamente instalados, ou nas nuvens de computação mencionadas acima.

- A lista dos pacotes python necessários para a execução do conjunto de cadernos aparece no arquivo [requirements.txt](requirements.txt). Esse arquivo não é apenas uma referência, ele é necessário para o [Binder](https://beta.mybinder.org/) poder montar o ambiente python com todos os pacotes a serem utilizados. O [Google Colab](http://colab.research.google.com), por outro lado, já tem o seu próprio ambiente, bastante completo, e não depende deste arquivo.

- No [Binder](https://beta.mybinder.org/) e no [Google Colab](http://colab.research.google.com), um ambiente python temporário é montado e os cadernos podem ser alterados e executados interativamente. Mas eles não são guardados para uma próxima sessão. Se quiser salvar as alterações, é necessário baixar os cadernos alterados para a sua máquina.

- Uma alternativa, caso tenha o [Google Drive](https://www.google.com/drive/), é habilitar o [Google Colab](http://colab.research.google.com) em sua conta do Google e copiar as notas para um diretório denominado *Colab Notebooks* que será automaticamente criado em seu [Google Drive](https://www.google.com/drive/). Nesse caso, as notas podem ser acessadas, executadas e gravadas normalmente para uso posterior, como se estivesse com uma instalação local do [jupyter](https://jupyter.org/).

- Vale ressaltar, no entanto, que o funcionamento do jupyter no [Google Colab](http://colab.research.google.com) é um pouco diferente do padrão e o acesso aos arquivos locais é um pouco mais delicado.

- Uma outra alternativa é criar uma conta no [github](https://github.com), *clonar* o repositório e usar o [Google Colab](http://colab.research.google.com) ou o [Binder](https://beta.mybinder.org/) a partir do seu repositório. Será necessário, no entanto, após a clonagem, modificar os cadernos para atualizar os links com o nome do seu repositório. Trabalhar com o github não é trivial, mas uma vantagem é que será mais fácil submeter correções ou sugestões para este repositório, ajudando-o a melhorar.

- Abrir um conta no [github](https://github.com) também permite marcar este repositório com uma "estrela", para acesso direto a partir do seu perfil. É uma espécie de "bookmark". Isso pode ser feito clicando-se no botão *Star*, no canto superior direito do repositório.

- Outra opção é clicar no botão *Watch*, também no canto superior direito do repositório. Dessa forma, você receberá notificações, por *e-mail*, sobre qualquer modificação feita no mesmo.

- Há um *branch* [livro](https://github.com/rmsrosa/modelagem_matematica/tree/livro), que contém uma versão bastante preliminar de um livro-texto para a disciplina. Este livro-texto ainda não está sendo muito utilizado na matéria. A ideia, no entanto, é que ele seja aprimorado aos poucos e que seja mais útil em uma das próximas edições da disciplina.

## Licença

Os **textos** neste repositório estão disponíveis sob a licença [CC-BY-NC-ND license](LICENSE-TEXT). Mais informações sobre essa licença em [Creative Commons Attribution-NonCommercial-NoDerivs 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode).

Os **códigos** neste repositório, nos blocos de código dos [jupyter notebooks,](https://jupyter.org/) estão disponíveis sob a [licença GNU-GPL](LICENSE-CODEE). Mais informações sobre essa licença em [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl.html).
