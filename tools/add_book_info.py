import os

import nbformat
from nbformat.v4.nbbase import new_markdown_cell

from generate_contents import iter_notebooks, NOTEBOOK_DIR


BOOK_COMMENT = "<!--BOOK_INFORMATION-->"


BOOK_INFO = BOOK_COMMENT + """
<!--<img align="left" style="padding-right:10px;" src="figures/PDSH-cover-small.png">-->

*[Notas de aula da disciplina de 
Modelagem Matemática](https://github.com/rmsrosa/modelagem_matematica)
do [IM-UFRJ](https://www.im.ufrj.br).*"""


def add_book_info():
    for nb_name in iter_notebooks():
        nb_file = os.path.join(NOTEBOOK_DIR, nb_name)
        nb = nbformat.read(nb_file, as_version=4)

        is_comment = lambda cell: cell.source.startswith(BOOK_COMMENT)

        if is_comment(nb.cells[0]):
            print('- amending comment for {0}'.format(nb_name))
            nb.cells[0].source = BOOK_INFO
        else:
            print('- inserting comment for {0}'.format(nb_name))
            nb.cells.insert(0, new_markdown_cell(BOOK_INFO))
        nbformat.write(nb, nb_file)


if __name__ == '__main__':
    add_book_info()
