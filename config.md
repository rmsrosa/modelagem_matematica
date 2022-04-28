# Configuration

## config vars
+++
prepath = "modelagem_matematica"
content_tag = ""
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
show_aside = false
show_github = true
github_repo = "https://github.com/rmsrosa/modelagem_matematica"
github_branch = "modmat2022p1"
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
    "*PARTE I",
    "Preliminares" => [
        "src/jupyter/c01/0101-Aspectos_curso.ipynb"
        "src/jupyter/c01/0102-Instalando_acessando_Julia.ipynb"
        "src/jupyter/c01/0103-Primeiros_passos_Julia.ipynb"
    ],
   "*PARTE II",
    "Princípios de Modelagem Matemática" => [
        "src/jupyter/c02/0201-Principios_basicos.ipynb"
        "src/jupyter/c02/0202-Exemplos_tipos_modelagem.ipynb"
    ],
    "Análise Dimensional" => [
        "src/jupyter/c03/0301-Quantidades_unidades_dimensoes.ipynb"
        "src/jupyter/c03/0302-BuckinghamPi.ipynb"
        "src/jupyter/c03/0303-Unidades_Julia.ipynb"
    ],
    "Ajuste de Parâmetros" => [
        "src/jupyter/c04/0401-Minimos_quadrados_ajuste.ipynb"
        "src/jupyter/c04/0402-Exemplos_ajuste_linear.ipynb"
        "src/jupyter/c04/0403-Modelos_redutiveis_linear_aplicacoes.ipynb"
        "src/jupyter/c04/0404-Minimos_quadrados_nao_linear.ipynb"
        "src/jupyter/c04/0405-Exemplos_ajuste_naolinear.ipynb"
        "src/jupyter/c04/0406-Ajuste_em_redes_neurais.ipynb"
    ],
    "Erros e Incertezas" => [
        "src/jupyter/c05/0501-Erros_e_incertezas.ipynb"
        "src/jupyter/c05/0502-Minimos_quadrados_verossimilhanca.ipynb"
        "src/jupyter/c05/0503-Propagacao_incertezas.ipynb"
    ],
]
menu_left = [
    "Avaliação de Modelos" => [
        "src/jupyter/c06/0601-Qualidade_do_modelo.ipynb"
        "src/jupyter/c06/0602-Validacao_do_modelo.ipynb"
        "src/jupyter/c06/0603-Comparacao_de_modelos.ipynb"
    ],
    "*PARTE III",
    "Mecânica" => [
        "src/jupyter/c07/0700-Mecanica.ipynb"
        "src/jupyter/c07/0701-Mecanica_Newtoniana.ipynb"
        "src/jupyter/c07/0702-Mecanica_Lagrangiana.ipynb"
        "src/jupyter/c07/0703-Conservacao_contexto_Newtoniano.ipynb"
        "src/jupyter/c07/0704-Conservacao_contexto_Lagrangiano.ipynb"
        "src/jupyter/c07/0705-Hamiltonianos.ipynb"
        "src/jupyter/c07/0706-Pendulo.ipynb"
        "src/jupyter/c07/0707-Pendulo_angulos_grandes.ipynb"
    ],
    "Modelos em Eletrônica" => [
        "src/jupyter/c08/0800-Eletronica.ipynb"
        "src/jupyter/c08/0801-Modelo_diodo.ipynb"
    ],
    "Reações Químicas" => [
        "src/jupyter/c09/0901-Lei_acao_de_massas.ipynb"
        "src/jupyter/c09/0902-Reacoes_enzimaticas.ipynb"
        "src/jupyter/c09/0903-Isomerizacao.ipynb"
    ],
    "Modelos Epidemiológicos" => [
        "src/jupyter/c10/1000-Modelos_epidemiologicos.ipynb"
        "src/jupyter/c10/1001-Modelos_epidemiologicos_compartimentais.ipynb"
        "src/jupyter/c10/1002-Ajuste_SIR.ipynb"
        "src/jupyter/c10/1003-Compartimentais_estruturados.ipynb"
    ],
    "Séries de Fourier e Aplicações" => [
        "src/jupyter/c11/1100-Fourier_e_aplicacoes.ipynb"
        "src/jupyter/c11/1101-Series_Fourier.ipynb"
        "src/jupyter/c11/1102-Transformada_discreta_Fourier.ipynb"
        "src/jupyter/c11/1103-Ondas_sonoras_elementos_musicais.ipynb"
        "src/jupyter/c11/1104-Compressao_audio.ipynb"
    ],
    "Equações a Derivadas Parciais" => [
        "src/jupyter/c12/1201-EDP_e_diferencas_finitas.ipynb"
        "src/jupyter/c12/1202-EDP_advecao.ipynb"
        "src/jupyter/c12/1203-EDP_calor.ipynb"
        "src/jupyter/c12/1204-EDP_onda.ipynb"
        "src/jupyter/c12/1205-EDP_calor_bidimensional.ipynb"
        "src/jupyter/c12/1206-EDP_onda_bidimensional.ipynb"
        "src/jupyter/c12/1207-Ondas_sismicas.ipynb"
        "src/jupyter/c12/1208-Resfriamento_rapido_morangos.ipynb"
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
exec_notebook = false
website = "rmsrosa.github.io/modelagem_matematica"
+++

## binder variables
+++
nbgitpuller_repo = "rmsrosa/modelagem_matematica"
nbgitpuller_branch = "julia-env-for-binder-2022p1"
binder_application = "lab" 
+++
