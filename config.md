# Configuration

## config vars
+++
prepath = "modelagem_matematica"
content_tag = ""
ignore = ["_weave/", "_jupyter/", "_literate"]
+++

## book variables
+++
book_title = "Modelagem Matemática"
book_subtitle = "Notas de aula"
book_author = "<a href=\"https://rmsrosa.github.io\">Ricardo M. S. Rosa</a>"
show_license = true
book_license = "(CC BY-NC-ND 4.0) Attribution-NonCommercial-NoDerivatives 4.0 International"
license_link = "https://creativecommons.org/licenses/by-nc-nd/4.0/"
book_licensees = ""
+++

## menu variables
+++
show_aside = true
show_github = true
github_repo = "https://github.com/rmsrosa/modelagem_matematica/tree/modmat2022p1"
+++

## navigation links
+++
nav_on_top = true
nav_on_bottom = true
+++

## toc variables
+++
page_numbering = true
menu = [
    "*pages/intro",
    "*PART I",
    "Preliminares" => [
        "_jupyter/c01/01.01-Aspectos_curso.ipynb"
        "_jupyter/c01/01.02-Instalando_acessando_Julia.ipynb"
        "_jupyter/c01/01.03-Primeiros_passos_Julia.ipynb"
    ],
   "*PART II",
    "Princípios de Modelagem Matemática" => [
        "_jupyter/c02/02.01-Principios_basicos.ipynb"
        "_jupyter/c02/02.02-Exemplos_tipos_modelagem.ipynb"
    ],
    "Análise Dimensional" => [
        "_jupyter/c03/03.01-Quantidades_unidades_dimensoes.ipynb"
        "_jupyter/c03/03.02-BuckinghamPi.ipynb"
        "_jupyter/c03/03.03-Unidades_Julia.ipynb"
    ],
]
menu_left = [
    "Ajuste de Parâmetros" => [
        "_jupyter/c04/04.01-Minimos_quadrados_ajuste.ipynb"
        "_jupyter/c04/04.02-Modelos_redutiveis_linear_aplicacoes.ipynb"
        "_jupyter/c04/04.03-Minimos_quadrados_nao_linear.ipynb"
        "_jupyter/c04/04.04-Exemplos_ajuste_naolinear.ipynb"
        "_jupyter/c04/04.05-Ajuste_em_redes_neurais.ipynb"
    ],
    "Erros e Incertezas" => [
        "_jupyter/c05/05.01-Erros_e_incertezas.ipynb"
        "_jupyter/c05/05.02-Minimos_quadrados_verossimilhanca.ipynb"
        "_jupyter/c05/05.03-Propagacao_incertezas.ipynb"
    ],
    "Avaliação de Modelos" => [
        "_jupyter/c06/06.01-Qualidade_do_modelo.ipynb"
        "_jupyter/c06/06.02-Validacao_do_modelo.ipynb"
        "_jupyter/c06/06.03-Comparacao_de_modelos.ipynb"
    ],
    "*PARTE III",
    "Mecânica" => [
        "_jupyter/c07/07.00-Mecanica.ipynb"
        "_jupyter/c07/07.01-Mecanica_Newtoniana.ipynb"
        "_jupyter/c07/07.02-Mecanica_Lagrangiana.ipynb"
        "_jupyter/c07/07.03-Conservacao_contexto_Newtoniano.ipynb"
        "_jupyter/c07/07.04-Conservacao_contexto_Lagrangiano.ipynb"
        "_jupyter/c07/07.05-Hamiltonianos.ipynb"
        "_jupyter/c07/07.06-Pendulo.ipynb"
        "_jupyter/c07/07.07-Pendulo_angulos_grandes.ipynb"
    ],
    "Modelos em Eletrônica" => [
        "_jupyter/c08/08.00-Eletronica.ipynb"
        "_jupyter/c08/08.01-Modelo_diodo.ipynb"
    ],
    "Reações Químicas" => [
        "_jupyter/c09/09.01-Lei_acao_de_massas.ipynb"
        "_jupyter/c09/09.02-Reacoes_enzimaticas.ipynb"
        "_jupyter/c09/09.03-Isomerizacao.ipynb"
    ],
    "Modelos Epidemiológicos" => [
        "_jupyter/c10/10.00-Modelos_epidemiologicos.ipynb"
        "_jupyter/c10/10.01-Modelos_epidemiologicos_compartimentais.ipynb"
        "_jupyter/c10/10.02-Ajuste_SIR.ipynb"
        "_jupyter/c10/10.03-Compartimentais_estruturados.ipynb"
    ],
    "Séries de Fourier e Aplicações" => [
        "_jupyter/c11/11.00-Fourier_e_aplicacoes.ipynb"
        "_jupyter/c11/11.01-Series_Fourier.ipynb"
        "_jupyter/c11/11.02-Transformada_discreta_Fourier.ipynb"
        "_jupyter/c11/11.03-Ondas_sonoras_elementos_musicais.ipynb"
        "_jupyter/c11/11.04-Compressao_audio.ipynb"
    ],
    "Equações a Derivadas Parciais" => [
        "_jupyter/c12/12.01-EDP_e_diferencas_finitas.ipynb"
        "_jupyter/c12/12.02-EDP_advecao.ipynb"
        "_jupyter/c12/12.03-EDP_calor.ipynb"
        "_jupyter/c12/12.04-EDP_onda.ipynb"
        "_jupyter/c12/12.05-EDP_calor_bidimensional.ipynb"
        "_jupyter/c12/12.06-EDP_onda_bidimensional.ipynb"
        "_jupyter/c12/12.07-Ondas_sismicas.ipynb"
        "_jupyter/c12/12.08-Resfriamento_rapido_morangos.ipynb"
    ],
    "*pages/appendix",
]
+++

## page variables
+++
show_link_bagdes = true
link_view_source = true
link_download_notebook = true
link_nbview_notebook = true
link_binder_notebook = true
website = "rmsrosa.github.io/modelagem_matematica/tree/modmat2021p1"
+++

## binder variables
+++
nbgitpuller_repo = "rmsrosa/modelagem_matematica"
nbgitpuller_branch = "julia-env-for-binder-2022p1"
binder_application = "lab" 
+++
