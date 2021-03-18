# Ambiente Julia do Binder para as notas de aula de Modelagem Matemática - IM/UFRJ

[![Text License: CC-BY-NC-ND license](https://img.shields.io/badge/Text%20License-CC--BY--NC--ND-yellow.svg)](https://opensource.org/licenses/MIT) [![Code License: GNU-GPLv3](https://img.shields.io/badge/Code%20License-GNU--GPLv3-yellow.svg)](https://www.gnu.org/licenses/gpl.html) ![GitHub repo size](https://img.shields.io/github/repo-size/rmsrosa/nbbinder)

Esse ramo do repositório é utilizado apenas para a criação do ambiente Julia pelo [binder](https://mybinder.org). O conteúdo principal do repositório está em outros ramos, cada um relativo ao seu semestre:

[![ModMat2020p2](https://img.shields.io/badge/Repo%20Branch-ModMat2020p2-darkgreen)](https://github.com/rmsrosa/modelagem_matematica/tree/modmat2020p2) [![Binder ModMat2020p2](https://img.shields.io/badge/Binder%20Launch-ModMat2020p2-orange)](https://mybinder.org/v2/gh/rmsrosa/modelagem_matematica/julia-env-for-binder?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Frmsrosa%252Fmodelagem_matematica%26urlpath%3Dtree%252Fmodelagem_matematica%252Fnotas_de_aula%26branch%3Dmodmat2020p2)

No momento do primeiro acesso, após cada alteração (i.e. cada novo *commit*) no repositório, um novo ambiente binder precisa ser gerado pelo [binder](https://mybinder.org), acarretando em uma grande demora no acesso. Isso acontece independemente da alteração ser nas informações essenciais ao ambiente (e.g. nos arquivos `Package.toml`, `requirements.txt`, `environment.yaml`, etc.) ou no conteúdo (e.g. `README.md`, Jupyter notebooks).

Ao separarmos as informações do ambiente para o Binder do conteúdo principal, evitamos que um novo ambiente seja gerado a cada alteração no conteúdo, acelerando o processo.

Este é o objetivo deste ramo. Ele contém apenas as informações para a geração do ambiente binder.

Isso é possível graças ao uso do [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/index.html). Ele carrega o ambiente deste ramos e puxa o conteúdo de outro ramos. O link para "pushar" um determinado conteúdo para o ambiente binder foi gerado em [nbgitpuller link generator](https://jupyterhub.github.io/nbgitpuller/link#nbgitpuller-link-generator)

## Licença

Os **textos** neste repositório estão disponíveis sob a licença [CC-BY-NC-ND license](LICENSE-TEXT). Mais informações sobre essa licença em [Creative Commons Attribution-NonCommercial-NoDerivs 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/us/legalcode).

Os **códigos** neste repositório, nos blocos de código dos [jupyter notebooks](https://jupyter.org/) ou em arquivos separados de códigos, estão disponíveis sob a [licença GNU-GPL](LICENSE-CODE). Mais informações sobre essa licença em [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl.html).
