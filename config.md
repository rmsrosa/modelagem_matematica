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
    ],
    "*PART II",
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
